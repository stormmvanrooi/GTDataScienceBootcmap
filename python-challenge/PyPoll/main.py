import csv
import os

election_data = os.path.join("/Users/svanrooi/DataViz/python_challenge/PyPoll/Resources/election_data.csv")

#Set variables
total_votes= 0
candidates=[]
percentage=[]
vote_count=[]

with open(election_data, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)

#The total number of votes cast
    for row in csvreader:
        total_votes = total_votes + 1

#The total number of votes per candidate
    if row[2] in candidates:
        candidates.append(row[2])
        index = candidates.index(row[2])
        vote_count.append(1)
    else:
        index = candidates.index(row[2])
        vote_count[index] += 1
   
#Calculate percentage & winner of election

for votes in vote_count:
    percent = (votes/total_votes) * 100
    percent = round(percent)
    percent = "%.3f%%" % percent
    percentage.append(percent)
    
# Find the winning candidate
winner = max(vote_count)
index = vote_count.index(winner)
winning_candidate = candidates[index]


#The winner of the election based on popular vote.  

print("Election Results")
print("---------------------------------")
print("Total Votes:", total_votes)
print("---------------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percentage[i])} ({str(vote_count[i])})")
print("---------------------------------")
print("Winner:", winning_candidate)
print("---------------------------------")