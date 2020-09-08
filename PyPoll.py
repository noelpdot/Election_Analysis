
# retrieve data from data source or CSV file
#Find the total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# the total number of votes each candidate won
# The winner of the election based on popular vote. 

import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#file_to_load = 'Resources/election_results.csv'

# This code is to write a file to a direct or indirect path to the file. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the election results and read the file.
# election_data = open(file_to_load,'r') # option 1: to open and close the file
with open(file_to_load) as election_data: # Option 2: using with statement 

#To do: Perform Analysis read and analyze data
# read the file object with the reader function
    file_reader = csv.reader(election_data)

# Close the file 
# Print each row in the csv file
# election_data.close() (instead of closing the file we are going to print it)
    #for row in file_reader:
        #print(row) # option 2 using the with statement
    headers = next(file_reader)
    print(headers)

# open the election results and read the file.
#with open (file_to_load)  as election_data:

    #print the file object 
    #print(election_data)



#usint the with statement opent the file as text file
#with open(file_to_save,"w") as txt_file:

#write some data to the file
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson, ")
    #txt_file.write("Arapahoe, Denver, Jefferson") # want to write a new line
    #txt_file.write("Counties in the Election\n")
    #txt_file.write("---------------------------\n") 
    #txt_file.write("Arapahoe\nDenver\nJefferson")

# using the open() function with the "w" mode we will write data to the file.
#open(file_to_save,"w")

# Close the file
#outfile.close()