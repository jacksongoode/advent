import math, time

start = time.time()
trees = open('day_3/input.txt', 'r') 
lines = trees.read().splitlines()

questions = [(1,1), (3,1), (5,1), (7,1), (1,2)]
answers = [0] * 5

def tree_looker(right, down):
    place, tree_count = 0, 0
  
    for index in range(down, len(lines), down):
        place = (place + right) % 31
        if index < len(lines):
            if lines[index][place] == '#':
                tree_count += 1
        
    return tree_count

for index, (right, down) in enumerate(questions):
    answers[index] = tree_looker(right, down)

finish = time.time()

print(math.prod(answers))
print(f'Done in {(finish - start):.3f}s')