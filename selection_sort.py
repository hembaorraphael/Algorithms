#selection sort

#ALGORITHM

#find the smallest element in the array
#put the smallest element at the begining of the  array
#Then select  smallest element in the remaining unsorted array
#   if the value of the element at index j is less than value at index i
#      Swap the values at the respective index


def selection_sort(array):
	length = len(array)
	for i in range(length):
		#assuming smallest element is at index i

		for j in range(i+1, length):
			#Selecting the smallest element in the remaining unsorted array
			if array[j] < array[i]:
				array[j],array[i] = array[i], array[j]

	return array





arr = [10,80,40,10,20]

results = selection_sort(arr)
print(results)




