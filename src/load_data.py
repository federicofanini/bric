import pandas as pd
import numpy as np

# Define sheet name mapping
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

# Define column mappings for each chain
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

def load_bric_data(path='data/dataset.xlsx', country_code=None, chain=None):
    """
    Load BRIC data from Excel file.
    
    Args:
        path (str): Path to the Excel file
        country_code (str): Country code (BR, RU, IN, or CN)
        chain (str): Chain type ('A' or 'B')
        
    Returns:
        pd.DataFrame: Loaded and cleaned data
    """
    # Read the Excel file from specific sheet if country_code is provided
    if country_code and chain:
        sheet_key = f"{country_code}_{chain}"
        sheet_name = COUNTRY_SHEETS[sheet_key]
        df = pd.read_excel(path, sheet_name=sheet_name)
    else:
        # If no country_code provided, read all sheets and concatenate
        all_data = pd.read_excel(path, sheet_name=list(COUNTRY_SHEETS.values()))
        df = pd.concat([all_data[sheet] for sheet in COUNTRY_SHEETS.values()], 
                      keys=COUNTRY_SHEETS.keys(),
                      names=['country', 'index'])
        df = df.reset_index(level='country')
    
    # Clean column names
    df.columns = df.columns.str.strip()
    
    # Get the appropriate column mapping based on chain
    numeric_columns = CHAIN_COLUMNS[chain] if chain else CHAIN_COLUMNS['A']
    
    # Drop unnamed columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    
    # Rename columns
    df = df.rename(columns=numeric_columns)
    
    # Convert numeric columns and handle missing values
    for col in numeric_columns.values():
        if col in df.columns:
            # Convert to string, replace commas with dots, then to numeric
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', '.'), errors='coerce')
            
            # Replace infinite values with NaN
            df[col] = df[col].replace([np.inf, -np.inf], np.nan)
    
    # Drop rows with missing values in key columns
    required_columns = ['gdp_growth', 'hdi']
    if chain == 'A':
        required_columns.extend(['education_expenditure', 'health_expenditure'])
    elif chain == 'B':
        required_columns.append('gcf')
        
    df = df.dropna(subset=required_columns)
    
    # Sort by year
    df = df.sort_values('year')
    
    return df
