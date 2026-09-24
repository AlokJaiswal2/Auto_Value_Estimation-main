"""
Evaluate trained model on the full dataset and plot MAE, MSE, RMSE, R².
Run from project root: python3 plot_model_metrics.py
"""

import json
from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, root_mean_squared_error

from car_price_model_advanced import DEFAULT_FEATURES, TARGET

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "model_advanced.joblib"
DATA_PATH = ROOT / "car_dataset_india_cleaned.csv"
METRICS_JSON = ROOT / "model_advanced_metrics.json"
PLOT_PATH = ROOT / "model_metrics_plot.png"


def main():
    if not MODEL_PATH.exists():
        raise SystemExit(f"Missing {MODEL_PATH}. Train first: python car_price_model_advanced.py train ...")

    df = pd.read_csv(DATA_PATH)
    if "Battery_Charge_Level" not in df.columns:
        df["Battery_Charge_Level"] = np.nan
    df["Battery_Charge_Level"] = df["Battery_Charge_Level"].fillna(0)

    X = df[DEFAULT_FEATURES].copy()
    y = df[TARGET].copy()

    pipe = joblib.load(MODEL_PATH)
    preds = pipe.predict(X)

    mae = float(mean_absolute_error(y, preds))
    mse = float(mean_squared_error(y, preds))
    rmse = float(root_mean_squared_error(y, preds))
    r2 = float(r2_score(y, preds))

    print("Model evaluation (full training set — same as training script fit):")
    print(f"  MAE  = ₹ {mae:,.2f}")
    print(f"  MSE  = {mse:,.2f}  (₹²)")
    print(f"  RMSE = ₹ {rmse:,.2f}")
    print(f"  R²   = {r2:.6f}")

    out_metrics = {"MAE": mae, "MSE": mse, "RMSE": rmse, "R2": r2}
    with open(METRICS_JSON, "w") as f:
        json.dump(out_metrics, f, indent=2)
    print(f"\nUpdated {METRICS_JSON}")

    # --- Figure: error metrics (₹) + MSE scaled + R² ---
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.2))
    fig.suptitle("Car price model — regression metrics", fontsize=14, fontweight="bold")

    # MAE & RMSE in lakhs (100k) for readable bar heights
    ax0 = axes[0]
    labels_err = ["MAE", "RMSE"]
    values_lakh = [mae / 1e5, rmse / 1e5]
    colors_err = ["#2563eb", "#7c3aed"]
    bars = ax0.bar(labels_err, values_lakh, color=colors_err, edgecolor="black", linewidth=0.8)
    ax0.set_ylabel("Error (lakhs of ₹)")
    ax0.set_title("Mean absolute & root mean\nsquared error")
    for b, v in zip(bars, [mae, rmse]):
        ax0.text(
            b.get_x() + b.get_width() / 2,
            b.get_height() + 0.02 * max(values_lakh + [0.1]),
            f"₹ {v:,.0f}",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    # MSE is huge in ₹² — show in billions of ₹²
    ax1 = axes[1]
    mse_bn = mse / 1e9
    ax1.bar(["MSE"], [mse_bn], color="#dc2626", edgecolor="black", linewidth=0.8)
    ax1.set_ylabel("MSE (billions of ₹²)")
    ax1.set_title("Mean squared error")
    ax1.text(
        0,
        mse_bn + 0.02 * max(mse_bn, 0.1),
        f"{mse:,.0f}\n₹²",
        ha="center",
        va="bottom",
        fontsize=9,
    )

    ax2 = axes[2]
    ax2.barh(["R² score"], [r2], color="#059669", height=0.35, edgecolor="black", linewidth=0.8)
    ax2.set_xlim(0, 1.05)
    ax2.set_xlabel("R² (0–1)")
    ax2.set_title("Coefficient of determination")
    ax2.text(min(r2 + 0.02, 0.98), 0, f"{r2:.4f}", va="center", fontsize=11, fontweight="bold")

    plt.tight_layout()
    plt.savefig(PLOT_PATH, dpi=150, bbox_inches="tight")
    print(f"Saved plot: {PLOT_PATH}")
    plt.close()


if __name__ == "__main__":
    main()
