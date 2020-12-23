from src.main.day4.day4 import *


def test_extract_raw_passports():
    input_lines = ['byr:2024 iyr:2016', 'eyr:2034 ecl:zzz pid:985592671 hcl:033b48', '',
                   'hgt:66cm', 'byr:2020 ecl:zzz iyr:2029', 'hcl:cfb18a eyr:1947']

    result = extract_raw_passports(input_lines)

    assert len(result) == 2
    assert len(result[0]) == 2
    assert len(result[1]) == 3
    assert result == [['byr:2024 iyr:2016', 'eyr:2034 ecl:zzz pid:985592671 hcl:033b48'],
                      ['hgt:66cm', 'byr:2020 ecl:zzz iyr:2029', 'hcl:cfb18a eyr:1947']]


def test_is_last_line__true():
    result = is_last_line(5, 6)

    assert result is True


def test_is_last_line__false():
    result = is_last_line(5, 7)

    assert result is False


def test_extract_dict_passport():
    raw_passports = [['byr:2024 iyr:2016', 'eyr:2034'],
                     ['hgt:66cm', 'byr:2020 ecl:zzz iyr:2029', 'hcl:cfb18a eyr:1947']]

    result = extract_dict_passports(raw_passports)

    assert len(result) == 2
    assert len(result[0]) == 3
    assert len(result[1]) == 6
    assert result == [{'byr': '2024', 'iyr': '2016', 'eyr': '2034'},
                      {'hgt': '66cm', 'byr': '2020', 'ecl': 'zzz', 'iyr': '2029', 'hcl': 'cfb18a', 'eyr': '1947'}]


def test_is_passport_valid__true__without_cid_without_data_validation():
    passport = {'hgt': '66cm', 'byr': '2020', 'ecl': 'zzz', 'iyr': '2029', 'hcl': 'cfb18a', 'eyr': '1947', 'pid': '558'}

    result = is_passport_valid(passport)

    assert result is True


def test_is_passport_valid__true__with_cid_without_data_validation():
    passport = {'hgt': '66cm', 'byr': '2', 'ecl': 'z', 'iyr': '2', 'hcl': 'c', 'eyr': '194', 'pid': '558', 'cid': '123'}

    result = is_passport_valid(passport)

    assert result is True


def test_is_passport_valid__true__with_data_validation():
    passport = {'hgt': '66cm', 'byr': '1919', 'ecl': 'zzz', 'iyr': '2029', 'hcl': 'cfb18a', 'eyr': '1947', 'pid': '558'}

    result = is_passport_valid(passport, check_data=True)

    assert result is False


def test_is_passport_valid__false():
    passport = {'hgt': '66cm', 'ecl': 'zzz', 'iyr': '2029', 'hcl': 'cfb18a', 'eyr': '1947', 'pid': '558'}

    result = is_passport_valid(passport)

    assert result is False


def test_is_byr_valid__true():
    passport = {'byr': '1920'}

    result = is_byr_valid(passport)

    assert result is True


def test_is_byr_valid__false():
    passport = {'byr': '2003'}

    result = is_byr_valid(passport)

    assert result is False


def test_is_iyr_valid__true():
    passport = {'iyr': '2020'}

    result = is_iyr_valid(passport)

    assert result is True


def test_is_iyr_valid__false():
    passport = {'iyr': '2009'}

    result = is_iyr_valid(passport)

    assert result is False


def test_is_eyr_valid__true():
    passport = {'eyr': '2020'}

    result = is_eyr_valid(passport)

    assert result is True


def test_is_eyr_valid__false():
    passport = {'eyr': '2031'}

    result = is_eyr_valid(passport)

    assert result is False


def test_is_hgt_valid__true__cm():
    passport = {'hgt': '150cm'}

    result = is_hgt_valid(passport)

    assert result is True


def test_is_hgt_valid__false__cm():
    passport = {'hgt': '194cm'}

    result = is_hgt_valid(passport)

    assert result is False


def test_is_hgt_valid__true__in():
    passport = {'hgt': '59in'}

    result = is_hgt_valid(passport)

    assert result is True


def test_is_hgt_valid__false__in():
    passport = {'hgt': '55in'}

    result = is_hgt_valid(passport)

    assert result is False


def test_is_hgt_valid__false__no_unit():
    passport = {'hgt': '151'}

    result = is_hgt_valid(passport)

    assert result is False


def test_is_hgt_valid__false__wrong_unit():
    passport = {'hgt': '151dm'}

    result = is_hgt_valid(passport)

    assert result is False


def test_is_hcl_valid__true():
    passport = {'hcl': '#123abc'}

    result = is_hcl_valid(passport)

    assert result is True


def test_is_hcl_valid__false():
    passport = {'hcl': '#123abz'}

    result = is_hcl_valid(passport)

    assert result is False


def test_is_ecl_valid__true():
    passport = {'ecl': 'brn'}

    result = is_ecl_valid(passport)

    assert result is True


def test_is_ecl_valid__false():
    passport = {'ecl': 'wat'}

    result = is_ecl_valid(passport)

    assert result is False


def test_is_pid_valid__true():
    passport = {'pid': '000000001'}

    result = is_pid_valid(passport)

    assert result is True


def test_is_pid_valid__false():
    passport = {'pid': '0123456789'}

    result = is_pid_valid(passport)

    assert result is False
