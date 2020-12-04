from collections import defaultdict 
import re, time
start = time.time()

passports = open('day_4/input.txt', 'r') 
pports = passports.read().split('\n\n')
reqs = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

# Part 1
valids_1 = [pport for pport in pports if all(req in pport for req in reqs)]
print(f'Part 1: {len(valids_1)}')

# Part 2
valids_2 = 0

pport_list = [pport.replace('\n',' ').split(' ') for pport in valids_1]
pport_tuples = [[tuple(item.split(':')) for item in pport if len(item)>1] \
                for pport in pport_list]
pport_dict = {}
pport_dict = [dict(pport) for pport in pport_tuples]

ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

for pport in pport_dict:
    if int(pport['byr']) in range(1920, 2003) \
    and int(pport['iyr']) in range(2010, 2021) \
    and int(pport['eyr']) in range(2020, 2031) \
    and any(ecl in pport['ecl'] for ecl in ecls) \
    and re.search(r'^#(?:[0-9a-f]{6})$', pport['hcl']) is not None \
    and re.search(r'^[0-9]{9}$', pport['pid']) is not None:
        if pport['hgt'][-2:] == 'cm':
            if int(pport['hgt'][:-2]) in range(150, 194):
                valids_2 += 1
        elif pport['hgt'][-2:] == 'in':
            if int(pport['hgt'][:-2]) in range(59, 77):
                valids_2 += 1

print(f'Part 2: {valids_2}')

finish = time.time()
print(f'Done in {(finish - start):.3f}s')




