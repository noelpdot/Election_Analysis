# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.[STEP 1]
counties = []
county_votes ={}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout. [STEP 2]
largest_county = ""  
largest_turnout = 0 # county with the largest / most votes
# county_total_votes = 0 #Total Votes  , can also use total_votes

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row. [STEP 3]
        # county_total_votes += 1; its the same as total votes in the election
        county = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write a decision statement that checks that the [STEP 4A]
        # county does not match any existing county in the county list.
        if county not in counties:

            # 4b: Add the existing county to the list of counties. [STEP 4B]
            counties.append(county)

            # 4c: Begin tracking the county's vote count. [STEp 4C]
            county_votes[county] = 0

        # 5: Add a vote to that county's vote count. [STEP 5]
        county_votes[county] += 1


# Save the results to our text file.
with open(file_to_save, "w") as election_results:

    # Print the final vote count (to terminal)
    election_result = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    
    print(election_result)

    election_results.write(election_result)

    # 6a: Write a repetition statement to get the county from the county dictionary. [STEP 6A]
    for county_name in county_votes:
        
        # 6b: Retrieve the county vote count. [STEP 6B]
        county_vote_count = county_votes[county_name]
        
        # 6c: Calculate the percent of total votes for the county.[STEP 6C]
        total_county_vote_percentage = (float(county_vote_count) / float(total_votes)) *100

        # 6d: Print the county results to the terminal. [STEP 6D]
        county_result= (
            f"{county_name}: {total_county_vote_percentage:.1f}% ({county_vote_count:,})\n")
        
        print(county_result)
        
        # 6e: Save the county votes to a text file. [STEP 6E]
        election_results.write(county_result)
        
        # 6f: Write a decision statement to determine the winning county and get its vote count. [STEP 6F]
        if (county_vote_count > largest_turnout):
            largest_turnout = county_vote_count
            largest_county = county_name

    # 7: Print the county with the largest turnout to the terminal.
    largest_county_summary = (
        f"\n-----------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-----------------------\n")

    print(largest_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    election_results.write(largest_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        election_results.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    election_results.write(winning_candidate_summary)
