import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor, OLSInfluence
import os

# Output directory
os.makedirs('figures/diagnostics', exist_ok=True)

def run_diagnostics(model, model_name="model"):
    print(f"\n🔬 Diagnostics for: {model_name}")

    # === 1. VIF ===
    print("\n📏 VIF (Variance Inflation Factor):")
    X = pd.DataFrame(model.model.exog, columns=model.model.exog_names)
    vif_data = pd.DataFrame()
    vif_data["Variable"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    print(vif_data)

    # === 2. QQ Plot ===
    fig = sm.qqplot(model.resid, line='45', fit=True)
    plt.title(f"QQ Plot - {model_name}")
    plt.tight_layout()
    plt.savefig(f'figures/diagnostics/{model_name}_qqplot.png')
    plt.close()

    # === 3. Residuals vs Fitted ===
    y_fitted = model.fittedvalues
    residuals = model.resid

    plt.figure(figsize=(8, 5))
    plt.scatter(y_fitted, residuals, alpha=0.7)
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel('Fitted values')
    plt.ylabel('Residuals')
    plt.title(f"Residuals vs Fitted - {model_name}")
    plt.tight_layout()
    plt.savefig(f'figures/diagnostics/{model_name}_residuals_vs_fitted.png')
    plt.close()

    # === 4. Cook’s Distance ===
    influence = OLSInfluence(model)
    cooks_d = influence.cooks_distance[0]

    plt.figure(figsize=(8, 4))
    plt.stem(np.arange(len(cooks_d)), cooks_d, markerfmt=",", basefmt=" ")
    plt.axhline(4 / len(cooks_d), color='red', linestyle='--', label='Threshold')
    plt.title(f"Cook’s Distance - {model_name}")
    plt.xlabel("Observation index")
    plt.ylabel("Cook’s D")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'figures/diagnostics/{model_name}_cooks_distance.png')
    plt.close()

    # === 5. Summary
    print(f"\n📊 Durbin-Watson: {sm.stats.stattools.durbin_watson(residuals):.3f}")
    print(f"📦 Saved diagnostics plots to 'figures/diagnostics/{model_name}_*.png'")
