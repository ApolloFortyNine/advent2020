import re

f = open('input.txt')
whole_file = f.read()

passports = whole_file.split('\n\n')
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_count = 0

for passport in passports:
    passport = passport.replace('\n', ' ')
    field_names = re.findall(r'(\w+):', passport)
    for x in required_fields:
        if x not in field_names:
            break
    else:
        valid_count += 1

print(valid_count)
