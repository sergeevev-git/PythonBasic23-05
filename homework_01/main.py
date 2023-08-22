from itertools import filterfalse
import math

"""
Домашнее задание №1
Функции и структуры данных
"""
def power_numbers(*nums):
	"""
	функция, которая принимает N целых чисел,
	и возвращает список квадратов этих чисел
	>>> power_numbers(1, 2, 5, 7)
	<<< [1, 4, 25, 49]
	"""
	return [i ** 2 for i in nums]


print('power_numbers(2,7,11): ', power_numbers(2, 7, 11))
print('power_numbers(1,5,3,71): ', power_numbers(1, 5, 3, 71))

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_odd(num):
	return num % 2

def is_prime(num):
	if num <= 1:
		return False
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True


def filter_numbers(nums, condition):
	"""
	функция, которая на вход принимает список из целых чисел,
	и возвращает только чётные/нечётные/простые числа
	(выбор производится передачей дополнительного аргумента)

	>>> filter_numbers([1, 2, 3], ODD)
	<<< [1, 3]
	>>> filter_numbers([2, 3, 4, 5], EVEN)
	<<< [2, 4]
	"""
	if condition == ODD:
		return [i for i in nums if i % 2]
	elif condition == EVEN:
		return [i for i in nums if i % 2 == 0]
	else:
		return list(filter(is_prime, nums))


print('filter_numbers([1, 2, 3], ODD): ', filter_numbers([1, 2, 3], ODD))
print('filter_numbers([2, 3, 4, 5], EVEN): ', filter_numbers([2, 3, 4, 5], EVEN))
print('filter_numbers([2, 7, 4, 11, 22, 26, 1, 0, 93], PRIME): ',
	  filter_numbers([2, 7, 4, 11, 22, 26, 1, 0, 93], PRIME))
