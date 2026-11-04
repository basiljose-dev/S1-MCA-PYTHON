age = int(input("Enter your age " ))
vote = lambda age: "Eligible for Vote" if age >= 18 else"Not Eligible for Vote"
print(vote(age))
