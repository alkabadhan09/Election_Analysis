# Data we need to retrieve
# Total number of votes cast
# Complete list of candidates who received votes
# %of votes each candidate won
# total number of votes each candidare won
# winner of the election based on popular vote



# Add our dependencies
import csv
from itertools import count
import os
# assign a variable for the file to load and path
file_to_load= os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


#1. initialize a total vote counter
total_votes = 0

# Candidates
candidate_options = []

# deeclaring empty dictionary
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # read and print the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        
        #2. Add the total vote count
        total_votes += 1
        #Candidate names
        candidate_name = row[2]
        # if candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #add it to the list of candidates.
            candidate_options.append(candidate_name)
            # begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # add votes
        candidate_votes[candidate_name] += 1

# % of votes for each candidate by looping through the counts
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    #retrieve the vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # calculate the % of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # to do: print out each candidate's name, vote count, and% of votes 
    # Determine winning vote count and candidate
    # determine if the votes is greater than the winning count
    print (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
    
    
    
    
    
# print the candidate name and % of votes
print(f"{candidate_name}: received {vote_percentage}% of the vote.")
#3. Prrint the total votes.
print(total_votes)

# Print candidate list
print(candidate_options)

# print the candidate votes dictionary
print(candidate_votes)





# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    #wrte data to file
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
   
    
