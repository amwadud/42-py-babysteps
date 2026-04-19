#!/usr/bin/env python3
"""
construct.py - Virtual Environment Detection

Detects whether running inside a virtual environment.
"""

import sys
import site


def main() -> None:
    """Main function - shows venv status."""
    if sys.prefix != sys.base_prefix:
        print(" MATRIX STATUS: Welcome to the construct\n")
        print(f" Current Python: {sys.executable}")
        print(f" Virtual Environment: {sys.prefix.split('/')[-1]}")
        print(f" Environment Path: {sys.prefix}\n")
        print(" SUCCESS: You're in an isolated environment!")
        print(" Safe to install packages without affecting")
        print(" the global system.\n")
        print(" Package installation path:")
        print(f" {site.getsitepackages()[0]}")
    else:
        print(" MATRIX STATUS: You're still plugged in\n")
        print(f" Current Python: {sys.executable}")
        print(" Virtual Environment: None detected\n")
        print(" WARNING: You're in the global environment!")
        print(" The machines can see everything you install.\n")
        print(" To enter the construct, run:")
        print(" python -m venv matrix_env")
        print(" source matrix_env/bin/activate # On Unix")
        print(" matrix_env\\Scripts\\activate    # On Windows")
        print("\n Then run this program again.")


if __name__ == "__main__":
    main()
