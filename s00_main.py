import pandas as pd
import numpy as np
import os
from src.s01_load_data import load_bric_data
from src.s02_clean_data import clean_bric_data
from src.utils import create_lags
from src.s05_ols_diagnostics import run_diagnostics
from src.s03_visualize import (
    create_descriptive_plots,
    generate_descriptive_table
)
from src.s06_classify_cycles import (
    analyze_cycle_dynamics, 
    plot_development_typology
)
from src.s04_ols import run_regression_analysis
from src.s07_tables import generate_all_tables

# Create output directories if they don't exist
os.makedirs('outputs', exist_ok=True)
os.makedirs('figures', exist_ok=True)
os.makedirs('figures/diagnostics', exist_ok=True)
os.makedirs('results', exist_ok=True)
os.makedirs('figures/descriptive', exist_ok=True)
os.makedirs('tables', exist_ok=True)

def main():
    # Step 1: Load and clean data
    print("\n📊 Step 1: Loading and cleaning data...")
    df = load_bric_data()
    df = clean_bric_data(df)
    print("✅ Data loaded and cleaned successfully")
    
    # Step 2: Perform descriptive analysis
    print("\n📊 Step 2: Performing descriptive analysis...")
    create_descriptive_plots(df)
    descriptive_table = generate_descriptive_table(df)
    with open('tables/descriptive_stats.md', 'w') as f:
        f.write(descriptive_table)
    print("✅ Descriptive analysis completed")
    
    # Step 3: Create lagged variables
    print("\n🔄 Step 3: Creating lagged variables...")
    df = create_lags(df)
    print("✅ Lagged variables created")
    
    # Step 4: Run regression analysis
    print("\n📈 Step 4: Running regression analysis...")
    countries = ['Brazil', 'Russia', 'India', 'China']
    chains = ['A', 'B']
    all_results = run_regression_analysis(df, countries, chains)
    print("✅ Regression analysis completed")

    # Step 5: Analyze development cycles
    print("\n🔄 Step 5: Analyzing development cycles...")
    cycle_analyses = analyze_cycle_dynamics(df)
    metrics = {country: analysis['metrics'] for country, analysis in cycle_analyses.items()}
    plot_development_typology(metrics, 'figures/development_typology.png')
    print("✅ Development cycles analyzed and plotted")

    # Step 6: Generate all tables
    print("\n📊 Step 6: Generating result tables...")
    generate_all_tables(df, all_results, cycle_analyses)
    print("✅ All tables generated and saved")

    print("\n✨ Analysis completed successfully!")

if __name__ == "__main__":
    main()
