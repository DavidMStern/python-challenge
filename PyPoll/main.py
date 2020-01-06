# Import functions
import os
import csv

# Read and open csv file
poll_data = os.path.join('Resources', 'election_data.csv')

with open(poll_data, newline = "") as csvfile:
    # Read file to variable
    read_poll = csv.reader(csvfile, delimiter = ',')

    # Skip Header
    next(csvfile)

    # Assigning variables that will be changed
    voter_total = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

    # Looping through the data
    for row in read_poll:
        # Tally up the voters
        voter_total += 1

        if str(row[2]) == 'Khan':
            khan_votes += 1
        elif str(row[2]) == 'Correy':
            correy_votes += 1
        elif str(row[2]) == 'Li':
            li_votes += 1
        elif str(row[2]) == 'O\'Tooley':
            otooley_votes += 1
    
    # Calculating percents and winner
    khan_percent = '{:.2%}'.format(khan_votes / voter_total)
    correy_percent = '{:.2%}'.format(correy_votes / voter_total)
    li_percent = '{:.2%}'.format(li_votes / voter_total)
    otooley_percent = '{:.2%}'.format(otooley_votes / voter_total)
    winner_total = 0
    
    if khan_votes > winner_total:
        winner = "Khan"
        winner_total = khan_votes
    if correy_votes > winner_total:
        winner = 'Correy'
        winner_total = correy_votes
    if li_votes > winner_total:
        winner = 'Li'
        winner_total = li_votes
    if otooley_votes > winner_total:
        winner = 'O\'Tooley'
        winner_total = otooley_votes

    # Print everything out
    print('Election Results')
    print('-------------------------')
    print(f'Total votes: {voter_total}')
    print('-------------------------')
    print(f'Khan: {khan_percent} ({khan_votes})')
    print(f'Correy: {correy_percent} ({correy_votes})')
    print(f'Li: {li_percent} ({li_votes})')
    print(f'O\'Tooley: {otooley_percent} ({otooley_votes})')
    print('-------------------------')
    print(f'Winner: {winner}')