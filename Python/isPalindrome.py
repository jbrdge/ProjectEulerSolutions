#is palindrome

def is_palindrome(a):

	forwards = list(str(a))
	backwards = list(reversed(forwards))

	n = len(forwards)//2
	if forwards[:n] == backwards[:n]:
		return 1
	else:
		return 0