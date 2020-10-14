#python exceptions let you deal
#with unexpected results

try:
	print(a) 
except:
	print("a is not defined")

#use a specific error
try:
	print(a)
except NameError:
	print("a is still not defined")
except:
	print("Something else went wrong")

#this will break our program
#since a is not defined
print(a)