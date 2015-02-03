#written by Pujun Bhatnagar
# For calculating the grades for students after importing the file from pearson and renaming it Results
# if you have any questions, please don't hesitate and just email me.
#
#
import csv
current_homework = int(raw_input('enter the assignment number: ')) - 1
max_points = int(raw_input('enter the max grade that the students can get in this homework: '))
row_to_be_updated_number = int(raw_input("enter the row that needs to be updated: ")) - 1
max_points = 100
count = 1
splitter = " "
updatedScores = {}
not_found = []
with open('../../ConfidentialInformation/studentNames') as f:
	student_names = f.readlines()
for s in student_names:
	s = s.strip()
	if len(s.split(splitter)) == 2:
 		last_name, first_name = s.split(splitter)
 		last_name = last_name[:len(last_name)-1]
	with open('../../ConfidentialInformation/rawResults.csv', 'rU') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			if len(row) == 0:
				continue
			row_list = row[0].split(',')
			if first_name in row_list and last_name in row_list: 
				if row_list[current_homework] == "":
					updatedScores[s] = 0
				else:
					updatedScores[s] = float(row_list[current_homework]) * max_points


for s in student_names:
	s = s.strip()
	if s not in updatedScores.keys():
		not_found.append(s)

print len(updatedScores)
with open("../../ConfidentialInformation/results.csv", 'rU') as csvfile1:
	with open("../../ConfidentialInformation/updatedResults.csv", 'wb') as csvfile2:
		spamreader = csv.reader(csvfile1, delimiter=';', quotechar='|')
		spamwriter = csv.writer(csvfile2, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for row in spamreader:
			row_list = row[0].split(',')
			tosearch = row_list[1][1:] + "," + row_list[2][:len(row_list[2])-1]
			if tosearch in updatedScores:
				row_list[row_to_be_updated_number] = str(updatedScores[tosearch])
			row_updated = [1]
			row_updated[0] = ','.join(row_list)
			spamwriter.writerow(row_updated)

print "students not found", not_found
print "the length is ", len(not_found)