import re
from typing import List, Dict

from util.file_handling import read_file_stripped


def extract_raw_passports(input_lines: List[str]) -> List[List[str]]:
    raw_passports = []
    current_passport = []
    for i, line in enumerate(input_lines):
        if line == '':
            raw_passports.append(current_passport)
            current_passport = []
        elif is_last_line(i, len(input_lines)):
            current_passport.append(line)
            raw_passports.append(current_passport)
        else:
            current_passport.append(line)
    return raw_passports


def is_last_line(index: int, lines_length: int):
    return index == lines_length - 1


def extract_dict_passports(raw_passports: List[List[str]]) -> List[Dict[str, str]]:
    dict_passports = []
    for passport in raw_passports:
        extracted_passport: Dict[str, str] = {}
        for line in passport:
            data_entries = line.split(' ')
            for entry in data_entries:
                key, value = entry.split(':')
                extracted_passport[key] = value
        dict_passports.append(extracted_passport)
    return dict_passports


def extract_passports(input_lines: List[str]) -> List[Dict[str, str]]:
    raw_passports = extract_raw_passports(input_lines)
    dict_passports = extract_dict_passports(raw_passports)
    return dict_passports


def is_byr_valid(passport: Dict[str, str]) -> bool:
    byr = int(passport['byr'])
    return 1920 <= byr <= 2002


def is_iyr_valid(passport: Dict[str, str]) -> bool:
    iyr = int(passport['iyr'])
    return 2010 <= iyr <= 2020


def is_eyr_valid(passport: Dict[str, str]) -> bool:
    eyr = int(passport['eyr'])
    return 2020 <= eyr <= 2030


def is_hgt_valid(passport: Dict[str, str]) -> bool:
    hgt = passport['hgt']
    if hgt.endswith('cm'):
        hgt_int = int(hgt.split('cm')[0])
        return 150 <= hgt_int <= 193
    elif hgt.endswith('in'):
        hgt_int = int(hgt.split('in')[0])
        return 59 <= hgt_int <= 76
    else:
        return False


def is_hcl_valid(passport: Dict[str, str]) -> bool:
    hcl = passport['hcl']
    return re.search('#[0-9a-f]{6}', hcl) is not None


def is_ecl_valid(passport: Dict[str, str]) -> bool:
    allowed_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    ecl = passport['ecl']
    return ecl in allowed_eye_colors


def is_pid_valid(passport: Dict[str, str]) -> bool:
    pid = passport['pid']
    return len(pid) == 9 and re.search('^[0-9]{9}', pid) is not None


def is_data_valid(passport: Dict[str, str]) -> bool:
    return is_byr_valid(passport) and is_iyr_valid(passport) and is_eyr_valid(passport) and \
           is_hgt_valid(passport) and is_hcl_valid(passport) and is_ecl_valid(passport) and is_pid_valid(passport)


def is_passport_valid(passport: Dict[str, str], check_data: bool = False) -> bool:
    return are_all_fields_present(passport) and (not check_data or is_data_valid(passport))


def are_all_fields_present(passport: Dict[str, str]) -> bool:
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all(field in passport.keys() for field in required_fields)


def solve_part_one(passports: List[Dict[str, str]]) -> int:
    counter = 0
    for passport in passports:
        if is_passport_valid(passport):
            counter += 1

    print('part one: {} valid passports'.format(counter))
    return counter


def solve_part_two(passports: List[Dict[str, str]]) -> int:
    counter = 0
    for passport in passports:
        if is_passport_valid(passport, check_data=True):
            counter += 1

    print('part two: {} valid passports'.format(counter))
    return counter


if __name__ == '__main__':
    lines = read_file_stripped('input.txt')
    extracted_passports = extract_passports(lines)
    solve_part_one(extracted_passports)
    solve_part_two(extracted_passports)
