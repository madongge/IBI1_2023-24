density=5 #the initial density is 5%
day=1 #use day1 as initial
while density<=90:
    density=density*2  #the cell density doubles in density per day when density is less than 90
    day+=1
print("I can stay away from lab for",day,"days")
print("On day", day,"the cell density is larger than 90%") #print the different case
