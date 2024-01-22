import os
import sys
import random
import pickle

HIGH_SCORE_FILE = '.dotw-high-score.pkl'
HIGH_SCORES = {}
LEAP_YEAR_SCORE = 0
ALL_YEARS_SCORE = 0
FULL_MODE_SCORE = 0

def increment_leap_year_score():
    global LEAP_YEAR_SCORE, HIGH_SCORES, HIGH_SCORE_FILE
    LEAP_YEAR_SCORE += 1
    if LEAP_YEAR_SCORE > HIGH_SCORES.get('leap_years'):
        HIGH_SCORES['leap_years'] = LEAP_YEAR_SCORE
        pickle.dump(HIGH_SCORES, open(HIGH_SCORE_FILE, 'wb'))

def reset_leap_year_score():
    global LEAP_YEAR_SCORE
    LEAP_YEAR_SCORE = 0

def increment_all_years_score():
    global ALL_YEARS_SCORE, HIGH_SCORES, HIGH_SCORE_FILE
    ALL_YEARS_SCORE += 1
    if ALL_YEARS_SCORE > HIGH_SCORES.get('all_years'):
        HIGH_SCORES['all_years'] = ALL_YEARS_SCORE
        pickle.dump(HIGH_SCORES, open(HIGH_SCORE_FILE, 'wb'))

def reset_all_years_score():
    global ALL_YEARS_SCORE
    ALL_YEARS_SCORE = 0

def increment_full_mode_score():
    global FULL_MODE_SCORE, HIGH_SCORES, HIGH_SCORE_FILE
    FULL_MODE_SCORE += 1
    if FULL_MODE_SCORE > HIGH_SCORES.get('full'):
        HIGH_SCORES['full'] = FULL_MODE_SCORE
        pickle.dump(HIGH_SCORES, open(HIGH_SCORE_FILE, 'wb'))

def reset_full_mode_score():
    global FULL_MODE_SCORE
    FULL_MODE_SCORE = 0

def practice_leap_years():
    global LEAP_YEAR_SCORE, HIGH_SCORES
    leap_years = [x*4 for x in range(25)]
    leap_year_codes = [(x*5)%7 for x in range(25)]

    while True:
        year_idx = random.choice(range(25))
        leap_year = leap_years[year_idx]
        leap_year_code = leap_year_codes[year_idx]
        ans = input(f'Year: {leap_year}. Code: ')
        ans = int(ans)
        if ans == leap_year_code:
            increment_leap_year_score()
            print(f'Correct!   Streak: {LEAP_YEAR_SCORE}. Best: {HIGH_SCORES.get("leap_years")}.')
        else:
            print(f'Incorrect. Code is: {leap_year_code}')
            reset_leap_year_score()

def get_year_code(year: int):
    last_two_digits = year % 100
    century = year // 100
    century_code = (7 - (century%4)*2) % 7
    leap_years = [x*4 for x in range(25)]
    leap_year_codes = [(x*5)%7 for x in range(25)]
    leap_year_idx = last_two_digits // 4
    leap_year_diff = last_two_digits % 4
    return (leap_year_codes[leap_year_idx] + leap_year_diff + century_code) % 7

def get_month_code(month: int):
    months = {0:6, 1:2, 2:2, 3:5, 4:0, 5:3, 6:5, 7:1, 8:4, 9:6, 10:2, 11:4}
    return months.get(month)

def num_to_dotw(num: int):
    dotw = {
        1: ['mon', 'monday'], 
        2: ['tue', 'tues', 'tuesday'], 
        3: ['wed', 'weds', 'wednesday'], 
        4: ['thu', 'thur', 'thurs', 'thursday'], 
        5: ['fri', 'friday'], 
        6: ['sat', 'saturday'], 
        0: ['sun', 'sunday']}
    return dotw.get(num)

def month_to_max_day(month: int):
    if month in [0, 2, 4, 6, 7, 9, 11]:
        return 31
    elif month == 1:
        return 28
    elif month in [3, 5, 8, 10]:
        return 30

def month_to_name(month: int):
    months = {0: 'January', 1: 'February', 2: 'March', 3: 'April', 4: 'May', 5: 'June', 6: 'July', 7: 'August', 8: 'September', 9: 'October', 10: 'November', 11: 'December'}
    return months.get(month)

def _practice_dates():
    global HIGH_SCORES, FULL_MODE_SCORE
    month = random.choice(range(12))
    month_code = get_month_code(month)
    year = random.choice(range(1600, 2100))
    is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    max_day = month_to_max_day(month)
    if is_leap_year and month == 1:
        max_day += 1
    if is_leap_year and month in [0, 1]:
        month_code -= 1
    day = random.choice(range(1, max_day+1))
    month_name = month_to_name(month)
    day_suffix = {0: 'th', 1: 'st', 2: 'nd', 3: 'rd', 4: 'th', 5: 'th', 6: 'th', 7: 'th', 8: 'th', 9: 'th'}.get(day%10)
    ans = input(f'Calculate the Day of the Week of {month_name} {day}{day_suffix}, {year}. Answer: ')
    ans = ans.lower()
    correct_ans_numeric = (month_code + get_year_code(year) + day) % 7
    if ans in num_to_dotw(correct_ans_numeric):
        increment_full_mode_score()
        print(f'Correct!    Streak: {FULL_MODE_SCORE}. Best: {HIGH_SCORES.get("full")}.')
    else:
        true_dotw = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}.get(correct_ans_numeric)
        print(f'Incorrect. It is a {true_dotw}.')
        reset_full_mode_score()

def practice_dates():
    while True:
        _practice_dates()

def practice_years():
    global ALL_YEARS_SCORE, HIGH_SCORES
    while True:
        year = random.choice(range(1600, 2100))
        code = get_year_code(year)
        ans = input(f'Year: {year}. Code: ')
        ans = int(ans)
        if ans == code:
            increment_all_years_score()
            print(f'Correct!   Streak: {ALL_YEARS_SCORE}. Best: {HIGH_SCORES.get("all_years")}.')
        else:
            print(f'Incorrect. Code is: {code}')
            reset_all_years_score()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python dotw-practice.py MODE')
        print('Supported values for MODE: leap_years, all_years, full')
        sys.exit()
    if sys.argv[-1] not in ['leap_years', 'all_years', 'full']:
        print(f'Unrecognized MODE: {sys.argv[-1]}')
        print('Supported values for MODE: leap_years, all_years, full')
        sys.exit()
    if os.path.isfile(HIGH_SCORE_FILE):
        HIGH_SCORES = pickle.load(open(HIGH_SCORE_FILE, 'rb'))
    else:
        HIGH_SCORES = {'all_years': 0, 'leap_years': 0, 'full': 0}
        pickle.dump(HIGH_SCORES, open(HIGH_SCORE_FILE, 'wb'))
    print('[Press Ctrl+C to Quit at Any Time]')
    if sys.argv[-1] == 'all_years':
        practice_years()
    elif sys.argv[-1] == 'leap_years':
        print('\n(Showing only the last two digits of the year.\nE.g., "16" means "2016" and "4" means "2004", etc.)\n')
        practice_leap_years() 
    elif sys.argv[-1] == 'full':
        practice_dates()
