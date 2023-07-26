def best_score(a_dictionary):
    """
  A function thatReturns the key with the biggest integer value.

  Arguments:
    a_dictionary: The dictionary to search.

  Returns:
    The key with the biggest integer value, or None if no scores found.
  """
    best_score = None
    best_key = None

    for key, value in  a_dictionary:
        if best_score is None or value > best_score:
            best_score = value
            best_key = key
    return best_key