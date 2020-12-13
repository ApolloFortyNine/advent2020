import re

f = open('input.txt')
lines = f.readlines()

valid_count = 0

for line in lines:
    line = line.strip()
    parts = line.split(' ')
    matched = re.match(r"(\d*)-(\d*) (\w): (\w*)", line)
    min_num = int(matched.group(1))
    max_num = int(matched.group(2))
    letter = matched.group(3)
    password = matched.group(4)
    letter_count = password.count(letter)
    if (letter_count >= min_num) and (letter_count <= max_num):
        valid_count += 1
print(valid_count)

# Part 2
valid_count = 0

for line in lines:
    line = line.strip()
    matched = re.match(r"(\d*)-(\d*) (\w): (\w*)", line)
    first_pos = int(matched.group(1))
    next_pos = int(matched.group(2))
    letter = matched.group(3)
    password = matched.group(4)
    matches = 0
    print(line)
    if (first_pos-1 <= len(password)) and (password[first_pos-1] == letter):
        matches += 1
    if (next_pos-1 <= len(password)) and (password[next_pos-1] == letter):
        matches += 1
    if matches == 1:
        valid_count += 1
print(valid_count)