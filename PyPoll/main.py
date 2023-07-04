import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "election_data.csv")

# Specify the file to write to
output_path = os.path.join("Analysis", "new.txt")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    charles_votes = 0
    charles = "Charles Casper Stockham"
    diana_votes = 0
    diana = "Diana DeGette"
    raymon_votes =0
    raymon = "Raymon Anthony Doane"

    for row in csvreader:

        if charles == row[2]:
            charles_votes = charles_votes + 1
        elif diana == row[2]:
            diana_votes = diana_votes + 1
        else:
            raymon_votes = raymon_votes + 1
        total_votes = charles_votes + diana_votes + raymon_votes

        charles_percent = (charles_votes/total_votes) * 100
        charles_percent_rd = round(charles_percent, 3)
        diana_percent = (diana_votes/total_votes) * 100
        diana_percent_rd = round(diana_percent, 3)
        raymon_percent = (raymon_votes/total_votes) * 100
        raymon_percent_rd = round(raymon_percent, 3)


#print output
print('Election Results')
print('--------------------')
print(f'Total Votes: {total_votes}')
print('--------------------')
print(f'{charles}: {charles_percent_rd}% ({charles_votes})')
print(f'{diana}: {diana_percent_rd}% ({diana_votes})')
print(f'{raymon}: {raymon_percent_rd}% ({raymon_votes})')   
print('--------------------')
if charles_votes > (diana_votes or raymon_votes):
    print(f'Winner: {charles}')
elif diana_votes > (charles_votes or raymon_votes):
    print(f'Winner: {diana}')
else:
    print(f'Winner: {raymon}')
print('--------------------')

#write output to a new text file
with open(output_path, 'w') as f:
    f.write('Election Results\n')
    f.write('-----------------------\n')
    f.write(f'Total Votes: {total_votes}\n')
    f.write(f'-----------------------\n')
    f.write(f'{charles}: {charles_percent} ({charles_votes})\n')
    f.write(f'{diana}: {diana_percent} ({diana_votes})\n')
    f.write(f'{raymon}: {raymon_percent} ({raymon_votes})\n')
    f.write(f'-----------------------\n')
    if charles_votes > (diana_votes or raymon_votes):
        f.write(f'Winner: {charles}\n')
    elif diana_votes > (charles_votes or raymon_votes):
        f.write(f'Winner: {diana}\n')
    else:
        f.write(f'Winner: {raymon}\n')
    f.write(f'-----------------------\n')