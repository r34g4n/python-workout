def hex_output(hex_input):
    hex_alphanumerics = {
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15,
    }
    tot_value = 0
    hex_reversed = tuple(reversed(hex_input))
    for i in range(len(hex_reversed)):
        digit_s = hex_reversed[i]
        if digit_s.isnumeric():
            digit = int(digit_s)
        else:
            digit = hex_alphanumerics.get(digit_s, 0)
        val = digit * (16 ** i)
        tot_value += val
    return tot_value


input = input('type hex value to be converted to decimal: ')
print(hex_output(input))
