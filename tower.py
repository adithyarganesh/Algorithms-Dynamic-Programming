#Tower Plcement Greedy Algorithm
houses = [1,4,7,8,10,13,15]
towers = []
t_range = 2
count = 1
for i in range(max(houses) + t_range + 1):
    towers.append(0)
for house in houses:
    if towers[house] == 0:
        for _ in range(house, house + 2*t_range):
            towers[_] = count
        count += 1
print(towers)