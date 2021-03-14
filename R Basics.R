#Task 1 Ask for input values and display
name <- readline("Please Write Your Name :")
Hello <-paste("Welcome", name, "!")
print(Hello)
age <- readline ("How old are you?")
Info <-paste("Well", name, ", who's", age, "years old, it's nice to meet you!")
print(Info)
# Task 2 program to retrieve details of objects in memory
airport.codesUK <-list("Birmingham" = "BHX", "London Heathrow" = "LHR", "Bristol" = "BRS", "Manchester" = "MAN")
airport.dubai <-"DBX"
airport.sanfran<-"SFO"
ls()
print("total objects in memory")
print(ls.str())
#Task 3 a: to create  a sequence of numbers from 20-50
20:50
#b: mean of numbers between 20-50
myseq <- seq(20, 50)
print(myseq)
results.mean <- mean(myseq)
print("The Mean of these values is:")
print(results.mean)
#c: sum of numbers between 51-91
sum(51:91)
