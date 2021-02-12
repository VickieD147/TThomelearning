import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("Holidays.csv")
holidays = data
print(data.shape)
print(holidays)
print(holidays.shape)
print(holidays.iloc[3:8])
print(holidays[["Destination", "All.Inc.Hotels"]])
print("The average number of 'All Inclusive Hotels' across all the destinations is: ", data["All.Inc.Hotels"].mean())
myfilter = data["Rating"] > 8
highratings = data[myfilter]
print("The highest customer rated destinations are:")
print(highratings)
myfilter2 = data["Rating"] < 3
lowratings = data[myfilter2]
print("The lowest scoring destinations are:")
print(lowratings)
hotelfilter = data["All.Inc.Hotels"] > 9
luxury = data[hotelfilter]
print("These destinations have the biggest variety of All Inclusive Hotels")
print(luxury)
data = pd.read_csv("Holidays.csv")
y = data["All.Inc.Hotels"]
x = data["Rating"]
plt.xlabel("Average Customer Rating")
plt.ylabel("All Inclusive Hotels")
plt.title("Customer ratings compared to the amount of all inclusive hotels on site")
plt.scatter(x, y)
plt.show()
data = pd.read_csv("Holidays.csv")
plt.bar(data["Destination"], data["Rating"])
plt.show()
