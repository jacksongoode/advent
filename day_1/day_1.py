import time, itertools, math

def day_1(r, stuff):
    start = time.time()

    stuff = sorted(stuff)
    for i in itertools.combinations(stuff, r):
        if sum(i) == 2020:
            print(f'Combination: {i}\nProduct: {math.prod(i)}')

            finish = time.time()
            print(f'Done in {(finish - start):.3f}s')
            return

if __name__ == '__main__':
    input = open('day_1/input.txt', 'r')
    stuff = [line.striplines() for line in input]
    day_1(2, stuff)
    day_1(3, stuff)