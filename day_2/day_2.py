import os, time

start = time.time()
pass_file = open('day_2/passwords.txt', 'r') 
lines = pass_file.readlines() 
valids_1, valids_2 = 0, 0

for line in lines: 
    range = line.split(" ", 1)[0]
    min, max = int(range.split("-")[0]), int(range.split("-")[1])
    left, right = min - 1, max - 1
    letter = line.split(" ")[1][0]
    password = line.split(" ")[2].strip()

    # Part 1
    if min <= password.count(letter) <= max:
        valids_1 += 1

    # Part 2
    try:
        if (password[left] == letter) ^ (password[right] == letter):
            valids_2 += 1
    except IndexError:
        if len(password) >= left:
            if password[left] == letter:
                valids_2 += 1
        elif len(password) >= right:
            if password[right] == letter:
                valids_2 += 1
        else: pass

finish = time.time()

print(f'Part 1: {valids_1}')
print(f'Part 2: {valids_2}')
print(f'Done in {(finish - start):.3f}s')

