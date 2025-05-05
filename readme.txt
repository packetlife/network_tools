Here's a `readme.txt` file for your script:

```
README.txt

BitCalc Command Line Script
===========================

Description:
------------
This script converts data measurements between various units using either legacy or IEEE notation.

Usage:
------
python bitcalc.py <input_units> <input_amount> <notation>

Arguments:
----------
1. <input_units>: The unit of the input amount. Valid options are:
   - bits
   - bytes
   - kilobits
   - kilobytes
   - megabits
   - megabytes
   - gigabits
   - gigabytes
   - terabits
   - terabytes
   - petabits
   - petabytes

2. <input_amount>: The numerical value to convert. It should be a number, and the script will strip out any non-numeric characters except for the decimal point.

3. <notation>: The notation to use for the conversion. Valid options are:
   - legacy: Uses the traditional notation where 1 kilobyte = 1024 bytes.
   - ieee: Uses the IEEE notation where 1 kilobyte = 1000 bytes.

Example:
--------
python bitcalc.py megabits 1 legacy

This command converts 1 megabit using the legacy notation and prints the results.

python bitcalc.py megabits 1 ieee

This command converts 1 megabit using the IEEE notation and prints the results.

Output:
-------
The script prints the converted values for the following units:
- bits
- bytes
- kilobits
- kilobytes
- megabits
- megabytes
- gigabits
- gigabytes
- terabits
- terabytes
- petabits
- petabytes

Author:
-------
Your Name

Version:
--------
1.0

License:
--------
This script is provided "as-is" without any warranty. Use at your own risk.
```
