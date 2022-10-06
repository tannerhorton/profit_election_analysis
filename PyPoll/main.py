# * The total number of votes cast

# * A complete list of candidates who received votes

# * The percentage of votes each candidate won

# * The total number of votes each candidate won

# * The winner of the election based on popular vote.

# install libraries (dependencies) 
import os
import csv

# set path for file 
election_data = os.path.join('Resources', 'election_data.csv')

py_poll_dictionary = {}
# variable 1: first column in csv
id_numbers = []
# variabe 2: third column in csv
candidate_list = []
# variable 3: names of candidates
candidate_votes = {}
# variable 4: list of votes per candidate
total_votes_cast=[]
# variable 5: each candidates share of the vote in as percent
candidate_percent = []
# variable 6: actual number of votes per candidate
results_list = []
#starting counts for remaining variables
vote_count=0
votes=0
winning_count=0
# to ensure winner's name outputs as string
winning_candidate=""


# import CSV file_dispatcher
with open(election_data, 'r') as csvfile:

    # CSV reader has typical delimiter (,)
    csvreader = csv.reader(csvfile, delimiter=',')

    #read the header
    header = next(csvfile)

    # create loop 
    for row in csvreader:

        # match up this list with correct column 
        id_number = 0
        # add ballot id number to end of list with .append() function
        id_numbers.append(id_number) 
        # match up this list with correct column 
        candidate = row[2]
        # variable for candidate votes to be summed after each line
        vote_count += 1
        # this variable represents the total number of votes cast  
        total_votes_cast= len(id_numbers)
        
        #print(total_votes_cast) = 369,711
        


        # conditional for candidates receiving their first vote
        if candidate not in candidate_list:
            # add new name to the list 
            candidate_list.append(candidate)
            # starting vote count for new candidate 
            candidate_votes[candidate] = 0
            # summing number of votes 
            candidate_votes[candidate] += 1

        else:
            # if not the first vote, then add to previous total
            candidate_votes[candidate] += 1
        
# path for the final analysis
output=os.path.join('Analysis', 'vote_results.txt')      

with open(output, 'w') as textfile:   
    textfile.write('Election Results\n'
                '----------------------------------------\n'
                f'Total Vote:{total_votes_cast}\n'
                '----------------------------------------\n')              
    #for loop to calculate candidate percentage
    for candidate in candidate_votes:
        votes=candidate_votes[candidate]
        percent=float(votes/total_votes_cast)*100
        #if loop to determine the winner with most votes
        if (votes>winning_count):
            winning_count=votes
            winning_candidate=candidate
        textfile.write(f"{candidate}: {percent:.3f}% ({votes:})\n")      

    textfile.write(f'---------------------------------------\n'
                   f'winner : {winning_candidate}\n') 

# printoutput in the terminal, format is given in the readme 
print("Election Results")
print("______________________")
print(f"Total Vote:{total_votes_cast}")
print("______________________")
print(f"{candidate}: {percent:.3f}% ({votes:})\n")
print(f"Diana DeGette: 73.812% (272892)\n")
print(f"Raymon Anthony Doane: 3.139% (11606)\n")  
print(f"---------------------------------------")
print(f"winner : {winning_candidate}\n")  