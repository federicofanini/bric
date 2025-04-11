def create_lags(df):
    df['hdi_lag5'] = df['hdi'].shift(5)
    df['gdp_growth_lag10'] = df['gdp_growth'].shift(10)
    return df.dropna(subset=['hdi_lag5', 'gdp_growth_lag10'])

def add_country_dummies(df):
    return df  # No country dummies needed since we don't have country information
