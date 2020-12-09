import time
from itertools import combinations
start = time.time()

xmas = open('day_9/input.txt', 'r')
xmas_lines = xmas.read().splitlines()
xmas_lines = [int(line) for line in xmas_lines]

def check(index, line):
    check = False
    while check is False:
        for (x, y) in combinations(xmas_lines[index-25:index], 2):
            if x + y == line:
                check = True
                return True
        return False

def weakness(end, invalid):
    check = False
    for index, _ in enumerate(xmas_lines[:end]):
        acc = []
        while index < len(xmas_lines[:end]):
            acc.append(xmas_lines[index])
            if sum(acc) < invalid:
                index += 1
                continue
            elif sum(acc) == invalid:
                check = True
                break
            elif sum(acc) > invalid:
                break
        
        if check is True:
            weakness = min(acc) + max(acc)
            return weakness
        else: continue

    print('Failed to find weakness!')
    return

# Part 1: Check for invalid
for index, line in enumerate(xmas_lines):
    if index < 25:
        continue
    if check(index, line) == True:
        continue
    else:
        print(f'Check failed for {line} at line {index}')
        # Part 2: Check for weakness
        weakness = weakness(index, line)
        print('Weakness:', weakness)
        break

finish = time.time()
print(f'Done in {(finish - start):.3f}s')