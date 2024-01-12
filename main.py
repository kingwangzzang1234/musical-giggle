def adder(num1: int, num2: int) -> int:
	return num1+num2


if __name__=='__main__':
	u_input = input('Enter two nums with space: ')
	num1, num2 = [int(c) for c in u_input.split()]
	print(adder(num1,num2))
