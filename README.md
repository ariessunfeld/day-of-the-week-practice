# About

`dotw-practice.py` is a command-line interface for practicing the Day of the Week mental math algorithm described [here](https://gmmentalgym.blogspot.com/2011/03/day-of-week-for-any-date-revised.html).

It currently offers three modes: Leap Year mode, All Years mode, and Full mode. In Leap Year mode, you will be prompted with century-agnostic leap years (e.g., "8" or "40") and asked to provide the corresponding leap year code (assuming a century like 2000, in which year 0 has code 0). In All Years mode, you will be prompted with specific years in the range 1600-2100 and asked to provide the year code. And in Full mode, you will be prompted with full dates in the same interval and asked to provide the day of the week as a string (e.g., "mon").

# Setup

Python 3.12+

# Usage

`python dotw-practice.py MODE`  
Supported modes: `leap_year`, `all_years`, `full`

