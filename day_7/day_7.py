file = open('day_7/input.txt', 'r')
rules = file.read().splitlines()

split_rules = [rule.replace(' bags','')\
                    .replace(' bag','')\
                    .replace('.','')   \
                    .split(' contain ') for rule in rules]

color_list = ['shiny gold']

for color in color_list:
    for rule in split_rules:
        if color in rule[1]:
            color_list.append(rule[0].strip())

print(len(set(color_list))-1)

def count_inside(bag):
    bag_count = 0
    for rule in split_rules:
        if bag in rule[0] and 'no other' not in rule[1]:
            split_bag_list = rule[1].split(', ')
            pair_bag_list = [bag.split(' ', 1) for bag in split_bag_list]

            for (num, color) in pair_bag_list:
                bag_count += int(num) * count_inside(color) + int(num)  # one for each current bag

    return bag_count

gold_inside = count_inside('shiny gold')
print(gold_inside)
