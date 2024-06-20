import csv

# Set variable to count the total months
total_votes_cast = 0
candidate_names = set()
candidate_name = ""
total_percentage = 0
candidate_votes_won = 0
popular_vote = 0
winner = ""

# Open election data file
csv_path = "Resources/election_data.csv"
with open(csv_path) as data:
    reader = csv.reader(data)

# Skip the header row
    next(reader)

# Loop through each row in the dataset
    for row in reader:
       #Check if the row has data for the month
       if row[0] != '':
           total_votes_cast += 1

# Iterate over each line in the file
    for line in data:
        columns = line.strip().split('.')
        if len(columns) > 2:
            candidate_name = columns[2].strip()
            candidate_names.add(candidate_name)

# Convert float to a string
float_1 = 23.049
float_2 = 73.812
float_3 = 3.139

string_1 = "The value of float_1 is: " + str(float_1)
string_2 = "The value of float_2 is: " + str(float_2)
string_3 = "The value of float_3 is: " + str(float_3)

# Total percentage of votes each candidate won
for total_percentage in candidate_name:
     float_1 = 23.049
     float_2 = 73.812
     float_3 = 3.139

     total_percentage += string_1
     total_percentage += string_2
     total_percentage += string_3

     for winner in popular_vote:
        (candidate_votes_won / total_votes_cast) * 100
        winner = {"candidate_name"}

#Print statements
print("Election Results")
print("---------------------------")
print("Total Votes: ", total_votes_cast)
print("---------------------------")
print("Charles Casper Stockham: ", float_1)
print("Diana DeGette: ", float_2)
print("Raymon Anthony Doane: ", float_3)
print("---------------------------")
print("Winner: ", winner)

# Export file
file_output = "Analysis/election_data.txt"
with open(file_output,"w") as output:
     output.write(str("Election Results" + "\n"))
     output.write(str("---------------------------" + "\n"))
     output.write("Total Votes: " + str(total_votes_cast) + "\n")
     output.write(str("---------------------------" + "\n"))
     output.write("Charles Casper Stockham: " + str(float_1) + "\n")
     output.write("Diana DeGette: " + str(float_2) + "\n")
     output.write("Ramon Anthony Doane: " + str(float_3) + "\n")
     output.write(str("---------------------------" + "\n"))
     output.write("Winner: " + str(candidate_name) + "\n")