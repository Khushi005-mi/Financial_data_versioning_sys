def difference_calculator(old_data, new_data):
    """
    Calculate the difference between old and new data.
    Returns a dictionary with added, removed, and modified entries.
    """
    diff = {
        'added': {},
        'removed': {},
        'modified': {}
    }

    # Check for added and modified entries
    for key, new_data_value in new_data.items():
        if key not in old_data:
            diff["added"][key] = new_data_value
        else:
            old_data_value = old_data[key]
            if new_data_value != old_data_value:
                diff["modified"][key] = {
                    "old": old_data_value,
                    "new": new_data_value
                }


    # Check for removed entries
    for key in old_data:
        if key not in new_data:
            diff["removed"][key] = old_data[key]