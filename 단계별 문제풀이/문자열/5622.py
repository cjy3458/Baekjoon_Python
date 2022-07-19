word = input()
count = 0

for _ in word:
    if _ == 'A' or _ == 'B' or _ == 'C':
        count += 3
    elif _ == 'D' or _ == 'E' or _ == 'F':
        count += 4
    elif _ == 'G' or _ == 'H' or _ == 'I':
        count += 5
    elif _ == 'J' or _ == 'K' or _ == 'L':
        count += 6
    elif _ == 'M' or _ == 'N' or _ == 'O':
        count += 7
    elif _ == 'P' or _ == 'Q' or _ == 'R' or _ == 'S':
        count += 8
    elif _ == 'T' or _ == 'U' or _ == 'V':
        count += 9
    elif _ == 'W' or _ == 'X' or _ == 'Y' or _ == 'Z':
        count += 10

print(count)