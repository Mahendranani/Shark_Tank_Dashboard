# # scripts/data_cleaning.py

import pandas as pd


def clean_data(
    input_path: str = "data/shark_tank_raw.csv",
    output_path: str = "data/shark_tank_clean.csv"
):
    """
    Cleans the raw Shark Tank dataset:
      1. Standardize column names to snake_case lowercase.
      2. Convert investment columns to numeric, cleaning commas/₹/spaces.
      3. Normalize string columns.
      4. Derive `deal_closed` and `investment_amount` columns.
      5. Save cleaned DataFrame to CSV.
    """
    # Load raw dataset
    df = pd.read_csv(input_path)

    # 1. Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^\w_]", "", regex=True)
    )

    # 2. Clean and convert numeric-like investment columns
    invest_cols = [c for c in df.columns if "amount" in c or "investment" in c]
    numeric_candidates = set(invest_cols) | {
        "original_ask_amount",
        "total_deal_amount"
    }

    for col in numeric_candidates:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(",", "", regex=False)   # remove commas
                .str.replace("₹", "", regex=False)   # remove rupee symbol
                .str.replace(" ", "", regex=False)   # remove spaces
            )
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # 3. Clean string columns
    for col in df.select_dtypes(include="object"):
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.title()
        )

    # 4. Derive `deal_closed` column
    if "accepted_offer" in df.columns:
        df["deal_closed"] = df["accepted_offer"].astype(str).str.lower() == "yes"
    else:
        df["deal_closed"] = False

    # 5. Derive `investment_amount` column
    if "total_deal_amount" in df.columns and df["total_deal_amount"].sum() > 0:
        df["investment_amount"] = df["total_deal_amount"]
    else:
        df["investment_amount"] = df.get("original_ask_amount", 0.0)

    # 6. Save cleaned dataset
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to {output_path}")


if __name__ == "__main__":
    clean_data()
