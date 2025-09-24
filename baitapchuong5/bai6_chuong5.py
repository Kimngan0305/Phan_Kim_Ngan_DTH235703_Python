def NegativeNumberInStrings(s):
    numbers = []
    i = 0
    while i < len(s):
        if s[i] == '-' and i + 1 < len(s) and s[i+1].isdigit():
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            numbers.append(int(s[i:j]))  # ép thành số nguyên âm
            i = j  # nhảy tới sau số
        else:
            i += 1
    return numbers

# Test
chuoi = "abc-5xyz-12k9l--p"
print(NegativeNumberInStrings(chuoi))  # [ -5, -12 ]
