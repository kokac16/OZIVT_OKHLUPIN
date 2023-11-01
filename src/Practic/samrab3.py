def count_most_common_numbers(s):
    digit_count = {}
    for digit in s:
        if digit.isdigit():
            digit = int(digit)
            if digit in digit_count:
                digit_count[digit] += 1
            else:
                digit_count[digit] = 1

    most_common = sorted(digit_count, key=digit_count.get, reverse=True)[:3]
    result = {digit: digit_count[digit] for digit in most_common}

    return result

input_string = "1234455667788990"
result_dict = count_most_common_numbers(input_string)
for key in sorted(result_dict.keys()):
    print(f"{key}: {result_dict[key]}")
