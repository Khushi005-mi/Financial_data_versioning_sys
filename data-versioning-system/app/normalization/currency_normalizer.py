def crrency_normalization(df):
    """
    Normalizes the currency values in the DataFrame by converting them to a standard format.
    """

    # Define a mapping of currency symbols to their respective
    # currency codes
    currency_mapping = {
        "$": "USD",
        "€": "EUR",
        "£": "GBP",
        "¥": "JPY",
        "₹": "INR",
        "₩": "KRW",
        "₽": "RUB",
        "₺": "TRY",
        "₫": "VND",
    }
    if "currency" in df.columns:
        # Normalize the currency values
        df["currency"] = df["currency"].apply()
        lambda x: currency_mapping.get(x, x)
        return df 
    else:
      raise ValueError("Currency column not found in the DataFrame.")