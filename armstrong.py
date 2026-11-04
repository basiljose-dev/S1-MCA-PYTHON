n = int(input("Enter a number : "))
s = 0
for i in str(n):
    s = s + int(i) ** 3
if s == n:
  print("Armstrong number")
else:
  print("not Armstrong number")
