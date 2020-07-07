x = [1, 2, 3, 4, 5]
y = [2, 6]
y = iter(y)
counter = 0
total = 0.0
while counter != len(x):
	# cycles through the y list.
    # multiplies 2 by 1, then 6 by 2. Then 2 by 3.
    total = total + x[counter] * next(y)
    counter += 1
print(total)