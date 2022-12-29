
def AlternateShift(arr, x):


	mid = len(arr) // 2


	c = 0



	while arr[mid] != x:


		z = arr.pop(mid)



		if c % 2 == 0:
			arr.insert(0, z)



		else:
			arr.append(z)


		c += 1


Arr = [2, 8, 5, 9, 10]


a = Arr[0]


AlternateShift(Arr, a)


print(*Arr)

