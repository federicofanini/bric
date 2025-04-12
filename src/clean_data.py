import pandas as pd
import os

def clean_bric_data(df):
    """
    Clean BRIC annual dataset and export it to structured Excel file for regression use.

    - Removes rows with missing required variables based on chain type.
    - Explicitly drops 'gcf' from Chain A (not used).
    - Exports full, per-chain, and per-country datasets.

    Args:
        df (pd.DataFrame): Combined dataset from load_bric_data().

    Returns:
        pd.DataFrame: Cleaned dataset ready for regression.
    """
    df = df.copy()

    # Split data by chain type
    chain_a = df[df['chain'] == 'A']
    chain_b = df[df['chain'] == 'B']

    # Remove 'gcf' from Chain A as it's not used in that chain
    chain_a = chain_a.drop(columns=['gcf'], errors='ignore')  # errors='ignore' in case column doesn't exist

    # Drop rows with missing required values
    chain_a = chain_a.dropna(subset=['gdp_growth', 'hdi', 'education_expenditure', 'health_expenditure'])
    chain_b = chain_b.dropna(subset=['gdp_growth', 'hdi', 'gcf'])

    # Export to Excel
    output_path = 'data/processed/bric_regression_data.xlsx'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        # Export Chain A data
        chain_a.to_excel(writer, sheet_name='Chain_A', index=False)
        
        # Export Chain B data
        chain_b.to_excel(writer, sheet_name='Chain_B', index=False)

        # Export per country data
        for country in df['country'].unique():
            # Chain A data for country
            country_a = chain_a[chain_a['country'] == country]
            if not country_a.empty:
                sheet_name = f'{country}_A'[:31]  # Excel sheet name limit
                country_a.to_excel(writer, sheet_name=sheet_name, index=False)
            
            # Chain B data for country
            country_b = chain_b[chain_b['country'] == country]
            if not country_b.empty:
                sheet_name = f'{country}_B'[:31]  # Excel sheet name limit
                country_b.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"\n✅ Cleaned dataset exported to: {output_path}")
    
    # Return combined dataset for further analysis
    return pd.concat([chain_a, chain_b], ignore_index=True)
