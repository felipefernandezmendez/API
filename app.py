"""Simple helper for loading client-specific environment variables."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Dict

ENV_DIR = Path(__file__).parent / ".env.d"


def load_env(client: str) -> Dict[str, str]:
    """Load environment variables for a client from `.env.d`.

    Parameters
    ----------
    client:
        Name of the client. It should match the file name in `.env.d` without
        the `.env` suffix.

    Returns
    -------
    dict
        A dictionary containing the parsed environment variables. Each key is
        also exported to ``os.environ``.
    """

    env_path = ENV_DIR / f"{client}.env"
    if not env_path.exists():
        raise FileNotFoundError(f"No environment file found for client '{client}'")

    loaded: Dict[str, str] = {}
    with env_path.open("r", encoding="utf-8") as env_file:
        for raw_line in env_file:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                raise ValueError(
                    f"Invalid environment line in {env_path.name!r}: {raw_line.rstrip()}"
                )

            key, value = (part.strip() for part in line.split("=", 1))
            os.environ[key] = value
            loaded[key] = value

    return loaded


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "client",
        help="Client identifier (file name in .env.d without the .env extension)",
    )
    args = parser.parse_args()

    variables = load_env(args.client)

    if variables:
        print(f"Loaded {len(variables)} variables for {args.client}:")
        for key, value in variables.items():
            print(f"  {key}={value}")
    else:
        print(f"No variables defined for {args.client}.")


if __name__ == "__main__":
    main()
