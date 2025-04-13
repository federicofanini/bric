import pandas as pd
import numpy as np
import os
from src.s01_load_data import load_bric_data
from src.s02_clean_data import clean_bric_data
from src.utils import create_lags
from src.s05_ols_diagnostics import run_diagnostics
from src.s03_visualize import (
    create_descriptive_plots,
    generate_descriptive_table,
    plot_diagnostics,
    plot_development_typology
)
from src.s06_classify_cycles import analyze_cycle_dynamics, generate_cycle_analysis_markdown
from src.s04_ols import run_regression_analysis

# Create output directories if they don't exist
os.makedirs('outputs', exist_ok=True)
os.makedirs('figures', exist_ok=True)
os.makedirs('figures/diagnostics', exist_ok=True)
os.makedirs('results', exist_ok=True)
os.makedirs('figures/descriptive', exist_ok=True)

def main():
    # Step 1: Load and clean data
    df = load_bric_data()
    df = clean_bric_data(df)
    
    # Step 2: Perform descriptive analysis
    print("\n📊 Performing descriptive analysis...")
    create_descriptive_plots(df)
    
    # Genera e salva la tabella delle statistiche descrittive
    descriptive_table = generate_descriptive_table(df)
    with open('figures/descriptive/descriptive_stats.md', 'w') as f:
        f.write(descriptive_table)
    
    # Step 3: Create lagged variables
    df = create_lags(df)
    
    # Step 4: Run regression analysis
    countries = ['Brazil', 'Russia', 'India', 'China']
    chains = ['A', 'B']
    
    all_results = run_regression_analysis(df, countries, chains)

    # Step 5: Analyze development cycles
    print("\n🔄 Analyzing development cycles...")
    cycle_analyses = analyze_cycle_dynamics(df)
    
    # Generate and save cycle analysis
    cycle_analysis_md = generate_cycle_analysis_markdown(cycle_analyses)
    with open('results/cycle_analysis.md', 'w') as f:
        f.write(cycle_analysis_md)
    print("✅ Cycle analysis completed and saved to results/cycle_analysis.md")
    
    # Generate and save development typology plot
    plot_development_typology(cycle_analyses, 'figures/development_typology.png')
    print("✅ Development typology plot saved to figures/development_typology.png")

if __name__ == "__main__":
    main()
