# BRIC Countries OLS Analysis

This repository contains an Ordinary Least Squares (OLS) analysis of the relationship between economic growth and human development in BRIC countries (Brazil, Russia, India, and China) from 2000 to 2019.

## Overview

The project analyzes two causal chains:

1. Chain A: Economic Growth → Human Development

   - Variables: GDP growth, HDI, education expenditure, health expenditure
   - Lagged variables: 5-year lags for GDP growth and HDI
2. Chain B: Human Development → Economic Growth

   - Variables: GDP growth, HDI, gross capital formation (gcf)
   - Lagged variables: 5-year las for GDP growth and HDI

## Project Structure

```
.
├── data/                    # Data files
│   ├── raw/                 # Raw data files
│   └── processed/           # Processed data files
├── src/                     # Source code
│   ├── s00_main.py          # Main execution script
│   ├── s01_load_data.py     # Loads and combines BRIC data from Excel
│   ├── s02_clean_data.py    # Cleans and preprocesses data
│   ├── s03_visualize.py     # Visualization functions
│   ├── s04_ols.py           # OLS regression analysis
│   ├── s05_ols_diagnostics.py # OLS model diagnostics
│   ├── s06_classify_cycles.py # Development cycle classification
│   └── utils.py             # Utility functions (lag creation)
├── figures/                 # Generated figures
│   ├── descriptive/         # Descriptive analysis plots
│   └── diagnostics/         # OLS diagnostics plots
├── outputs/                 # Analysis outputs
│   └── regression_r2_summary.csv
├── results/                 # Analysis results
│   └── cycle_analysis.md
└── requirements.txt         # Python dependencies
```

## Dependencies

The project requires the following Python packages:

- pandas: For data manipulation and analysis
- openpyxl: For Excel file handling
- statsmodels: For statistical models and tests
- matplotlib: For creating visualizations
- seaborn: For enhanced visualizations
- scipy: For statistical functions

## Installation

1. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the main script to perform the full analysis:

```bash
python src/s00_main.py
```

This will execute the following steps in sequence:

1. Load BRIC data from Excel files (s01_load_data.py)
2. Clean and preprocess the data (s02_clean_data.py)
3. Perform descriptive analysis and generate visualizations (s03_visualize.py)
4. Create lagged variables (utils.py)
5. Run OLS regression analysis (s04_ols.py)
6. Generate OLS diagnostics (s05_ols_diagnostics.py)
7. Classify development cycles (s06_classify_cycles.py)

## Data Processing

### Loading Data (s01_load_data.py)

- Loads data from Excel files for each BRIC country
- Combines data for both chains (A and B)
- Standardizes column names and formats

### Cleaning Data (s02_clean_data.py)

- Removes missing values
- Handles outliers
- Separates data by chain type
- Removes unused variables (e.g., gcf from Chain A)

### Visualization (s03_visualize.py)

- Generates descriptive statistics
- Creates time series plots
- Produces correlation heatmaps
- Generates distribution plots

### OLS Analysis (s04_ols.py)

- Performs OLS regression for both chains
- Handles lagged and non-lagged variables
- Generates regression outputs and plots

### Diagnostics (s05_ols_diagnostics.py)

- Performs VIF analysis
- Generates QQ plots
- Creates residuals vs fitted plots
- Calculates Cook's distance

### Cycle Classification (s06_classify_cycles.py)

- Analyzes development cycles
- Classifies countries into development typologies
- Generates development cycle plots

## Output

The analysis generates:

1. Processed data in Excel format:

   - `data/processed/bric_regression_data.xlsx`
   - Separate sheets for each chain and country
2. Visualizations in the figures directory:

   - Descriptive analysis plots
   - OLS diagnostic plots
   - Development cycle plots
3. Analysis results:

   - Regression summaries in outputs/
   - Cycle analysis in results/
   - R² summary in outputs/

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is open source and available under the MIT License.
