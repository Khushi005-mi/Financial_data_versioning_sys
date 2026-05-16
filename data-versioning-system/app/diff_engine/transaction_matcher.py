def transaction_matcher(transaction_a, transaction_b):
    """
    Compares two transactions and returns a similarity score between 0 and 1.
    The score is based on the similarity of the transaction attributes such as
    amount, date, description, and category.

    Args:
        transaction_a (dict): The first transaction to compare.
        transaction_b (dict): The second transaction to compare.

    Returns:
        float: A similarity score between 0 and 1, where 1 means identical transactions.
    """
    score = 0.0
    total_attributes = 4  # amount, date, description, category

    # Compare amount
    if transaction_a["amount"] == transaction_b["amount"]:
        score += 1.0

    # Compare date
    if transaction_a["date"] == transaction_b["date"]:
        score += 1.0
    # Compare description
    if transaction_a["description"] == transaction_b["description"]:
        score += 1.0

    # Compare category
    if transaction_a["category"] == transaction_b["category"]:
        score += 1.0