def common_elements(*sets):
  """Returns a set of common elements in two or more sets."""
  common_elements = set()
  for set_ in sets:
    for element in set_:
      if element in common_elements:
        continue
      if element in set_:
        common_elements.add(element)
  return common_elements

