import statsmodels.api as sm
import pandas as pd

def run_chain_a(df):
    # Chain A: Economic Growth → Human Development
    X = df[['gdp_growth', 'education_expenditure', 'health_expenditure']]
    y = df['hdi']
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit(cov_type='HC3')

    print(f"\n[Chain A] R²: {model.rsquared:.4f} | Adj. R²: {model.rsquared_adj:.4f}")
    return model

def run_chain_b(df):
    # Chain B: Human Development → Economic Growth
    X = df[['hdi', 'education_expenditure', 'health_expenditure']]
    y = df['gdp_growth']
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit(cov_type='HC3')

    print(f"\n[Chain B] R²: {model.rsquared:.4f} | Adj. R²: {model.rsquared_adj:.4f}")
    return model

def run_country_ols(df):
    """
    Perform OLS analysis for each country separately.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing the BRIC data with columns:
        - country: country name
        - year: year of observation
        - gdp_growth: GDP growth rate
        - hdi: Human Development Index
        - education_expenditure: Education expenditure as % of GDP
        - health_expenditure: Health expenditure as % of GDP
    
    Returns:
    --------
    dict
        Dictionary containing OLS models for each country
    """
    countries = df['country'].unique()
    country_models = {}
    
    for country in countries:
        country_df = df[df['country'] == country]
        
        # Model 1: HDI as dependent variable
        X1 = country_df[['gdp_growth', 'education_expenditure', 'health_expenditure']]
        y1 = country_df['hdi']
        X1 = sm.add_constant(X1)
        model1 = sm.OLS(y1, X1).fit(cov_type='HC3')
        
        # Model 2: GDP growth as dependent variable
        X2 = country_df[['hdi', 'education_expenditure', 'health_expenditure']]
        y2 = country_df['gdp_growth']
        X2 = sm.add_constant(X2)
        model2 = sm.OLS(y2, X2).fit(cov_type='HC3')
        
        country_models[country] = {
            'hdi_model': model1,
            'gdp_model': model2
        }
        
        print(f"\n=== {country} ===")
        print(f"HDI Model R²: {model1.rsquared:.4f} | Adj. R²: {model1.rsquared_adj:.4f}")
        print(f"GDP Model R²: {model2.rsquared:.4f} | Adj. R²: {model2.rsquared_adj:.4f}")
    
    return country_models
