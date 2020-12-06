import time
start = time.time()

customs = open('day_6/code6.txt', 'r')
customs = customs.read().split('\n\n')
any_yes = 0
all_yes = 0

# Part 1
any_customs = [custom.replace('\n', '') for custom in customs]
for any_custom in any_customs:
    set_custom = ''.join(set(any_custom)) 
    any_yes += len(set_custom)

# Part 2
all_customs = [custom.split('\n') for custom in customs]
for all_custom in all_customs:
    set_custom = [set(x) for x in all_custom]
    intrsct_customs = set.intersection(*set_custom)
    all_yes += len(intrsct_customs)

print(f'Answers by anyone: {any_yes}')
print(f'Same answers by everyone: {all_yes}')

finish = time.time()
print(f'Done in {(finish - start):.3f}s')