#define the main() function
def main():

	i = 0 			#declare an integer i
	x = 119.0 		#declare a float x

	for i in range(120):		#loop i from 0-119
		if((i%2)==0):			#if i is even add 3 to x
			x += 3.
		else:
			x -= 5.

	s = "%3.2e" % x

	print(s) 					#print s to the screen


if __name__ == "__main__":		#if the main() function exists, run it
	main()