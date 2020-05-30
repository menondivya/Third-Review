import TSPFuzzyCost as fuzzy

#Sensor Values
distance=input("Distance (0 to 500) ")
difficulty=input("Difficulty (0 or 1) ")
condition=input("Condition (0 to 50) ")

#Pass it to the Fuzzy function
cost=fuzzy.getCost(distance,difficulty,condition)

print("Weight for TSP:")
print(cost)

#use the obtained cost in TSP

#Test case:
#1) Dis=500,diff=100,cond=100: cost=1
#2) Dis=20,diff=90,cond=60: cost=5
#3) Dis=400,diff=30,cond=70: cost=4
#4) Dis=30,diff=10,cond=5: cost=6
#5) Dis=250,diff=45,cond=80: cost=5
