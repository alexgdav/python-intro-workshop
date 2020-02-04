"""Translates code originally written in JavaScript"""

def check_for_as(str_input):
    """checks if a string contains 'A'"""
    if str_input[0] == "A":
      return f"The string '{str_input}' starts with 'A'!"
    for i, letter in enumerate(str_input):
      if letter == "A":
        return f"We found an 'A' in '{str_input}' at character {i + 1}"
      else:
        return f"There's not a single 'A' in the string '{str_input}'"


print (check_for_as(f"Someone should move to the Andes"))
print (check_for_as(f"After work we should finally sleep"))
print (check_for_as(f"There be no beginning of the letter list here"))
