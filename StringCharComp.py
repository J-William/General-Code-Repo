# Given two strings return the characters shared in common and the characters not shared

string1 = 'abc def ghi'				#input("Enter a string:")
string2 = 'b d f h j'				#input("Enter a string to compare:")

shared, unshared = [], []

# Remove white space from strings
string1 = string1.replace(' ','')	
string2 = string2.replace(' ','')

# Make a dict of keys for each char in string1
D = dict.fromkeys(string1)			

# Set the initial values 0
for keys in D:						
	D[keys] = 0

# If a char from string2 is listed in dict increment value 1; else add it at value 0
for char in string2:				
	if char in D.keys():
		D[char] += 1
	else:
		D[char] = 0

# Now have a dictionary with keys for each char in both strings and values > 0 
# if shared or = 0 if not shared; divide them into lists for display
for keys in D:						
	if D[keys] > 0:					
		shared += keys
	else:
		unshared += keys


print(f"Shared: {shared}")
print(f"Unshared: {unshared}")



