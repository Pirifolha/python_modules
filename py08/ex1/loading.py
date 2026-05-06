#!/usr/bin/env python3

import importlib
import importlib.util
import sys

required: list = ["pandas", "numpy", "matplotlib"]


def check_dependencies() -> None:
    print("Checking dependencies:")

    missing: list = []
    for lib in required:
        if importlib.util.find_spec(lib) is None:
            missing.append(lib)

    if missing:
        print("Missing dependencies:", ", ".join(missing))
        print("Install with:")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install")
        sys.exit(1)
    else:
        import pandas
        import numpy
        import matplotlib

        print(f"[OK] pandas {pandas.__version__} - Data manipulation ready")
        print(f"[OK] numpy {numpy.__version__} - Numerical computation ready")
        print(
            f"[OK] matplotlib {matplotlib.__version__} - Visualization ready\n"
        )


def analyse_data() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analysing Matrix data...")
    print("Processing 100 data points...")
    n1 = np.linspace(0, 10, 100)
    n2 = np.sin(n1) + np.random.normal(0, 0.2, size=100)

    data = {"num1": n1, "num2": n2}

    df = pd.DataFrame(data)
    df.describe()
    plt.plot(n1, n2)
    print("Generating visualization...\n")
    plt.savefig("analysis.png")
    print("Analysis complete!")
    print("Results saved to: analysis.png")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    check_dependencies()
    analyse_data()


main()
