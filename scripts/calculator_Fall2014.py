#written by Pujun Bhatnagar
# For calculating the grades for students after importing the file from pearson and renaming it Results
# if you have any questions, please don't hesitate and just email me.
#
#
import csv
current_homework = int(raw_input('enter the assignment number: ')) - 1
max_points = int(raw_input('enter the max grade that the students can get in this homework: ')) 
count = 1
not_found = []
with open('GTID') as f:
    		gt_ids = f.readlines()
for current_name in gt_ids:
	found = False
	current_name = current_name.strip()
	if len(current_name.split(" ")) == 2:
		last_name, first_name = current_name.split(" ")
	else:
		last_name, middle_name, first_name = current_name.split(" ")
		first_name = middle_name + " " + first_name

	with open('Results.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			if len(row) == 0:
				continue
			row_list = row[0].split(',')
			if first_name in row_list and last_name in row_list: 
				print count, "." , row_list[0], " ", row_list[1], " ", (float(row_list[current_homework]) * max_points)
				count+=1
				found = True
				break
		if found == False:
			not_found.append(current_name)

print '*'*10
display_counter = 1
print  "here are all the ones that were not found", not_found
# with open('Results.csv', 'rb') as csvfile:
# 	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# 	for row in spamreader:
# 		if len(row) == 0:
# 			continue
# 		row_list = row[0].split(',')
# 		if display_counter == 336:
# 			print count, "." , row
# 			count+=1
# 		display_counter +=1

		