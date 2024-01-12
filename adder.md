```shell
vagrant@ubuntu:~/Documents/dev/musical-giggle$ touch adder.py
vagrant@ubuntu:~/Documents/dev/musical-giggle$ vi adder.py
vagrant@ubuntu:~/Documents/dev/musical-giggle$ python adder.py
hello
vagrant@ubuntu:~/Documents/dev/musical-giggle$ cat adder.py
print('hello')
vagrant@ubuntu:~/Documents/dev/musical-giggle$ git add adder.py
vagrant@ubuntu:~/Documents/dev/musical-giggle$ git commit -m "feat: Create adder.py"
[main 05e7629] feat: Create adder.py
 1 file changed, 1 insertion(+)
 create mode 100644 adder.py
vagrant@ubuntu:~/Documents/dev/musical-giggle$ vi adder.py
vagrant@ubuntu:~/Documents/dev/musical-giggle$ python adder.py
  1
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
"contribute.md" 0L, 0B                                                                           0,0-1         All
  1 function add(num1: int, num2: int)
7
vagrant@ubuntu:~/Documents/dev/musical-giggle$ cat adder.py
def adder(num1: int, num2: int) -> int:
	return num1+num2


if __name__=='__main__':
  1
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
"main.py" 0L, 0B                                                                                 0,0-1         All
  1 def adder(num1: int, num2: int) -> int:
	print(adder(3,4))
vagrant@ubuntu:~/Documents/dev/musical-giggle$ git add adder.py
vagrant@ubuntu:~/Documents/dev/musical-giggle$ git commit -m "feat: Add Feature - Return Sum of 2 nums"
[main ee9a794] feat: Add Feature - Return Sum of 2 nums
 1 file changed, 6 insertions(+), 1 deletion(-)
vagrant@ubuntu:~/Documents/dev/musical-giggle$ vi adder.py
vagrant@ubuntu:~/Documents/dev/musical-giggle$ python adder.py
7
vagrant@ubuntu:~/Documents/dev/musical-giggle$ cat adder.py
def add(num1: int, num2: int) -> int:
	# add -> adder 이나 이미 adder라고 해서 add로 바꿈
	return num1+num2


if __name__=='__main__':
	print(add(3,4))
vagrant@ubuntu:~/Documents/dev/musical-giggle$ git add adder.py
vagrant@ubuntu:~/Documents/dev/musical-giggle$ git commit "fix: Rename func name adder to add"
error: pathspec 'fix: Rename func name adder to add' did not match any file(s) known to git
vagrant@ubuntu:~/Documents/dev/musical-giggle$ git commit -m "fix: Rename func name adder to add"
[main a6cd4b7] fix: Rename func name adder to add
 1 file changed, 3 insertions(+), 2 deletions(-)
vagrant@ubuntu:~/Documents/dev/musical-giggle$ touch contribute.md
vagrant@ubuntu:~/Documents/dev/musical-giggle$ vi contribute.md
vagrant@ubuntu:~/Documents/dev/musical-giggle$ git add contribute.md
vagrant@ubuntu:~/Documents/dev/musical-giggle$ git commit -m "docs: Create contribute.md"
[main 41a50cf] docs: Create contribute.md
 1 file changed, 2 insertions(+)
 create mode 100644 contribute.md
vagrant@ubuntu:~/Documents/dev/musical-giggle$ touch main.py
vagrant@ubuntu:~/Documents/dev/musical-giggle$ vi main.py
vagrant@ubuntu:~/Documents/dev/musical-giggle$ python main.py
Enter two nums with space: 2 3
5
vagrant@ubuntu:~/Documents/dev/musical-giggle$ cat main.py
def adder(num1: int, num2: int) -> int:
	return num1+num2


if __name__=='__main__':
	u_input = input('Enter two nums with space: ')
	num1, num2 = [int(c) for c in u_input.split()]
	print(adder(num1,num2))
vagrant@ubuntu:~/Documents/dev/musical-giggle$ git add main.py
vagrant@ubuntu:~/Documents/dev/musical-giggle$ git commit -m "refactor: Create main.py
>
> To adder.py make run on main function"
[main 0eb4651] refactor: Create main.py
 1 file changed, 8 insertions(+)
 create mode 100644 main.py
```
