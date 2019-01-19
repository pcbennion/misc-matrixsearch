# search.py
#
# Searches for the location of elements with a specific value within a m-by-n
# matrix with the following properties:
# - Every column is sorted such that values ascend from top to bottom
# - Every row is sorted such that values ascend from left to right
import sys
import csv

class Element:
	value = 0
	coords = {0, 0}
	up = []
	right = []

	def search(self, target) :
		print(self.value)
		try :
			if self.value == target :
				return self.coords
			elif self.value < target :
				self.right.search(target, output)
			else :
				self.up.search(target, output)
		except :
			return output

def matrixSearch(e, target) :
	e.search(target, ret)
	return ret

if __name__ == '__main__':
	print(sys.argv)
	argv = sys.argv
	assert(len(sys.argv) == 3)
	with open(str(argv[1]), 'rb') as file :
		reader = csv.reader(file)
		for csvrow in reader :
			print(csvrow)
			matrix = list()
			row = list()
			for value in csvrow :
				e = Element()
				e.value = value
				row.append(e)
				print(e.value)
			matrix.append(row)
		for m in range(len(matrix), 0) :
			for n in range(0, len(matrix[0])) :
				e.coords = {m, n}
				try :
					e.up = matrix[m-1][n]
				except :
					e.up = None
				try :
					e.right = matrix[m][n+1] 
				except :
					e.right = None
		print(matrixSearch(matrix[len(matrix)][0], argv[3]))


