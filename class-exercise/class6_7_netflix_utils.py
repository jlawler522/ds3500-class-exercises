import logging

logger = logging.getLogger(__name__)


def show_overview(df):
    """Display basic information about a DataFrame."""
    logger.debug(f"DataFrame shape: {df.shape}")

    print(f"Shape: {df.shape}")
    print(df.head())
    print(f"Columns: {list(df.columns)}")
    print(f"Data types:\n{df.dtypes}")


def remove_duplicates(df):
    """Remove exact duplicate rows."""
    before = len(df)
    df = df.drop_duplicates()
    logger.debug(f"Duplicate removal: {before} rows before, {len(df)} after")

    return df


def drop_missing_rows(df):
    """Remove rows containing missing values."""
    before = len(df)
    df = df.dropna()
    logger.debug(f"Missing-row removal: {before} rows before, {len(df)} after")

    return df