# import the required libraries

import os
import csv

# declare and instatiate the variables
total_votes = 0


# set path to the budget data and the output file
cwd = os.path.abspath(__file__)
dir_name = os.path.dirname(cwd)
datapath = os.path.join(dir_name, 'Resources', 'election_data.csv')
outpath = os.path.join(dir_name, "analysis", "Election_Results.txt")


# open the data file

with open(datapath) as csvfile:

    ## use csv reader to read data from the file
    reader = csv.reader(csvfile)
    data = list(reader)

    # remove the header
    votes = data[1:]

# Initialize a dictionary to hold candidate vote counts
vote_counts = {}

# Count the votes for each candidate
for vote in votes:
    #Candidate names are in index 2
    candidate = vote[2]
    if candidate not in vote_counts:
        vote_counts[candidate] = 0
    vote_counts[candidate] += 1

# Calculate total votes
total_votes = len(votes)

# **********************************************************************************
#                   Output results to text file
# **********************************************************************************
# Open the output file
with open(outpath, 'w') as f:
    # Write the output to the file
    f.write(f"Election Results\n")
    f.write(f"----------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write(f"----------------------\n")
    for candidate, vote_count in vote_counts.items():
        percentage = (vote_count / total_votes) * 100
        f.write(f"{candidate}: {percentage:.2f}% ({vote_count})\n")
    
    # Find the candidate with the greatest votes
    max_votes = max(vote_counts.values())
    winner = max(vote_counts, key=vote_counts.get)
    f.write(f"----------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write(f"----------------------\n")
