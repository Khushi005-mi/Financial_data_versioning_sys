def change_classifier(change):
    """
    Classify the type of change based on the change description.

    Args:
        change (str): The description of the change.

    Returns:
        str: The type of change (e.g., 'addition', 'deletion', 'modification').
    """
    if "added" in change.lower():
        return "addition"
    if "removed" in change.lower() or "deleted" in change.lower():
        return "deletion"
    if "modified" in change.lower() or "changed" in change.lower():
        return "modification"
    elif :
    return ("Unknown change detected")

            