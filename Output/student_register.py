# creating a user input variable to be used for the total number of students
number_of_students = int(input("Input the number of students that are registering: "))

# text file to write and save all of the inputted IDs
text_file = 'reg_form.txt'
title = "Student ID"
line_counter = 1
signature = (".")*80
# opening the text file in write mode
file_open = open(text_file, "w")
file_open.write("Student ID""\n""\n")
for i in range (number_of_students):
    # accept input from the user for their ID
    student_ID = input("Input the ID number of the student: ")
    # write each entry in the opened file
    file_open.write(str(line_counter) + " | " + student_ID+"\n" + signature + "\n")
    line_counter += 1
    

# closing the text file
file_open.close()
    