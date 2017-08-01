#File: Project0002.py

first_term = 1
second_term = 2
total_sum = 0

while first_term < 4000000:
	if first_term%2 == 0:
		total_sum += first_term
	second_term += first_term
	first_term = second_term-first_term


print total_sum
