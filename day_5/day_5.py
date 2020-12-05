import time
start = time.time()

seats = open('day_5/input.txt', 'r') 
seats = seats.read().splitlines()

seats = [seat.replace('F','0').replace('B','1') \
            .replace('L','0').replace('R','1') \
            for seat in seats]

seat_nums = [int(seat[:7], 2) * 8 \
            + int(seat[7:], 2) \
            for seat in seats]

# Part 1
max_id = max(seat_nums)

# Part 2
empty_seats = list(set(range(0, 1024)) - set(seat_nums))

for index, seat in enumerate(empty_seats[1:-1], 1):
    if abs(empty_seats[index+1] - seat) != 1 and abs(seat - empty_seats[index-1]) != 1:
        my_seat = seat

print(f'Max seat ID: {max_id}')
print(f'My seat: {my_seat}')

finish = time.time()
print(f'Done in {(finish - start):.3f}s')