iterations = 3
koch_set = "F"

for i in range(iterations):
    koch_set = koch_set.replace("F","FLFRFLF")

print "[",
for aLetter in koch_set:
	if aLetter == "L":
		print '"l", 60,'
	elif aLetter == "R":
		print '"r", 120,'
	else:
		print '"f", ', 100.0 / (3 ** (iterations - 1)), ","
print "]"