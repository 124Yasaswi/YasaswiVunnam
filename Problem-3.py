# Problem-3: Modified odd number series

a = int(input("Enter a number: "))
num = 1

if a % 2 == 0:
    limit = a - 1   # even -> one less
else:
    limit = a       # odd -> full series

for i in range(limit):
    print(num, end=" ")
    num += 2
