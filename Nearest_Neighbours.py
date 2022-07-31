from collections import Counter
import math

# ----------------------------------------------------------
# GOAL: 
# Given the dataset of ages of people and if they enjoy 
# pineapple on pizza, predict if a person of a certain age
# would also like pineapple on pizza or not 
# ----------------------------------------------------------



def knn(data, query, k):
	neighbor_distances_and_indices = []  # format:[[distance,index],[distance,index]...]

	
	# 1. For each example in the data
	for index, example in enumerate(data):
		#break;
		# 1.1 Calculate the distance between the query example and the current
		# example from the data.
		#-----------------------------------
		distance = euclidean_distance(query, example)
		#-----------------------------------
		
		# 1.2 Add the distance and the index of the example to an ordered collection
		#-----------------------------------
		neighbor_distances_and_indices.append([distance, index])
		#-----------------------------------

	# 2. Sort the ordered collection of distances and indices from
	# smallest to largest (in ascending order) by the distances
	#-----------------------------------
	neighbor_distances_and_indices.sort(key=lambda x:x[0])
	#-----------------------------------



	# 3. Pick the first K entries from the sorted collection
	#-----------------------------------
	ans = neighbor_distances_and_indices[:k]
	#-----------------------------------


	# 4. Get the labels of the selected K entries
	#-----------------------------------
	indexs_arr = [ i[1] for i in ans ]
	neighbor_ks_Yvalues = [ data[i][1] for i in indexs_arr ]
	#-----------------------------------

	# 5. Return the mode of the K labels
	#-----------------------------------
	return ans, mode(neighbor_ks_Yvalues)
	#-----------------------------------


	


#This fucntion returns the mode of the params
def mode(labels):
	return Counter(labels).most_common(1)[0][0]

#This fucntion returns the distance between to points
def euclidean_distance(point1, point2):
	sum_squared_distance = 0
	for i in range(len(point1)):
		sum_squared_distance += math.pow(point1[i] - point2[i], 2)
	return math.sqrt(sum_squared_distance)


def main():
	
	'''
	# Data
	# 
	# Column 0: age
	# Column 1: likes pineapple
	'''
	data = [
	   [22, 1],
	   [23, 1],
	   [21, 1],
	   [18, 1],
	   [19, 1],
	   [25, 0],
	   [27, 0],
	   [29, 0],
	   [31, 0],
	   [45, 0],
	]

	
	# Question:
	# Given the data we have, does a 33 year old like pineapples on their pizza?
	# Change the parameters to understand their effect
	query = [33]
	k = 3

	# You must return the #k nearest neighbors and the index in the data 
	# and the prediction of the query


	k_nearest_neighbors, prediction = knn(data, query, k,)
	print(k_nearest_neighbors, "\n", prediction)

if __name__ == '__main__':
	main()