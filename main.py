# Task 1 Store input in a file
my_file = open("numbers.txt", "w")
my_file.write("Input Numbers\n")
my_file.close()
print("Please choose 4 numbers")
first_digit = int(input("Please input your 1st number: "))
second_digit = int(input("Please input your 2nd number: "))
third_digit = int(input("Please input your 3rd number: "))
fourth_digit = int(input("Please input your 4th number: "))
data = first_digit, second_digit, third_digit, fourth_digit
my_file = open("numbers.txt", "a")
my_file.write(str(data))
my_file.write("\n")
my_file.close()

# Task 2 Function for converting percentages into grades
percentage = int(input("Please insert students percentage mark: "))


def mark_grade(percentage):
    percent = int(percentage)
    if percent < 40:
        return"Fail"
    elif 40 <= percent < 60:
        return"D"
    elif 60 <= percent < 75:
        return"C"
    elif 75 <= percent < 90:
        return"B"
    elif 90 <= percent < 100:
        return"A"
    else:
        return"You have entered an invalid number"


grade = mark_grade(percentage)
print("Your grade is", str(grade), "(", percentage, "%)")
