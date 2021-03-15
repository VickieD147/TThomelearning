#Task 1 write a programe with 3 vectors combine to create 3:5 matrix...
a <- c(93, 83, 62, 56, 83)
b <- c(13, 27, 48, 53, 73)
c <- c(15, 32, 29, 26, 49)
mymatrix <- cbind(a, b, c)
mymatrix
#Plot the matrix on a graph
x <- mymatrix(c)
y <- mymatrix(b)
plot(x, y, main = "Plotting a Basic Scattergraph",
     xlab = "Random Numbers", ylab = "Ascending Numbers",
     pch = 19, frame = FALSE)
#Task 2 Create a Dataframe of Employess info 5 columns)
Name<- c("Marcus", "Roman", "Lilly", "Maria", "Saida")
Age <- c(32, 43, 29, 67, 36)
Gender <- c("Male", "Male", "Female", "Female", "Female")
Role <- c("Assistant", "Deputy", "Trainee", "CEO", "Manager")
YearsInRole <- c("3 Years", "19 Years", "1 Year", "32 years", "7 Years")
employ.data <- data.frame(Name, Age, Gender, Role, YearsInRole)
print(employ.data)
#Task 3 install gg plot and create graph
install.packages("ggplot2", dependencies = TRUE)
library(ggplot2)
myseq <- seq(1,20)
root <- myseq ^2
data1 <- data.frame(
  myseq,
  root)
print(data1)
ggplot(data, aes(x=myseq, y=root))
qplot(x, y)
#Task 4 Create a simple bar plot of five subjects
data <- data.frame(
  Animals=c("Foxes", "Mice", "Badgers", "Rabbits", "Moles"),
  Sightings=c(7, 12, 3, 18, 5)
)
ggplot(data, aes(x=Animals, y=Sightings)) +
  geom_bar(stat = "identity")

