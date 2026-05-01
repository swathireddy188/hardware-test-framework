import matplotlib.pyplot as plt
import pandas as pd

def generate_report(csv_file="test_results.csv"):
    df = pd.read_csv(csv_file)

    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot each rail as a separate line
    for rail in df["rail_name"].unique():
        subset = df[df["rail_name"] == rail]
        nominal = subset["nominal"].iloc[0]
        ax.plot(subset["voltage"].values, label=rail, marker="o")

        # Draw tolerance band (green zone = pass region)
        ax.axhline(nominal * 1.05, color="green", linestyle="--",
                   alpha=0.4, label=f"Upper limit ({rail})")
        ax.axhline(nominal * 0.95, color="red",   linestyle="--",
                   alpha=0.4, label=f"Lower limit ({rail})")

    ax.set_title("Voltage Rail Test Report", fontsize=14)
    ax.set_xlabel("Reading number")
    ax.set_ylabel("Voltage (V)")
    ax.legend(loc="upper right", fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("test_report.png", dpi=150)
    print("Report saved: test_report.png")
    plt.show()

if __name__ == "__main__":
    generate_report()
