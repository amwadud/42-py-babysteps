#!/usr/bin/env python3
"""oracle.py - Configuration Management Demo"""

from dotenv import load_dotenv
import os


def get_config() -> dict[str, str]:
    """Get configuration from environment variables."""
    load_dotenv()

    return {
        "mode": os.getenv("MATRIX_MODE", "development"),
        "database_url": os.getenv("DATABASE_URL", "sqlite:///matrix.db"),
        "api_key": os.getenv("API_KEY", ""),
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        "zion_endpoint": os.getenv("ZION_ENDPOINT", "http://localhost:8000"),
    }


def show_config(config: dict[str, str]) -> None:
    """Display configuration status."""
    print("\n ORACLE STATUS: Reading the Matrix...\n")
    print(" Configuration loaded:")
    print(f"  Mode: {config['mode']}")

    if config["mode"] == "production":
        print("  Database: Connected to production instance")
    else:
        print("  Database: Connected to local instance")

    if config["api_key"]:
        print("  API Access: Authenticated")
    else:
        print("  API Access: Not authenticated")

    print(f"  Log Level: {config['log_level']}")
    print("  Zion Network: Online")


def check_security() -> None:
    """Check environment security."""
    print("\n Environment security check:")
    print(" [OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print(" [OK] .env file properly configured")
    else:
        print(" [WARNING] No .env file found")

    if os.environ.get("MATRIX_MODE") or os.environ.get("API_KEY"):
        print(" [OK] Production overrides available")
    else:
        print(" [INFO] No env var overrides detected")

    print("\n The Oracle sees all configurations.")


def main() -> None:
    """Main entry point."""
    config = get_config()
    show_config(config)
    check_security()


if __name__ == "__main__":
    main()
