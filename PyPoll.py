# Data we need to retrieve
# Total number of votes cast
# Complete list of candidates who received votes
# %of votes each candidate won
# total number of votes each candidare won
# winner of the election based on popular vote

# add our dependencies
import csv
import os

# assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# create a filename variable to a direct or indiract path
file_to_save = os.path.join("analysis" , "election_analysis.txt")

# initialize tha total vote counter
total_votes = 0

# candidate options
candidate_options = []

# declate the empty dictionary
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read file
with open(file_to_load) as election_data:

   # to do: read and analyze data here
   file_reader = csv.reader(election_data)

   # Read and print the header row
   headers = next(file_reader)
   
   #Print each row in the CSV file.
   for row in file_reader:
       
        # add the total vote count
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        
            # Add the candidate name to candidate options
            candidate_options.append(candidate_name)

            # Begin tracking thatcandidate's vote count
            candidate_votes[candidate_name] = 0

        # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    print(election_results, end="")

    #Save the final vtecount to the text file
    txt_file.write(election_results)

    

    # determine the % of votes for each candidate by looping through the counts
    # iterate through the candidate list

    for candidate_name in candidate_votes:
        # retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        # calculate the % of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)
        txt_file.write(candidate_results)

        # To Do: print out each candidate's name, vote count, and percentage of votes to the terminal
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Determiine winning vote count and candidate
        # Determine if the votes is greater than the winning count

        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

            # and set the winning_candidate = candidate_name
            winning_candidate = candidate_name

    winning_candidate_summary = (

        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)







 
        
        
        
        
        
