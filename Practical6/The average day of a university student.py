import matplotlib.pyplot as plt
# original data
daily_schedule ={
    'Sleeping': 8,
    'Classes': 6,
    'Studying': 3.5,
    'TV': 2,
    'Music': 1,
    'Other': 3.5
}
# Calculate total hours in a day
total_hours =24
#(1)dictionary containing the information
print("Dictionary containing the informatioin:")
print(daily_schedule)
print()
#(2)pie chart plot describing the data
activities = list(daily_schedule.keys())
time_spent = list(daily_schedule.values())
# Plotting the pie chart without percentages
plt.figure(figsize=(10, 8))
plt.pie(time_spent, labels=activities, autopct=lambda p: '{:.1f}h'.format(p) if p else '', startangle=140, colors=plt.cm.tab20.colors)
plt.title('Average Day of a University Student')
plt.axis('equal')
plt.show()


