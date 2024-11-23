result = []


def divider(a, b):
    if a < b:
        raise ValueError(f"Error: a < b (a={a}, b={b})")
    if b > 100:
        raise IndexError(f"Error: b > 100 (b={b})")
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        if not isinstance(key, (int, float)) or not isinstance(value, (int, float)):
            raise TypeError(f"Error: Invalid key type or value (key={key}, value={value})")

        res = divider(key, value)
        result.append(res)

    except ZeroDivisionError as e:
        print(f"Error: Division by zero for a pair ({key}, {value}). {e}")
    except ValueError as e:
        print(f"ValueError for the pair ({key}, {value}). {e}")
    except IndexError as e:
        print(f"IndexError for pair ({key}, {value}). {e}")
    except TypeError as e:
        print(f"TypeError for the pair({key}, {value}). {e}")
    except Exception as e:
        print(f"Unknown error for pair ({key}, {value}). {e}")

print("Result:", result)
