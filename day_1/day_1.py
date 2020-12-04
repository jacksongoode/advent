import time, itertools, math
start = time.time()

def day_1(r, numbers):

    numbers = sorted(numbers)
    for i in itertools.combinations(numbers, r):
        if sum(i) == 2020:
            print(f'Combination: {i}\nProduct: {math.prod(i)}')
            return

if __name__ == '__main__':
    expenses = open('day_1/input.txt', 'r')
    numbers = [int(line.strip()) for line in expenses]
    
    day_1(2, numbers)
    day_1(3, numbers)

    finish = time.time()
    print(f'Done in {(finish - start):.3f}s')