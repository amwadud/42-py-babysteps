#!/usr/bin/env python3
"""
loading.py - Package Management Demo

Demonstrates pip vs Poetry package management.
"""

import importlib


def check_deps() -> dict[str, str | None]:
    packages = ["pandas", "numpy", "matplotlib", "requests"]
    deps: dict[str, str | None] = {}

    for pkg in packages:
        try:
            module = importlib.import_module(pkg)
            deps[pkg] = getattr(module, "__version__")
        except ImportError:
            deps[pkg] = None

    return deps


def show_deps_stat(deps: dict[str, str | None]) -> None:
    print("\n LOADING STATUS: Loading programs...\n")
    print(" Checking dependencies:")

    descriptions = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
        "requests": "Network access ready",
    }

    for pkg, version in deps.items():
        status = "OK" if version else "MISSING"
        if version:
            print(f" [{status}] {pkg} ({version}) - {descriptions[pkg]}")
        else:
            print(f" [{status}] {pkg} - {descriptions[pkg]}")

    print()


def analyze_data() -> None:
    """Analyze data and generate visualization."""
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

    np.random.seed(42)
    data = pd.DataFrame(
        {
            "time": np.linspace(0, 100, 1000),
            "value": np.random.randn(1000).cumsum() + 50,
        }
    )
    _ = plt.figure(figsize=(8, 4))
    _ = plt.plot(data["time"], data["value"], color="green")
    _ = plt.title("Matrix Data Analysis")
    _ = plt.xlabel("Time")
    _ = plt.ylabel("Value")
    plt.grid(True, alpha=0.3)
    plt.savefig("matrix_analysis.png")
    plt.close()
    print(" Analyzing Matrix data...")
    print(" Processing 1000 data points...")
    print(" Generating visualization...")
    print("\n Analysis complete!")
    print(" Results saved to: matrix_analysis.png")


def main() -> None:
    """Main entry point."""
    deps = check_deps()
    show_deps_stat(deps)

    missing = [pkg for pkg, ver in deps.items() if ver is None]

    if missing:
        print(f" Missing required packages: {', '.join(missing)}")
        print(" To install dependencies, use one of these methods:\n")
        print(" With pip:")
        print("   pip install -r requirements.txt")
        print("\n With Poetry:")
        print("   poetry install")
        print("   poetry run python loading.py")
        print()
    else:
        analyze_data()


if __name__ == "__main__":
    main()
