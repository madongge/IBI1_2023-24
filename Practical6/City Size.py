import matplotlib.pyplot as plt 

# Define the cities and their populations in a list of dictionaries
cities = [
    {"name": "Edinburgh", "country": "UK", "population": 0.56},
    {"name": "Glasgow", "country": "UK", "population": 0.62},
    {"name": "Stirling", "country": "UK", "population": 0.04},
    {"name": "London", "country": "UK", "population": 9.7},
    {"name": "Haining", "country": "China", "population": 0.58},
    {"name": "Hangzhou", "country": "China", "population": 8.4},
    {"name": "Shanghai", "country": "China", "population": 29.9},
    {"name": "Beijing", "country": "China", "population": 22.2}
]

# Separate populations of cities in the UK and China into two lists
uk_populations = [city["population"] for city in cities if city["country"] == "UK"]
china_populations = [city["population"] for city in cities if city["country"] == "China"]

# Sort the populations of cities in the UK and China
uk_populations.sort()
china_populations.sort()

# Plotting
plt.figure(figsize=(10, 5))  # Set the size of the figure

# Bar plot for UK city populations
plt.subplot(1, 2, 1)  # Create a subplot with 1 row, 2 columns, and select the first subplot
plt.bar(range(len(uk_populations)), uk_populations)  # Create the bar plot
plt.title('City Populations in the UK')  # Set the title of the plot
plt.xlabel('Cities')  
plt.ylabel('Population (millions)')  
plt.xticks(range(len(uk_populations)), [city["name"] for city in cities if city["country"] == "UK"], rotation=45)  # Set the tick labels for the x-axis

# Bar plot for China city populations
plt.subplot(1, 2, 2)  
plt.bar(range(len(china_populations)), china_populations)  # Create the bar plot
plt.title('City Populations in China')  
plt.xlabel('Cities')  
plt.ylabel('Population (millions)')  
plt.xticks(range(len(china_populations)), [city["name"] for city in cities if city["country"] == "China"], rotation=45)  
plt.show()  # Display the plot
