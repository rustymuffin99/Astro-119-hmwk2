#string

s = "I am a string"
print(type(s))   #will say str

#boolean

yes = True
print(type(yes))

no = False
print(type(no))

# List -- ordered and changeable

alpha_list = ["a", "b", "c"]
print(type(alpha_list))
print(type(alpha_list[0]))
alpha_list.append("d")
print(alpha_list)


alpha_tuple = ("a", "b", "c")
print(type(alpha_tuple))

try:							#attempt the following line
	alpha_tuple[2] = "d"		#won't work and will raise TypeError
except TypeError:				#when we get a TypeError
	print("We can't add elements to tuples!") 
print(alpha_tuple)