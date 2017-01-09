with open ('hello.txt') as temp_file:
	for line in temp_file:
		city_name = line
		city_temp = temp_file.readline()