import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import os
from load_data import load_bric_data

# Create output directories if they don't exist
os.makedirs('outputs', exist_ok=True)
os.makedirs('figures', exist_ok=True)

# Define the variables for analysis
CHAIN_VARS = {
    'A': {
        'independent_vars': ['gdp_growth', 'education_expenditure', 'health_expenditure'],
        'dependent_var': 'hdi'
    },
    'B': {
        'independent_vars': ['gdp_growth', 'gcf'],
        'dependent_var': 'hdi'
    }
}

def perform_ols_analysis(df, dependent_var, independent_vars, country):
    # Prepare the data
    X = df[independent_vars]
    X = sm.add_constant(X)  # Add constant term for intercept
    y = df[dependent_var]
    
    # Drop rows with missing values
    valid_data = pd.concat([y, X], axis=1).dropna()
    y = valid_data[dependent_var]
    X = valid_data.drop(columns=[dependent_var])
    
    # Perform OLS regression
    model = sm.OLS(y, X)
    results = model.fit()
    
    return results, X, y

def analyze_country_chain(country_code, chain):
    print(f"\nAnalyzing {country_code} - Chain {chain}")
    
    # Get variables for this chain
    chain_config = CHAIN_VARS[chain]
    independent_vars = chain_config['independent_vars']
    dependent_var = chain_config['dependent_var']
    
    # Load data for specific country and chain
    df = load_bric_data(country_code=country_code, chain=chain)
    
    # Print HDI values
    print("\nHDI Values:")
    print(df[['year', 'hdi']].to_string(index=False))
    
    # Perform the analysis
    results, X, y = perform_ols_analysis(df, dependent_var, independent_vars, country_code)
    
    # Save results to file
    with open(f'outputs/{country_code}_chain_{chain}_ols_results.txt', 'w') as f:
        f.write(results.summary().as_text())
    
    # Create correlation matrix
    corr_vars = ['hdi'] + independent_vars
    correlation_matrix = df[corr_vars].corr()
    
    # Plot correlation heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title(f'Correlation Matrix - {country_code} Chain {chain}')
    plt.tight_layout()
    plt.savefig(f'figures/{country_code}_chain_{chain}_correlation_matrix.png')
    plt.close()
    
    # Plot actual vs predicted values
    y_pred = results.predict(X)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(y, y_pred, alpha=0.5)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
    plt.xlabel('Actual HDI')
    plt.ylabel('Predicted HDI')
    plt.title(f'Actual vs Predicted HDI Values - {country_code} Chain {chain}')
    plt.tight_layout()
    plt.savefig(f'figures/{country_code}_chain_{chain}_actual_vs_predicted.png')
    plt.close()
    
    # Print key findings
    print(f"\nKey Findings for {country_code} - Chain {chain}:")
    print(f"R-squared: {results.rsquared:.4f}")
    print(f"Adjusted R-squared: {results.rsquared_adj:.4f}")
    print("\nCoefficients:")
    for var, coef in zip(['Intercept'] + independent_vars, results.params):
        print(f"{var}: {coef:.4f}")
    print("\nP-values:")
    for var, pval in zip(['Intercept'] + independent_vars, results.pvalues):
        print(f"{var}: {pval:.4f}")

# Analyze each BRIC country for both chains
countries = ['BR', 'RU', 'IN', 'CN']
chains = ['A', 'B']

for country in countries:
    for chain in chains:
        analyze_country_chain(country, chain) 