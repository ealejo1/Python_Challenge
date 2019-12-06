# List all dependencies:
import csv
import os


# Determine the files to load and output. 
file_to_load = os.path.join("election_data.csv")
file_to_output = os.path.join("election_analysis.txt")

total_votes = 0
number_candidates = 0
candidate_list = []
candidate_votes = {}
max_votes = -1

# Read the csv file and convert it into a list of dictionaries.
with open(file_to_load) as poll_data:
    reader = csv.DictReader(poll_data)
    
    for row in reader:
        current_candidate = row['Candidate']
        if current_candidate not in candidate_list:
            number_candidates = number_candidates + 1
            candidate_list.append(current_candidate)
            candidate_votes[current_candidate] = 0
            
        candidate_votes[current_candidate]=candidate_votes[current_candidate] + 1
        total_votes = total_votes + 1
        
        if candidate_votes[current_candidate] > max_votes :
            max_votes = candidate_votes[current_candidate]
            max_candidate = current_candidate


# Determine Election Results, including election winner. 


line1 = '  Election Results'
line2 = '  -------------------------'
line3 = ('  Total Votes: %d' %(total_votes))
line4 = '  -------------------------'
output = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4

for name in candidate_list :
    linex = ('  %s: %.3f%% (%d)' %(name,  100*candidate_votes[name]/(0.0+total_votes), candidate_votes[name]))
    output = output + '\n' + linex

output = output + '\n' + '  -------------------------'
output = output + '\n' + ('  Winner: %s' %max_candidate)
output = output + '\n' + '  -------------------------'

print(output)
with open(file_to_output,'w') as outputfile:
        outputfile.write(output)
