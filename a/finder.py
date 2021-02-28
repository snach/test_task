"""Написать программу для поиска n-ого простого числа. Где n задается параметром при старте программы и время работы не должно превышать 5 минут. Для примера, n=10000:
python finder.py -n 10000
"""

import argparse
import datetime
from math import sqrt

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()
n = int(args.n)

lst_prime_nums = [2]
num = 2

start_time = datetime.datetime.now()

while len(lst_prime_nums) < n:
    num += 1
    if num > 10:
        if (num % 2 == 0) or (num % 10 == 5):
            continue
    for prime_num in lst_prime_nums:
        if prime_num > int((sqrt(num)) + 1):
            lst_prime_nums.append(num)
            break
        if num % prime_num == 0:
            break
    else:
        lst_prime_nums.append(num)

processing_time = datetime.datetime.now() - start_time

print(f'n = {n}\nprime number = {lst_prime_nums[n - 1]}')
print(f'Processing time = {processing_time}')
