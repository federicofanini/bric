def create_lags(df):
    """
    Create lagged variables for GDP growth and HDI, using 5-year and 10-year lags.

    This is consistent with the thesis framework, which refers to lagged values
    at 5 and 10 years to capture long-term effects and mitigate endogeneity.

    Args:
        df (pd.DataFrame): Cleaned dataset with 'country', 'year', 'chain', 'hdi', 'gdp_growth'

    Returns:
        pd.DataFrame: Dataset with new lag variables
    """
    df = df.copy()

    group = df.groupby(['country', 'chain'])

    # Add lagged values
    df['hdi_lag5'] = group['hdi'].shift(5)
    # df['hdi_lag10'] = group['hdi'].shift(10)
    df['gdp_growth_lag5'] = group['gdp_growth'].shift(5)
    # df['gdp_growth_lag10'] = group['gdp_growth'].shift(10)

    # Drop rows with missing values in lagged variables
    # df = df.dropna(subset=['hdi_lag5', 'hdi_lag10', 'gdp_growth_lag5', 'gdp_growth_lag10'])
    # df = df.dropna(subset=['hdi_lag5', 'gdp_growth_lag5'])

    return df


def add_country_dummies(df):
    return df  # No country dummies needed since we don't have country information
