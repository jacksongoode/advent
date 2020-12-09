boot_code = open('day_8/input.txt', 'r')
boot_code = boot_code.read().splitlines()
insts = [inst.split(' ') for inst in boot_code]
insts = [inst + ['0', '0'] for inst in insts]
acc, index, order = 0, 0, 0

# Initial check!
while index < len(insts):
    if insts[index][2] == "1":
        break
    if insts[index][0] == 'acc':
        acc += int(insts[index][1])
        insts[index][2] = '1'
        index += 1
    elif insts[index][0] == 'jmp':
        order += 1
        insts[index][3] = order
        index += int(insts[index][1])
    else:
        order += 1
        insts[index][3] = order
        index += 1

# Which things to change and in what order should we change them
orders = [[int(order[3]), index] for (index, order) in enumerate(insts) if int(order[3])!=0] # (switch priority, index)
orders = sorted(orders, reverse=True)

# See if it boots
def boot_at(insts, index):
    acc = 0
    while index < len(insts):
        if insts[index][2] == "1":
            return False
        if insts[index][0] == 'acc':
            acc += int(insts[index][1])
            index += 1
        elif insts[index][0] == 'jmp':
            index += int(insts[index][1])
        else:
            index += 1

    # Boot completed
    if index == len(insts):
        print("Done!", acc)
    else:
        print('Issue')
    return True

# Try to repair it, if not, revert change
def repair(order):
    or_index = order[1]
    old = insts[or_index][0]
    print(insts[or_index][0])
    
    if old == 'jmp':
        insts[or_index][0] = 'nop'
    else:
        insts[or_index][0] = 'jmp'

    if boot_at(insts, 0) is True:
        print('Yay!', or_index, insts[or_index])
        boot_at(insts, 0)
        return True
    else:
        insts[or_index][0] = old
        print(insts[or_index])
        return False

# Let's check!
for order in orders:
    print(order)
    if repair(order) is True:
        print(f'Repair successful!')
        break
    else: pass
    