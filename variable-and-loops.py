import numpy as np
def main():
	i = 0
	n = 10
	x = 119

	#use numpy to declare arrays

	y = np.zeros(n,dtype=float)


	for i in range(n):		#i in range [0,n-1]
		y[i] = 2.0 * float(i)+1 #set y = 2i+1 as floats

	for y_element in y:
		print(y_element)

#execute the main function
if __name__ == "__main__":
	main()