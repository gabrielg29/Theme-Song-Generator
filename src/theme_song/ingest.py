from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = ["rank", "track", "artist", "scrobbles"]


def load_top10(path: str | Path) -> pd.DataFrame:
    """Load and validate a Top 10 listening-history CSV."""

    df = pd.read_csv(path)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if len(df) != 10:
        raise ValueError(f"Expected 10 tracks, found {len(df)}")

    if df["rank"].duplicated().any():
        raise ValueError("Ranks must be unique")

    if (df["scrobbles"] <= 0).any():
        raise ValueError("Scrobble counts must be positive")

    return df.sort_values("rank").reset_index(drop=True)