"""EX06 - Dictionary."""
__author__ = "730570748"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary by swapping keys and values."""
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError(f"Duplicate value '{value}' found in the input dictionary. Inverting the dictionary is not possible.")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """Finds the most popular color in a dictionary of names and favorite colors."""
    color_counter = {}
    the_favorite_color = ""
    current_popular = 0
    for name, color in names_and_colors.items():
        if color in color_counter:
            color_counter[color] += 1
        else:
            color_counter[color] = 1
    for color, counter in color_counter.items():
        if counter > current_popular:
            current_popular = counter
            the_favorite_color = color
    return the_favorite_color


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the frequency of items in a list and returns a dictionary with item counts."""
    result_dict = {}
    for item in input_list:
        item_lower = item.lower()
        if item_lower in result_dict:
            result_dict[item_lower] += 1
        else:
            result_dict[item_lower] = 1
    return result_dict


def alphabetizer(word_list) -> dict[str, list[str]]:
    """Categorizes words into lists by their initial letter, case-insensitive."""
    alphabet_dict = {}
    for word in word_list:
        first_letter = word[0].lower()
        if first_letter in alphabet_dict:
            alphabet_dict[first_letter].append(word)
        else:
            alphabet_dict[first_letter] = [word]
    return alphabet_dict


def update_attendance(attendance_dict, day_of_week, student) -> dict[str, list[str]]:
    """Updates and returns a dictionary of attendance information."""
    if day_of_week in attendance_dict:
        attendance_dict[day_of_week].append(student)
    else: 
        attendance_dict[day_of_week] = [student]
    return attendance_dict