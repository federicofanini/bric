# BRIC Countries OLS Analysis

This repository contains an Ordinary Least Squares (OLS) analysis of the relationship between economic growth and human development in BRIC countries (Brazil, Russia, India, and China) from 2000 to 2019.

## Overview

The project analyzes two causal chains:

1. Chain A: Economic Growth → Human Development

   - Variables: GDP growth, HDI, education expenditure, health expenditure
   - Lagged variables: 5-year lags for GDP growth and HDI

2. Chain B: Human Development → Economic Growth
   - Variables: GDP growth, HDI, gross capital formation (gcf)
   - Lagged variables: 5-year lags for GDP growth and HDI

## Project Structure

```
.
├── data/                    # Data files
│   ├── raw/                 # Raw data files
│   └── processed/           # Processed data files
├── src/                     # Source code
│   ├── load_data.py         # Loads and combines BRIC data from Excel
│   ├── clean_data.py        # Cleans and preprocesses data
│   ├── utils.py             # Utility functions (lag creation)
│   └── visualize.py         # Visualization functions
├── main.py                  # Main execution script
└── requirements.txt         # Python dependencies
```

## Dependencies

The project requires the following Python packages:

- pandas: For data manipulation and analysis
- openpyxl: For Excel file handling
- statsmodels: For statistical models and tests
- matplotlib: For creating visualizations

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
python main.py
```

This will:

1. Load BRIC data from Excel files
2. Clean and preprocess the data
3. Create lagged variables
4. Run OLS regression analysis
5. Generate visualizations

## Data Processing

### Loading Data

- Loads data from Excel files for each BRIC country
- Combines data for both chains (A and B)
- Standardizes column names and formats

### Cleaning Data

- Removes missing values
- Handles outliers
- Separates data by chain type
- Removes unused variables (e.g., gcf from Chain A)

### Feature Engineering

- Creates 5-year lagged variables for GDP growth and HDI
- Handles missing values in lagged variables

## Output

The analysis generates:

1. Processed data in Excel format:

   - `data/processed/bric_regression_data.xlsx`
   - Separate sheets for each chain and country

2. Regression results in the console:
   - Model summaries
   - Statistical significance
   - R-squared values

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is open source and available under the MIT License.
