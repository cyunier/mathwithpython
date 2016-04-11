'''
Calculate the mean
'''

import random

def calculate_mean(numbers):
	s = sum(numbers)
	N = len(numbers)
	mean = s/N

	return mean

if __name__ == '__main__':
	grades = [100, 35, 100, 65, 99, 80, 79]
	mean = calculate_mean(grades)
	N = len(grades)

	print('Mean grade over the last {0} exame is {1} '.format(N, mean))