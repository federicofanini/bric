import pandas as pd
import numpy as np

# Mapping of Excel sheet names by country and chain
COUNTRY_SHEETS = {
    'BR_A': 'BRA CH.A',
    'BR_B': 'BRA CH.B',
    'RU_A': 'RUS A',
    'RU_B': 'RUS B',
    'IN_A': 'IND A',
    'IN_B': 'IND B',
    'CN_A': 'CHN A',
    'CN_B': 'CHN B'
}

# Mapping of original column names to standard format
CHAIN_COLUMNS = {
    'A': {
        'YEAR': 'year',
        'GDP_pc': 'gdp_per_capita',
        'GDP_pc_g_rate': 'gdp_growth',
        'HDI': 'hdi',
        'ed_exp': 'education_expenditure',
        'hlt_exp': 'health_expenditure'
    },
    'B': {
        'YEAR': 'year',
        'GDP_pc_g_rate': 'gdp_growth',
        'HDI': 'hdi',
        'gcf': 'gcf'
    }
}

def load_bric_data(path='data/dataset.xlsx'):
    """
    Load and normalize BRIC data from an Excel file, combining all countries and both chains (A and B).
    
    Args:
        path (str): Path to the Excel file containing raw data.
    
    Returns:
        pd.DataFrame: Combined, cleaned, and labeled annual data for all countries and chains.
    """
    all_dfs = []

    for key, sheet_name in COUNTRY_SHEETS.items():
        country_code, chain = key.split('_')
        country_map = {'BR': 'Brazil', 'RU': 'Russia', 'IN': 'India', 'CN': 'China'}
        country = country_map[country_code]
        columns_map = CHAIN_COLUMNS[chain]

        # Load and clean the sheet
        df = pd.read_excel(path, sheet_name=sheet_name)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df.columns = df.columns.str.strip()
        df = df.rename(columns=columns_map)

        # Add metadata columns
        df['country'] = country
        df['chain'] = chain

        # Normalize numeric values
        for col in columns_map.values():
            if col in df.columns:
                df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', '.'), errors='coerce')
                df[col] = df[col].replace([np.inf, -np.inf], np.nan)

        all_dfs.append(df)

    # Combine all sheets
    full_df = pd.concat(all_dfs, ignore_index=True)
    full_df = full_df.sort_values(['country', 'year', 'chain']).reset_index(drop=True)

    return full_df
