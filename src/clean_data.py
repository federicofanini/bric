import pandas as pd
import numpy as np

def clean_brach_data(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Clean column names
    df.columns = [col.strip() for col in df.columns]
    
    # Convert comma decimal separators to periods and convert to numeric
    numeric_columns = ['GDP PER CAPITA (current US$)', 'GDP PER CAPITA GROWTH RATE', 'HDI*', 
                      'EDUCATION EXPENDITURE (% OF GDP)', 'HEALTH EXPENDITURE (% OF GDP)']
    
    for col in numeric_columns:
        if col in df.columns:
            df[col] = df[col].str.replace(',', '.').astype(float)
    
    # Drop empty columns and unnamed columns
    df = df.dropna(axis=1, how='all')
    unnamed_cols = [col for col in df.columns if 'Unnamed' in col]
    df = df.drop(columns=unnamed_cols)
    
    # Rename columns for easier access
    df = df.rename(columns={
        'GDP PER CAPITA (current US$)': 'GDP_per_capita',
        'GDP PER CAPITA GROWTH RATE': 'GDP_growth_rate',
        'HDI*': 'HDI',
        'EDUCATION EXPENDITURE (% OF GDP)': 'education_expenditure',
        'HEALTH EXPENDITURE (% OF GDP)': 'health_expenditure'
    })
    
    # Ensure YEAR is numeric
    df['YEAR'] = pd.to_numeric(df['YEAR'], errors='coerce')
    
    # Sort by year
    df = df.sort_values('YEAR')
    
    # Reset index
    df = df.reset_index(drop=True)
    
    return df

if __name__ == "__main__":
    # Clean the data
    cleaned_df = clean_brach_data('data/BRACH_A.csv')
    
    # Save the cleaned data
    cleaned_df.to_csv('data/BRACH_A_cleaned.csv', index=False)
    
    # Print basic information about the cleaned data
    print("\nCleaned Data Information:")
    print(cleaned_df.info())
    print("\nFirst few rows of cleaned data:")
    print(cleaned_df.head())
    print("\nSummary statistics:")
    print(cleaned_df.describe()) 