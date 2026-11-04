startyear=int(input("Enter the start year"))
endyear=int(input("Enter the end year"))
print("list of leap years:")
#loop through between the start and endyear
for year in range(startyear,endyear):
#check if the year is a leap year
	if((year%4==0)and(year%100!=0))or (year%400==0):
		print(year)
