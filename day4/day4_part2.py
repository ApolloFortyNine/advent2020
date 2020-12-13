import re

f = open('input.txt')
whole_file = f.read()

passports = whole_file.split('\n\n')
valid_count = 0
byr = r'byr:(\d{4})\b'
iyr = r'iyr:(\d{4})\b'
eyr = r'eyr:(\d{4})\b'
hgt = r'hgt:(\d+)(in|cm)\b'
hcl = r'hcl:\#(([0-9]|[a-f]){6})\b'
ecl = r'ecl:(\w+)\b'
pid = r'pid:(\d{9})\b'

valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

for passport in passports:
    passport = passport.replace('\n', ' ')
    byr_match = re.search(byr, passport)
    iyr_match = re.search(iyr, passport)
    eyr_match = re.search(eyr, passport)
    hgt_match = re.search(hgt, passport)
    hcl_match = re.search(hcl, passport)
    ecl_match = re.search(ecl, passport)
    pid_match = re.search(pid, passport)
    valid = True

    try:
        byr_num = int(byr_match.group(1))
        iyr_num = int(iyr_match.group(1))
        eyr_num = int(eyr_match.group(1))
        if byr_num < 1920 or byr_num > 2002:
            valid = False
        if iyr_num < 2010 or iyr_num > 2020:
            valid = False
        if eyr_num < 2020 or eyr_num > 2030:
            valid = False
        hgt_num = int(hgt_match.group(1))
        if hgt_match.group(2) not in ['in', 'cm']:
            valid = False
        if hgt_match.group(2) == 'in':
            if hgt_num < 59 or hgt_num > 76:
                valid = False
        if hgt_match.group(2) == 'cm':
            if hgt_num < 150 or hgt_num > 193:
                valid = False
        if hcl_match.group(1):
            pass
        if ecl_match.group(1) not in valid_eye_colors:
            valid = False
        if pid_match.group(1):
            pass

    except:
        valid = False
    if valid is True:
        valid_count += 1

print(valid_count)
