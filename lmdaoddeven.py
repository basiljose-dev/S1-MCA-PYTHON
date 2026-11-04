odd = lambda a: a % 2 != 0
even = lambda l: l % 2 == 0

a = int(input("Enter the number: "))
l = int(input("Enter the number: "))

print("Number is odd:", odd(a))
print("Number is even:", even(l))
