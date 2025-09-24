# Problem-2: Generate odd number series up to 'a'

a = int(input("Enter a number: "))
num = 1

for i in range(a):
    print(num, end=" ")
    num += 2
