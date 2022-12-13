#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("welcome to the tip calculator")
bill = float(input("what was the total bill: "))
percentage = float(input("What percentage would you like to tip? 10, 12 or 15% : "))
num_of_people = int(input("please input the total amount of people to split the bill: "))
percentage = 1 + percentage/int(100)
each_person_pays = round((bill/num_of_people)) * percentage
print(f"each person should pay {each_person_pays} ")
