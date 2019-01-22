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
	coords = (0,0)
	up = []
	right = []

	def matrixSearch(self, target) :
		print("{0}: {1}".format(self.value, self.coords))
		try :
			if self.value == target :
				return self.coords
			elif self.value < target :
				return self.right.matrixSearch(target)
			else :
				return self.up.matrixSearch(target)
		except :
			return None

	def bruteSearch(self, target) :
		row = self.bruteSearchRow(target)
		if row != None :
			return row
		else :
			try :
				return self.up.bruteSearch(target)
			except :
				return None

	def bruteSearchRow(self, target) :
		print("{0}: {1}".format(self.value, self.coords))
		if self.value == target :
			return self.coords
		else :
			try :
				return self.right.bruteSearchRow(target)
			except :
				return None

if __name__ == '__main__':
	argv = sys.argv
	assert(len(sys.argv) == 3)
	with open(str(argv[1]), 'rb') as file :
		reader = csv.reader(file)
		matrix = list()
		for csvrow in reader :
			row = list()
			for value in csvrow :
				e = Element()
				e.value = int(value)
				row.append(e)
			matrix.append(row)
		for m in range(-1, -len(matrix)-1, -1) :
			for n in range(0, len(matrix[0])) :
				e = matrix[m][n]
				e.coords = (m+4, n)
				try :
					e.up = matrix[m-1][n]
				except :
					e.up = None
				try :
					e.right = matrix[m][n+1] 
				except :
					e.right = None
		print("\t"+str(matrix[-1][0].matrixSearch(int(argv[2]))))
		print("\t"+str(matrix[-1][0].bruteSearch(int(argv[2]))))