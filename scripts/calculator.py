#written by Pujun Bhatnagar
# For calculating the grades for students after importing the file from pearson and renaming it Results
# if you have any questions, please don't hesitate and just email me.
#
#
import csv
current_homework = int(raw_input('enter the assignment number: ')) - 1
max_points = int(raw_input('enter the max grade that the students can get in this homework: '))
current_homework = 10
max_points = 100
count = 1
splitter = " "
updatedScores = {}
not_found = []
with open('studentNames') as f:
	student_names = f.readlines()
for s in student_names:
	s = s.strip()
	# print "here is the length" , len(s.split(splitter))
	if len(s.split(splitter)) == 2:
 		last_name, first_name = s.split(splitter)
 		last_name = last_name[:len(last_name)-1]
 	# print "here is the last name", last_name
	# print "here is the first name", first_name
	with open('rawResults.csv', 'rU') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			# print row
			if len(row) == 0:
				continue
			row_list = row[0].split(',')
			# print row_list
			if first_name in row_list and last_name in row_list: 
				if row_list[current_homework] == "":
					updatedScores[s] = 0
					# print count, "." , row_list[0], " ", row_list[1], " ", (float(0))
				else:
					updatedScores[s] = float(row_list[current_homework]) * max_points
					# print count, "." , row_list[0], " ", row_list[1], " ", (float(row_list[current_homework]) * max_points)
			# 	count+=1
print len(updatedScores)
# for i in updatedScores:		
# 	with open("results.csv", 'rU') as csvfile1:
# 		with open("updatedResults.csv", 'wb') as csvfile2:
# 			spamreader = csv.reader(csvfile1, delimiter=';', quotechar='|')
# 			spamwriter = csv.writer(csvfile2, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 			for row in spamreader:
# 				# print "here is the row", row
# 				row_list = row[0].split(',')
# 				# print "Row List", row_list
# 				# print i
# 				# print row
# 				if i in row[0]:
# 					row_list[2] = str(updatedScores[i])
# 					# print i
# 					# print row_list
# 					# raw_input("enter to continue")
# 				row_updated = [1]
# 				row_updated[0] = ','.join(row_list)
# 					# print row_updated
				# spamwriter.writerow(row_updated)	

with open("results.csv", 'rU') as csvfile1:
	with open("updatedResults.csv", 'wb') as csvfile2:
		spamreader = csv.reader(csvfile1, delimiter=';', quotechar='|')
		spamwriter = csv.writer(csvfile2, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for row in spamreader:
			row_list = row[0].split(',')
			tosearch = row_list[1][1:] + "," + row_list[2][:len(row_list[2])-1]
			if tosearch in updatedScores:
				row_list[3] = str(updatedScores[tosearch])
			row_updated = [1]
			row_updated[0] = ','.join(row_list)
			spamwriter.writerow(row_updated)


# with open('swag') as f:
#     		gt_ids = f.readlines()
# for current_name in gt_ids:
# 	found = False
# 	current_name = current_name.strip()
# 	#print "here is the length" , len(current_name.split(splitter))
# 	if len(current_name.split(splitter)) == 2:
# 		last_name, first_name = current_name.split(splitter)
# 	else:
# 		last_name, middle_name, first_name = current_name.split(splitter)
# 		first_name = middle_name + " " + first_name

# 	with open('Results.csv', 'rU') as csvfile:
# 		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# 		for row in spamreader:
# 			if len(row) == 0:
# 				continue
# 			row_list = row[0].split(',')
# 			if first_name in row_list and last_name in row_list: 
# 				if row_list[current_homework] == "":
# 					print count, "." , row_list[0], " ", row_list[1], " ", (float(0))
# 				else:
# 					print count, "." , row_list[0], " ", row_list[1], " ", (float(row_list[current_homework]) * max_points)
# 				count+=1
# 				found = True
# 				break
# 		if found == False:
# 			not_found.append(current_name)

# print '*'*10
# display_counter = 1
# print  "here are all the ones that were not found", not_found
# with open('Results.csv', 'rb') as csvfile:
# 	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# 	for row in spamreader:
# 		if len(row) == 0:
# 			continue
# 		row_list = row[0].split(',')
# 		if display_counter == 161:
# 			print count, "." , row
# 			count+=1
# 		display_counter +=1

		
