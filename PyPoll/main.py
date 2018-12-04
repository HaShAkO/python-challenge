import csv
import os

# Create file path and save as variable
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:
    #Read csv and parse data 
    reader = csv.reader(csvfile, delimiter=',')
    # Skip HEaders
    csvheader = next(reader)
    # List of Candidate
    candidate = []
    #Loop trough candidates to count it
    for row in reader:
        candidate.append(row[2])

    candidate_count = [[x,candidate.count(x)] for x in set(candidate)]
    #Blank variables
    votes = []
    name = []
    #Loop to count the votes for each candidate
    for row in candidate_count:
        name.append(row[0])
        votes.append(row[1])

    candidate_zip = zip(name, votes)
    candidate_list = list(candidate_zip)

    winner = max(votes)
    #Loop to find the Wiiner
    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]       
            
total_votes = len(candidate)

#Calculate the percents of the votes for each candidate
correy_total = candidate.count('Correy')
correy_percent = int(correy_total) / int(total_votes)

o_tooley_total = candidate.count("O'Tooley")
o_tooley_percent = o_tooley_total / total_votes

li_total = candidate.count('Li')
li_percent = li_total / total_votes

khan_total = candidate.count('Khan')
khan_percent = khan_total / total_votes

#Printing in a file
with open('PyPoll.txt', 'w') as text_file:
    print(f'Election Results', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Total Votes: {total_votes}', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Khan: {khan_percent:.3%} - {khan_total} Votes', file=text_file)
    print(f'Correy: {correy_percent:.3%} - {correy_total} Votes', file=text_file)
    print(f'Li: {li_percent:.3%} - {li_total} Votes', file=text_file)
    print(f"O'Tooley: {o_tooley_percent:.3%} - {o_tooley_total} Votes", file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Winner: {winner_name}', file=text_file)
    print(f'-------------------------', file=text_file)

#Opens the output file in r mode and prints to terminal
txtpath = os.path.join('PyPoll.txt')
with open(txtpath, 'r') as readfile:
    print(readfile.read())