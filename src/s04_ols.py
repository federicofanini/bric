import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import os
from src.s05_ols_diagnostics import run_diagnostics

# Define chain-specific variables (lagged)
CHAIN_VARS = {
    'A': {
        'independent_vars': ['gdp_growth_lag5', 'education_expenditure', 'health_expenditure'],
        'dependent_var': 'hdi'
    },
    'B': {
        'independent_vars': ['hdi_lag5', 'gcf'],
        'dependent_var': 'gdp_growth'
    }
}

# Store results summary
results_summary = []

def perform_ols_analysis(df, dependent_var, independent_vars):
    """
    Esegue l'analisi OLS su un set di dati specifico.
    
    Args:
        df (pd.DataFrame): DataFrame contenente i dati
        dependent_var (str): Variabile dipendente
        independent_vars (list): Lista delle variabili indipendenti
        
    Returns:
        tuple: (model, X, y) dove model è il modello OLS, X sono le variabili indipendenti,
               e y è la variabile dipendente
    """
    # Prepare the data
    X = df[independent_vars]
    X = sm.add_constant(X)
    y = df[dependent_var]

    # Drop rows with missing values
    valid_data = pd.concat([y, X], axis=1).dropna()
    y = valid_data[dependent_var]
    X = valid_data.drop(columns=[dependent_var])

    if len(X) < len(independent_vars) + 2:
        print("⚠️ Not enough observations. Skipping regression.")
        return None, None, None

    # Perform OLS regression
    model = sm.OLS(y, X).fit(cov_type='HC3')
    return model, X, y

def save_regression_outputs(model, country, chain, label):
    """
    Salva gli output della regressione in file di testo e grafici.
    
    Args:
        model: Modello OLS
        country (str): Nome del paese
        chain (str): Catena di analisi ('A' o 'B')
        label (str): Etichetta per identificare il tipo di analisi
    """
    # Save regression summary
    txt_path = f'outputs/{country}_chain_{chain}_{label}_ols_results.txt'
    with open(txt_path, 'w') as f:
        f.write(model.summary().as_text())

    # Actual vs Predicted plot
    y_pred = model.predict(model.model.exog)
    y_true = model.model.endog

    plt.figure(figsize=(8, 6))
    plt.scatter(y_true, y_pred, alpha=0.6)
    plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--')
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.title(f'{country} Chain {chain} - {label.capitalize()}')
    plt.tight_layout()
    plt.savefig(f'figures/{country}_chain_{chain}_{label}_actual_vs_predicted.png')
    plt.close()

def analyze_country_chain(df, country, chain):
    """
    Analizza una specifica catena per un paese.
    
    Args:
        df (pd.DataFrame): DataFrame contenente i dati
        country (str): Nome del paese
        chain (str): Catena di analisi ('A' o 'B')
        
    Returns:
        dict: Dizionario contenente i risultati delle regressioni
    """
    print(f"\n🔍 Analyzing {country} - Chain {chain}")

    chain_config = CHAIN_VARS[chain]
    dep_var = chain_config['dependent_var']
    lagged_vars = chain_config['independent_vars']
    no_lag_vars = [v.replace('_lag5', '') for v in lagged_vars]

    df_country = df[(df['country'] == country) & (df['chain'] == chain)]

    if df_country.empty:
        print(f"⚠️ No data for {country} - Chain {chain}")
        return

    results = {}
    for label, vars_used in [('nolag', no_lag_vars), ('lag', lagged_vars)]:
        print(f"\n▶️ Running regression ({label})")
        model, X, y = perform_ols_analysis(df_country, dep_var, vars_used)

        if model is None:
            continue

        save_regression_outputs(model, country, chain, label)

        # Run diagnostics
        model_name = f"{country}_chain_{chain}_{label}"
        run_diagnostics(model, model_name=model_name)

        # Store results
        results[f'{chain}_{label}'] = {
            'r2': model.rsquared,
            'pvalues': dict(zip(model.model.exog_names, model.pvalues)),
            'params': dict(zip(model.model.exog_names, model.params))
        }

        # Print summary
        print(f"[{label.upper()}] R²: {model.rsquared:.4f} | Adj. R²: {model.rsquared_adj:.4f}")
        print("Coefficients:")
        for name, val in model.params.items():
            print(f"  {name}: {val:.4f}")
        print("P-values:")
        for name, val in model.pvalues.items():
            print(f"  {name}: {val:.4f}")

        # Save summary for CSV
        results_summary.append({
            'Country': country,
            'Chain': chain,
            'Lag': label,
            'R2': model.rsquared,
            'Adj_R2': model.rsquared_adj,
            'N_obs': int(model.nobs)
        })
    
    return results

def run_regression_analysis(df, countries, chains):
    """
    Esegue l'analisi di regressione per tutti i paesi e le catene specificati.
    
    Args:
        df (pd.DataFrame): DataFrame contenente i dati
        countries (list): Lista dei paesi da analizzare
        chains (list): Lista delle catene da analizzare
        
    Returns:
        dict: Dizionario contenente tutti i risultati delle regressioni
    """
    all_results = {}
    for country in countries:
        country_results = {}
        for chain in chains:
            results = analyze_country_chain(df, country, chain)
            if results:
                country_results.update(results)
        all_results[country] = country_results
    return all_results 