import pandas as pd
import numpy as np
import statsmodels.api as sm

def generate_trend_table(df):
    """Genera tabella dei trend temporali per paese"""
    trend_data = []
    for country in df['country'].unique():
        country_df = df[df['country'] == country]
        for col in ['gdp_growth', 'hdi']:
            model = sm.OLS(country_df[col], sm.add_constant(country_df['year'])).fit()
            slope = model.params.iloc[1]
            trend_data.append({
                'Country': country,
                'Variable': col,
                'Mean': country_df[col].mean(),
                'Std Dev': country_df[col].std(),
                'Trend (slope)': slope
            })
    trend_df = pd.DataFrame(trend_data)
    trend_df = trend_df.round(4)
    return trend_df

def generate_regression_summary(all_results):
    """Genera tabella di sintesi R² per paese e chain"""
    summary_data = []
    for country, country_results in all_results.items():
        row = {'Country': country}
        for model_name, model_data in country_results.items():
            chain = model_name.split('_')[0]
            lag_type = model_name.split('_')[1]
            row[f'Chain {chain} ({lag_type})'] = model_data['r2']
        summary_data.append(row)
    summary_df = pd.DataFrame(summary_data)
    summary_df = summary_df.round(4)
    return summary_df

def generate_regression_coefficients(all_results):
    """Genera tabella dettagliata dei coefficienti di regressione"""
    regression_table = []
    for country, country_results in all_results.items():
        for model_name, model_data in country_results.items():
            chain = model_name.split('_')[0]
            lag_type = model_name.split('_')[1]
            for var_name, coef in model_data['params'].items():
                if var_name != 'const':
                    regression_table.append({
                        'Country': country,
                        'Chain': chain,
                        'Model': lag_type,
                        'Variable': var_name,
                        'Coefficient': coef,
                        'P-value': model_data['pvalues'][var_name],
                        'R2': model_data['r2']
                    })
    
    regression_df = pd.DataFrame(regression_table)
    regression_df = regression_df.round(4)
    return regression_df

def generate_durbin_watson_table(all_results, df):
    """Genera tabella dei test di Durbin-Watson"""
    dw_data = []
    for country, country_results in all_results.items():
        for model_name, model_data in country_results.items():
            chain = model_name.split('_')[0]
            lag_type = model_name.split('_')[1]
            if 'residuals' in model_data:
                dw_stat = sm.stats.stattools.durbin_watson(model_data['residuals'])
                dw_data.append({
                    'Country': country,
                    'Chain': chain,
                    'Model': lag_type,
                    'DW Statistic': dw_stat
                })
    
    dw_df = pd.DataFrame(dw_data)
    dw_df = dw_df.round(4)
    return dw_df

def generate_cycle_distribution_table(cycle_analyses):
    """Genera tabella della distribuzione dei cicli"""
    cycle_counts = {}
    for analysis in cycle_analyses.values():
        cycle_type = analysis['classification']
        cycle_counts[cycle_type] = cycle_counts.get(cycle_type, 0) + 1
    
    dist_df = pd.DataFrame([
        {'Cycle Type': cycle_type, 'Count': count}
        for cycle_type, count in cycle_counts.items()
    ])
    return dist_df

def generate_cycle_analysis_table(cycle_analyses):
    """Genera tabella dell'analisi dei cicli"""
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
    return cycle_df

def generate_performance_comparison(df, cycle_analyses):
    """Genera tabella comparativa delle performance dei paesi"""
    performance_data = []
    for country in df['country'].unique():
        country_df = df[df['country'] == country]
        performance_data.append({
            'Country': country,
            'Avg Growth': country_df['gdp_growth'].mean(),
            'Avg HDI': country_df['hdi'].mean(),
            'Growth Rank': None,  # Sarà calcolato dopo
            'HDI Rank': None,     # Sarà calcolato dopo
            'Classification': cycle_analyses[country]['classification']
        })
    
    perf_df = pd.DataFrame(performance_data)
    # Calcola i rank
    perf_df['Growth Rank'] = perf_df['Avg Growth'].rank(ascending=False)
    perf_df['HDI Rank'] = perf_df['Avg HDI'].rank(ascending=False)
    perf_df = perf_df.round(4)
    return perf_df

def generate_all_tables(df, all_results, cycle_analyses):
    """Genera e salva tutte le tabelle"""
    # 1. Trend Analysis
    trend_table = generate_trend_table(df)
    trend_table.to_markdown('tables/trend_analysis.md')
    
    # 2. Regression Summary
    regression_summary = generate_regression_summary(all_results)
    regression_summary.to_markdown('tables/regression_summary.md')
    
    # 3. Regression Coefficients
    regression_coefficients = generate_regression_coefficients(all_results)
    regression_coefficients.to_markdown('tables/regression_coefficients.md')
    
    # 4. Durbin-Watson Tests
    dw_table = generate_durbin_watson_table(all_results, df)
    dw_table.to_markdown('tables/durbin_watson_tests.md')
    
    # 5. Cycle Distribution
    cycle_dist = generate_cycle_distribution_table(cycle_analyses)
    cycle_dist.to_markdown('tables/cycle_distribution.md')
    
    # 6. Cycle Analysis
    cycle_analysis = generate_cycle_analysis_table(cycle_analyses)
    cycle_analysis.to_markdown('tables/cycle_analysis.md')
    
    # 7. Performance Comparison
    perf_comparison = generate_performance_comparison(df, cycle_analyses)
    perf_comparison.to_markdown('tables/performance_comparison.md')
    
    print("✅ All tables generated and saved to tables/ directory")
