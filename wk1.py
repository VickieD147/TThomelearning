# Task 1 Import random numbers & make friends
import random

r_number = random.randint(1, 10)
username = input("Hi friend, what's your name?")
print("Hello " + username + " nice to meet you!")
print(username + ", I'm thinking of a number between 1 - 10")
g_number = int(input("can you guess the number?"))
if g_number == r_number:
    print("Congrats!" + username + ", you're a genius!"),
else:
    print("Sorry" + username + ", better luck next time! It was"),
    print(r_number)
# Task 2 Favourite numbers and jokes
Fav_number = input("Anyway, tell me your favourite number between 1 - 100 and I'll tell you a joke!")
convert_fnum = int(Fav_number)
if 0 < convert_fnum <= 20:
    print("What do you call a dinosaur with no eyes?")
    print("Do-you-think-he-saw-us!")
elif 20 < convert_fnum <= 37:
    print("What do you call cheese that isn't yours?")
    print("Nacho cheese!")
elif 37 < convert_fnum <= 54:
    print("Who says sticks and stones may break my bones but words will never hurt me?")
    print("Someone who has never been hit with a dictionary!")
elif 54 < convert_fnum <= 73:
    print("Why can't you tell a joke while standing on ice?")
    print("Because it might crack up!")
elif 73 < convert_fnum <= 100:
    print("Why did the orange stop in the middle of the road?")
    print("Because it ran out of juice!")
# Task 3 User Menu
print("Now " + username + "tell me about your perfect meal")
starter = input("What is your favourite starter?")
main = input("Sounds Great! What would your main course be?")
dessert = input("Wow! and what would you finish that off with something sweet?")
drink = input("With all that amazing food what would you wash it down with?")
print("So" + username + " your favourite meal would be " + starter + " followed by " + main + " with " + dessert)
print(" all paired with a tipple of " + drink)

# Task 4 Motorbike Devaluation 10% per year
Motorcycle_value = int(2000)
Year = int(2020)
print("your motorcycle is worth", Motorcycle_value, Year)
Motorcycle_value = Motorcycle_value - 200
Year = Year + 1
print("your motorcycle is worth", Motorcycle_value, Year)
Motorcycle_value = Motorcycle_value - 200
Year = Year + 1
print("your motorcycle is worth", Motorcycle_value, Year)
Motorcycle_value = Motorcycle_value - 200
Year = Year + 1
print("your motorcycle is worth", Motorcycle_value, Year)
Motorcycle_value = Motorcycle_value - 200
Year = Year + 1
print("your motorcycle is worth", Motorcycle_value, Year)
Motorcycle_value = Motorcycle_value - 200
Year = Year + 1
print("your motorcycle is worth", Motorcycle_value, Year)
if Motorcycle_value == 1000:
    print(Year, "Your motorcycle value has decreased by 50% since purchase.")

# Task 5 calculator
print("please think of two numbers you'd like to combine")
number_a = int(input("input your first number"))
number_b = int(input("input your second number"))
print("if you would like to add press a")
print("if you would like to subtract press t")
print("if you would like to divide press d")
print("if you would like to multiply press m")
print("if you would like to square press s")
userinput = (input("what command would you like to run?"))

a = number_a + number_b
t = number_a - number_b
d = number_a / number_b
m = number_a * number_b
s = number_a ** number_b

if userinput == "a":
    print(float(number_a+number_b))
elif userinput == "t":
    print(float(number_a-number_b))
elif userinput == "d":
    print(float(number_a/number_b))
elif userinput == "m":
    print(float(number_a*number_b))
elif userinput == "s":
    print(float(number_a**number_b))
# finished
