data = []
with open('food.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
print(data)