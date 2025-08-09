# Assignment_4_python
For Tutedude
# Task_1

Opened the text file in reading mode, whose address belong from other drive. "r" used before address to make the backslash inside address as raw characters. Same way "encoding = utf-8" used to avoid encoding error
readline method used to read the firstline from the text file. same was stored in a variable & print function used to display the first line as output
To read second line same as above repeated, after that file is closed.
To avoid, File not found error, if we try to open a text file which is not existing, Try & Except function used.
The full code used under try to avoid trace back error of variable (file1) not defined when we try to open none existing text file.

# Task_1_alter

As a alternative code was written for the same task_1 to avoid repeatation of code for reading multiple lines and for the possibility of text file containing more than the task line.
For this readlines method used to make all the lines in text file as list as output.
While loop is used to iterate all the lines in the list to print line by line as output.

# Task_2

Input function used to take data from the user
opened the text file in write mode
input data written in the opened text file
print the output data as required by Program for the user
close the text file
Input function used to take additional data from the user
Same text file opened in append mode to write additional data at end of existing data
Next line appended in the text file so that we can append additional data in the next line
Additional data appended
print the output data as required by Program for the user
Close the file
Opened the text file in reading mode to display the entire content of file as output
Read function is used to read the data & Print function used to display output as required by the Program.
Close the file
