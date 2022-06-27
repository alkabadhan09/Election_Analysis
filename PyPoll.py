# Data we need to retrieve
# Total number of votes cast
# Complete list of candidates who received votes
# %of votes each candidate won
# total number of votes each candidare won
# winner of the election based on popular vote




import csv
import os
# assign a variable for the file to load and path
file_to_load= os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # read and print the header row.
    headers = next(file_reader)
    print(headers)






# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    #wrte data to file
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
   
    
