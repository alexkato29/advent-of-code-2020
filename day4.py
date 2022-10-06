from string import digits
REQUIRED = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

with open("inputs/day4.txt") as f:
    lines = f.read()

lines = lines.split('\n\n')
lines = [line.replace('\n', ' ') for line in lines]

# Part 1
passports = []
for line in lines:
    passport = {}
    for field in line.split():
        key, value = field.split(":")
        passport[key] = value
    if all(attr in passport for attr in REQUIRED):
        passports.append(passport)

print(len(passports))


# Part 2
valid = 0

for passport in passports:
    if not 1920 <= int(passport.get("byr")) <= 2002:
        continue
    if not 2010 <= int(passport.get("iyr")) <= 2020:
        continue
    if not 2020 <= int(passport.get("eyr")) <= 2030:
        continue

    if 'cm' in passport.get("hgt"):
        if not 150 <= int(passport.get("hgt")[:-2]) <= 193:
            continue
    elif 'in' in passport.get("hgt"):
        if not 59 <= int(passport.get("hgt")[:-2]) <= 76:
            continue
    else:
        continue

    if not passport.get("hcl").startswith('#'):
        continue
    if not all(c in digits + 'abcdef' for c in passport.get("hcl")[1:]):
        continue

        # check ecl
    if not passport.get("ecl") in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        continue

        # check pid
    if len(passport.get("pid")) != 9:
        continue
    if not all(c in digits for c in passport.get("pid")):
        continue
    valid += 1

print(valid)
