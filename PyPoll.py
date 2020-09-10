# Add dependencies 
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#file_to_load = 'Resources/election_results.csv'

# This code is to write a file to a direct or indirect path to the file. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# creating a variable to do so. 
# initializing the vote counter beofre opening the file and increment it by 1 so that the increment happens in a loop
total_votes = 0
# reseting the candidate names
candidate_options = []
# Declaring the empty dictionaries
candidate_votes = {}
# Winning candiate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read the file.
# election_data = open(file_to_load,'r') # option 1: to open and close the file
# Option 2: using with statement
with open(file_to_load) as (election_data):

#To do: Perform Analysis read and analyze data
# read the file object with the reader function
    file_reader = csv.reader(election_data)

# Print each row in the csv file
#instead of closing the file we are going to print it)
    #for row in file_reader:
        #print(row) # option 2 using the with statement
    # Read the Headers row.
    headers = next(file_reader)
    
    for row in file_reader:
        # add the total vote count:
        total_votes += 1
    #print(total_votes)

# open the election results and read the file.
#with open (file_to_load)  as election_data:

# print the candidate name from each row
        candidate_name = row[2]

# Add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # candidate votes
            candidate_votes[candidate_name] = 0

        # begin tallying or adding the vote counts 
        candidate_votes[candidate_name] += 1

#Save the results to our text file
with open(file_to_save,"w") as txt_file:
    
    #print final vote count to the terminal
    election_results = (
        f"\nElection results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    #save the final vote count to the text file/
    txt_file.write(election_results)
    
    # Determine the percentage of votes for each candiate by looping throught the counts
    # 1. iterate through the candidate list
    for candidate_name in candidate_votes:

        #2. retreivevote count of a candidate
        votes = candidate_votes[candidate_name]

        # calcualte percentage of votes
        vote_percentage = (float(votes) / float(total_votes)) * 100
        #print(candidate_name, candidate_votes)
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # print each candidates resutls count and percentage to the terminal
        print(candidate_results)

        # save candidate results to text file
        txt_file.write(candidate_results)

        #Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2.if true then set winning_count = votes and winning percentage =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage

            #3. set thhe winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

        # print the candidate name and percentage of votes
        #print(f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate} \n"
        f"Winning Vote Count: {winning_count:,} \n"
        f"Winning Vote Percentage: {winning_percentage:.1f}% \n"
        f"-------------------------\n")
    print (winning_candidate_summary)
        
    #save to text file
    txt_file.write(winning_candidate_summary)