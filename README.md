# BRIC Countries OLS Analysis

This repository contains an Ordinary Least Squares (OLS) analysis of the relationship between economic growth and human development in BRIC countries (Brazil, Russia, India, and China) from 2000 to 2019.

## Overview

The project analyzes two causal chains:

1. Chain A: Economic Growth → Human Development
2. Chain B: Human Development → Economic Growth

The analysis includes:

- Data preprocessing and feature engineering
- OLS regression modeling
- Visualization of key trends and relationships
- Statistical analysis of the causal relationships

## Project Structure

```
.
├── data/               # Data files
├── src/                # Source code
│   ├── load_data.py    # Data loading functions
│   ├── utils.py        # Utility functions
│   ├── regression.py   # OLS regression models
│   ├── clean_data.py   # Data cleaning script
│   ├── ols_analysis.py # OLS analysis script
│   └── visualize.py    # Visualization functions
├── figures/            # Generated plots and analysis results
├── main.py             # Main execution script
└── requirements.txt    # Python dependencies
```

## Dependencies

The project requires the following Python packages:

- pandas: For data manipulation and analysis
- seaborn: For statistical data visualization
- matplotlib: For creating static, animated, and interactive visualizations
- statsmodels: For statistical models and tests

## Installation

1. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Run the Data Cleaning Script

Navigate to the `src` directory and run the data cleaning script:

```bash
python src/clean_data.py
```

### Run the OLS Analysis

Execute the OLS analysis script:

```bash
python src/ols_analysis.py
```

### Run the Main Analysis

Finally, run the main script to perform the full analysis and generate visualizations:

```bash
python main.py
```

This will:

1. Load and preprocess the BRIC countries data
2. Run the OLS regression analysis for both causal chains
3. Generate visualizations in the `figures` directory

## Analysis Components

### Data Processing

- Loading BRIC countries data
- Creating lagged variables
- Adding country dummy variables

### Regression Analysis

- Chain A: Economic Growth → Human Development
- Chain B: Human Development → Economic Growth

### Visualizations

- Time series plots of GDP growth and HDI
- Scatter plots of key relationships
- Correlation heatmaps
- Quadrant analysis plots

## Output

The analysis generates:

1. Regression model summaries in the console
2. Visualizations saved in the `figures` directory:
   - GDP growth trends
   - HDI trends
   - Scatter plots
   - Heatmaps
   - Quadrant analysis

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is open source and available under the MIT License.
