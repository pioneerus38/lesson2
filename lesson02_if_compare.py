def compare_strings(first_str, second_str):
    if (type(first_str) != str) or (type(second_str) != str):
        return 0
    elif first_str == second_str:
        return 1
    elif len(first_str) > len(second_str):
        return 2
    elif second_str == "learn":
        return 3
    return None # Explicit is better than implicit 

print(compare_strings(True, "learn"))
print(compare_strings("learn", "learn"))
print(compare_strings("python", "learn"))
print(compare_strings("123", "learn"))
print(compare_strings("learn", "python"))