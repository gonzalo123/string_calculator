def add(string):
    separator, value = split_string(string)
    for valid_separator in ("\n", separator):
        value = value.replace(valid_separator, ",")

    items = [int(string or 0) for string in value.split(",")]
    return sum(map(lambda item: item if item<1000 else 0, items))


def split_string(string):
    parts = string.split("\n")
    if has_custom_separator(parts):
        return parse_custom_separator(parts[0]), parts[1]
    else:
        return ",", string


def parse_custom_separator(separator):
    return separator[2:]


def has_custom_separator(parts):
    return len(parts) > 1 and parts[0][0:2] == '//'
