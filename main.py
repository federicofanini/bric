from src.load_data import load_bric_data
from src.utils import create_lags
from src.regression import run_chain_a, run_chain_b
from src.visualize import *

def main():
    df = load_bric_data()
    df = create_lags(df)

    # Run overall models
    model_a = run_chain_a(df)
    print("\nCHAIN A: Economic Growth ➝ Human Development")
    print(model_a.summary())

    model_b = run_chain_b(df)
    print("\nCHAIN B: Human Development ➝ Economic Growth")
    print(model_b.summary())

    ensure_output_dir()
    plot_time_series(df, 'gdp_growth', 'GDP Growth (2000–2019)', 'Annual % Growth', 'gdp_growth')
    plot_time_series(df, 'hdi', 'HDI Trends (2000–2019)', 'HDI Score', 'hdi_trends')
    plot_scatter(df)
    plot_heatmap(df)
    plot_quadrant(df)

if __name__ == '__main__':
    main()
