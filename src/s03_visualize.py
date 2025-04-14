import seaborn as sns
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
from scipy import stats

def ensure_output_dir():
    os.makedirs('figures', exist_ok=True)
    os.makedirs('figures/descriptive', exist_ok=True)
    os.makedirs('figures/diagnostics', exist_ok=True)
    os.makedirs('tables', exist_ok=True)

def plot_time_series(df, column, title, ylabel, filename):
    plt.figure(figsize=(10, 6))
    plt.plot(df['year'], df[column], marker='o')
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.savefig(f'figures/descriptive/{filename}.png')
    plt.close()

def plot_scatter(df, x_col, y_col, title, filename):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_col], df[y_col])
    plt.xlabel(x_col.replace('_', ' ').title())
    plt.ylabel(y_col.replace('_', ' ').title())
    plt.title(title)
    plt.grid(True)
    plt.savefig(f'figures/descriptive/{filename}.png')
    plt.close()

def plot_heatmap(df, columns, title, filename):
    plt.figure(figsize=(10, 8))
    corr = df[columns].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(f'figures/descriptive/{filename}.png')
    plt.close()

def plot_boxplot(df, column, by_country=True, filename=None):
    plt.figure(figsize=(10, 6))
    if by_country:
        sns.boxplot(x='country', y=column, data=df)
        plt.title(f'Boxplot of {column} by Country')
    else:
        sns.boxplot(y=column, data=df)
        plt.title(f'Boxplot of {column}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    if filename:
        plt.savefig(f'figures/descriptive/{filename}.png')
    plt.close()

def plot_histogram(df, column, by_country=False, filename=None):
    plt.figure(figsize=(10, 6))
    if by_country:
        for country in df['country'].unique():
            sns.histplot(data=df[df['country'] == country], x=column, 
                        kde=True, label=country, alpha=0.5)
        plt.legend()
    else:
        sns.histplot(data=df, x=column, kde=True)
    plt.title(f'Distribution of {column}')
    plt.tight_layout()
    if filename:
        plt.savefig(f'figures/descriptive/{filename}.png')
    plt.close()

def generate_descriptive_stats(df):
    """Generate comprehensive descriptive statistics and save to markdown"""
    stats_md = "# Descriptive Analysis of BRIC Data\n\n"
    
    # Basic statistics
    stats_md += "## 1. Basic Statistics\n\n"
    stats_md += "### By Country\n\n"
    for country in df['country'].unique():
        stats_md += f"#### {country}\n\n"
        country_df = df[df['country'] == country]
        stats_md += country_df.describe().to_markdown() + "\n\n"
    
    # Correlation analysis
    stats_md += "## 2. Correlation Analysis\n\n"
    corr_matrix = df[['gdp_growth', 'hdi', 'education_expenditure', 'health_expenditure']].corr()
    stats_md += corr_matrix.to_markdown() + "\n\n"
    
    # Time series analysis
    stats_md += "## 3. Time Series Analysis\n\n"
    for country in df['country'].unique():
        stats_md += f"### {country}\n\n"
        country_df = df[df['country'] == country]
        for col in ['gdp_growth', 'hdi']:
            stats_md += f"#### {col}\n\n"
            stats_md += f"- Mean: {country_df[col].mean():.2f}\n"
            stats_md += f"- Std Dev: {country_df[col].std():.2f}\n"
            stats_md += f"- Trend (slope): {stats.linregress(country_df['year'], country_df[col]).slope:.4f}\n\n"
    
    # Distribution analysis
    stats_md += "## 4. Distribution Analysis\n\n"
    for col in ['gdp_growth', 'hdi', 'education_expenditure', 'health_expenditure']:
        stats_md += f"### {col}\n\n"
        stats_md += f"- Skewness: {df[col].skew():.2f}\n"
        stats_md += f"- Kurtosis: {df[col].kurtosis():.2f}\n"
        stats_md += f"- Shapiro-Wilk test p-value: {stats.shapiro(df[col])[1]:.4f}\n\n"
    
    return stats_md

def create_descriptive_plots(df):
    """Create all descriptive plots"""
    ensure_output_dir()
    
    # Time series plots
    for country in df['country'].unique():
        country_df = df[df['country'] == country]
        for col in ['gdp_growth', 'hdi']:
            plot_time_series(country_df, col, 
                           f'{col} over time - {country}',
                           col.replace('_', ' ').title(),
                           f'{country}_{col}_time_series')
    
    # Scatter plots
    plot_scatter(df, 'gdp_growth', 'hdi', 
                'GDP Growth vs HDI', 'gdp_hdi_scatter')
    
    # Correlation heatmap
    plot_heatmap(df, ['gdp_growth', 'hdi', 'education_expenditure', 'health_expenditure'],
                'Correlation Matrix', 'correlation_matrix')
    
    # Boxplots
    for col in ['gdp_growth', 'hdi', 'education_expenditure', 'health_expenditure']:
        plot_boxplot(df, col, True, f'{col}_boxplot')
    
    # Histograms
    for col in ['gdp_growth', 'hdi', 'education_expenditure', 'health_expenditure']:
        plot_histogram(df, col, True, f'{col}_histogram')

def generate_descriptive_table(df: pd.DataFrame) -> str:
    """
    Genera una tabella markdown con le statistiche descrittive.
    
    Args:
        df: DataFrame con i dati
        
    Returns:
        str: Tabella in formato markdown
    """
    # Seleziona le colonne rilevanti
    cols = ['gdp_growth', 'hdi', 'education_expenditure', 'health_expenditure']
    
    # Calcola le statistiche per paese
    stats_by_country = {}
    for country in df['country'].unique():
        country_data = df[df['country'] == country]
        stats = {}
        for col in cols:
            stats[col] = {
                'mean': country_data[col].mean(),
                'std': country_data[col].std(),
                'min': country_data[col].min(),
                'max': country_data[col].max()
            }
        stats_by_country[country] = stats
    
    # Genera la tabella markdown
    markdown = "## Statistiche Descrittive per Paese\n\n"
    
    # Intestazione
    markdown += "| Paese | Variabile | Media | Dev. Std. | Min | Max |\n"
    markdown += "|-------|-----------|-------|-----------|-----|-----|\n"
    
    # Dati
    for country, stats in stats_by_country.items():
        for col, values in stats.items():
            markdown += f"| {country} | {col} | {values['mean']:.2f} | {values['std']:.2f} | {values['min']:.2f} | {values['max']:.2f} |\n"
    
    return markdown

def generate_results_tables(df: pd.DataFrame, regression_results: dict, cycle_analyses: dict) -> None:
    """
    Genera e salva le tabelle dei risultati in formato markdown.
    
    Args:
        df: DataFrame con i dati
        regression_results: Risultati delle regressioni
        cycle_analyses: Analisi dei cicli di sviluppo
    """
    # 1. Tabella delle statistiche descrittive
    desc_stats = df.groupby('country')[['gdp_growth', 'hdi', 'education_expenditure', 'health_expenditure']].agg(['mean', 'std', 'min', 'max'])
    desc_stats.columns = ['_'.join(col).strip() for col in desc_stats.columns.values]
    desc_stats = desc_stats.round(3)
    desc_stats.to_markdown('tables/descriptive_stats.md')

    # 2. Tabella delle correlazioni
    corr_matrix = df[['gdp_growth', 'hdi', 'education_expenditure', 'health_expenditure']].corr()
    corr_matrix = corr_matrix.round(3)
    corr_matrix.to_markdown('tables/correlation_matrix.md')

    # 3. Tabella dei risultati delle regressioni
    regression_table = []
    for country, country_results in regression_results.items():
        for chain_type, chain_results in country_results.items():
            for model_type, model_results in chain_results.items():
                # Estrai i coefficienti e i p-values
                for var_name, coef in model_results['params'].items():
                    if var_name != 'const':  # Escludi l'intercetta
                        regression_table.append({
                            'Country': country,
                            'Chain': chain_type,
                            'Model': model_type,
                            'Variable': var_name,
                            'Coefficient': coef,
                            'P-value': model_results['pvalues'][var_name],
                            'R2': model_results['r2']
                        })
    
    regression_df = pd.DataFrame(regression_table)
    regression_df = regression_df.round(4)
    regression_df.to_markdown('tables/regression_results.md')

    # 4. Tabella dell'analisi dei cicli
    cycle_table = []
    for country, analysis in cycle_analyses.items():
        cycle_table.append({
            'Country': country,
            'Classification': analysis['classification'],
            'Avg Growth': analysis['metrics']['avg_growth'],
            'Avg HDI': analysis['metrics']['avg_hdi'],
            'Growth Relative': analysis['metrics']['growth_relative'],
            'HDI Relative': analysis['metrics']['hdi_relative']
        })
    
    cycle_df = pd.DataFrame(cycle_table)
    cycle_df = cycle_df.round(3)
    cycle_df.to_markdown('tables/cycle_analysis.md')

    print("✅ Tables saved to 'tables/' directory")
