a = int(input("Enter the starting range : "))
b = int (input("Enter the ending range : "))
for i in range(a,b + 1):
  if all (int(d) % 2 ==0 for d in str(i)):
   print(i)
