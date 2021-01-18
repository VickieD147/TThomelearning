print("please think of two numbers you'd like to combine")
number_a = int(input("input your first number"))
number_b = int(input("input your second number"))
print("if you would like to add press a")
print("if you would like to subtract press t")
print("if you would like to divide press d")
print("if you would like to multiply press m")
print("if you would like to square press s")
user_input = (input("what command would you like to run?"))


def function1(number_a, number_b, user_input):

    output = "your calculation is ", number_a, user_input, number_b
    return output


def procedure1(number_a, number_b, user_input):

    message = function1(number_a, number_b, user_input)

    print(message)


procedure1(number_a, number_b, user_input)
if user_input == "a":
    print(float(number_a + number_b))
elif user_input == "t":
    print(float(number_a - number_b))
elif user_input == "d":
    print(float(number_a / number_b))
elif user_input == "m":
    print(float(number_a * number_b))
elif user_input == "s":
    print(float(number_a ** number_b))
else:
    print("can not compute")
# Task 4 Motorbike Devaluation 10% per year
motorcycle_value = int(2000)
year = int(2020)

print(year, "your motorcycle is worth", motorcycle_value)


def function_1(year, motorcycle_value,):

    output_new1 = year, "your motorcycle is worth", motorcycle_value

    return output_new1


year = year + 1
motorcycle_value = motorcycle_value - 200
while year < 2025 and motorcycle_value > 800:
    print(function_1(year, motorcycle_value))
    year += 1
    motorcycle_value -= 200
else:
    print("2025 Your motorcycle value has decreased by 50%")