import time, itertools, math

def day_1(r, numbers):
    start = time.time()

    numbers = sorted(numbers)
    for i in itertools.combinations(numbers, r):
        if sum(i) == 2020:
            print(f'Combination: {i}\nProduct: {math.prod(i)}')

            finish = time.time()
            print(f'Done in {(finish - start):.3f}s')
            return

if __name__ == '__main__':
    text = open('day_1/input.txt', 'r')
    numbers = [int(line.strip()) for line in text]
    day_1(2, numbers)
    day_1(3, numbers)