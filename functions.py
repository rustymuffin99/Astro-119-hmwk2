
import numpy as np
import sys

#define a function that returns a value
def expo(x):
	return np.exp(x)
#define a function that does not return a value
def show_expo(n):
	for i in range(n):
		print( expo(float(i)) ) #call the expo function


#define a main function
def main():
	n = 10 # provide a default value for n

	#check if there is a command line arg
	if(len(sys.argv)>1):
		n = int(sys.argv(1) #if additional arg provided

	#print the value of n
	print("n is equal to ",n)

	#print e^x n times
	show_expo(n)

#run the main function
if _name_ == "__main__":
	main()