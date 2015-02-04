#written by Pujun Bhatnagar
# For calculating the grades for students after importing the file from pearson and renaming it Results
# if you have any questions, please don't hesitate and just email me.
#
#
import csv
current_homework = int(raw_input('enter the assignment number: One indexed from the Pearson Homework file ')) - 1
max_points = int(raw_input('enter the max grade that the students can get in this homework: '))
row_to_be_updated_number = int(raw_input("enter the row that needs to be updated: One indexed from the t-square file ")) #we are not subtracting one since we are splitting with commas 
max_points = 100
count = 1
splitter = " "
updatedScores = {}
not_found = []
studentsWithWrongNames = {
	"Baskaran, Madhumita":"Baskaran, Madhu",
	'Braschi, Gian': "braschi, gian",
	'Breslin, Kevin': "Breslin, Kevin",
	'Callaway, Mckenzie': "Callaway, McKenzie",
	'Cappa, Christopher': "Cappa, Chris",
	'Crawford, William': "Crawford, William",
	'Diamond, Benjamin': "Diamond, Ben", 
	'Donohue, Timothy': "donohue, timmy", 
	'Everett, Joshua': "Everett, Josh", 
	'Fish, Rebecca': "Fish, Becca", 
	'Grogan, Ronald': "Grogan, Hank",
	'Ihnen, Anthony': "Ihnen, Anthony", 
	'Jackson, Amber': "jackson, amber",
	'Jae Hyuk Shin, Steve' : "Shin, Steve",
	'Kasturi, Abishek': "903051390), Abishek",
	'Kazlow, Jacob': "Kaslow, Jacob", 
	'Khan, Abdur-Raheem': "Khan, Raheem", 
	'Kim, Michael': "Kim, Michael", 
	'Kim, Woojae': "Kim, Woo Jae", 
	'Kim, Yu Jin': "Kim, Yu Jin",
	'Lawrence, Jevone': "Lawrence, Jevone",
	'McAuliffe, Alexander': "McAuliffe, Alex",
	'McBurnie, Dejuan': "mcb, dj",
	'Mcvicker, Shawn': "McVicker, Shawn",
	'Medford, Marcie': "Medford, Marci",
	'Mullins, Cassandra': "Mullins, Cassie",
	'Murley, Matthew': "Murley, Matt",
	'Patel, Arjun': "Patel, Arjun",
	'Rankin, Jillian': "Rankin, Jill",
	'Rathakrishnan, Priyadharshi': "Rathakrishnan, Priyadharshini",
	'Rich, Ryan': "rich, ryan",
	'Rogstad, Nicholas':"Rogstad, Nick",
	'Sheffield, Katarina': "Sheffield, Skye",
	'Shim, Kyuin': "Shim, Kyuin",
	'Shin, Kyung Min': "Shin, Kyung Min",
	'Smith, Joshua': "Smith, Josh", 
	'Song, Wootae': "Song, Alan",
	'Sparkman, John': "Sparkman, Jack",
	'Villanueva, Eilin': "Villanueva, Denali",
	'Votaw, Lucas': "Votaw, Luke",
	'Waites, Christopher': "Waites, Chris",
	'Wilkins, Alexander': "W, A",
	'Yi, Matthew': "Yi, Matt",
	'Zalar, Zachary': "Zalar, Zach",
	'Jang, Sung Hyun': "Jang, Sunghyun",
	'Konkala, Sai Venkat': "Konkala, Sai",
	"Ryu, Yu Jung": "Ryu, YuJung", 
	"Um, Da El": "Um, Dael"



}

with open('../../ConfidentialInformation/studentNames') as f:
	student_names = f.readlines()
	print len(student_names)
	current_homework_backup = current_homework
count = 0
for s in student_names:
	specialCase = False
	current_homework = current_homework_backup
	s = s.strip()
	temp_buffer = s
	if s in studentsWithWrongNames:
		s = studentsWithWrongNames[s]
	if len(s.split(splitter)) == 2:
 		last_name, first_name = s.split(splitter)
 		last_name = last_name[:len(last_name)-1]
 	if len(s.split(splitter)) == 3:
 		specialCase = True
 		last_name = s.split(splitter)[0]
 		first_name = s.split(splitter)[1]
 		last_name = last_name[:len(last_name)-1]
 	s = temp_buffer
	with open('../../ConfidentialInformation/rawResults.csv', 'rU') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			if len(row) == 0:
				continue
			row_list = row[0].split(',')
			if first_name in row_list and last_name in row_list:
				if specialCase:
					row_list = row[1].split(',')
					current_homework = current_homework - 1 
				if row_list[current_homework] == "":
					updatedScores[s] = 0
					# raw_input()
				else:
					updatedScores[s] = float(row_list[current_homework]) * max_points
				break


for s in student_names:
	s = s.strip()
	if s not in updatedScores.keys():
		not_found.append(s)

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