#PyPoll main

import os
import csv

Total_Vote = 0
Canidate_Votes = []
Canidate_Percent_Vote = []
Canidates = []
Winner = []

csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(csvpath, encoding= "UTF-8") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter= ",")
    
    csvheader = next(csvreader)

    for row in csvreader:
        
        Total_Vote += 1

        if row[2] not in Canidates:
            Canidates.append(row[2])
            
            index = Canidates.index(row[2])

            Canidate_Votes.append(1)
        else:
            index = Canidates.index(row[2])

        Canidate_Votes[index] +=1

    for votes in Canidate_Votes:
        
        Percent_of_Votes = (votes/Total_Vote) * 100  #This line used parts of code from attached GitHub in ReadME
                
        Canidate_Percent_Vote.append(Percent_of_Votes)

    Winner_Votes = max(Canidate_Votes)
    
    index = Canidate_Votes.index(Winner_Votes)
    
    Winner = Canidates[index]

print(f"Total Votes: {str(Total_Vote)}")
    
for i in range(len(Canidates)):  #This line used parts of code from attached GitHub in ReadME
    
    print(f"{Canidates[i]}: {str(Canidate_Percent_Vote[i])} ({str(Canidate_Votes[i])})")

print(f"Winner: {Winner}") 

Export_Path = os.path.join("PyPoll", "Analysis", "results.txt")

with open(Export_Path, "w") as txt_file:

    txtwriter = csv.writer(txt_file)

    txtwriter.writerow(str(f"Total Votes: {str(Total_Vote)}"))

    for i in range(len(Canidates)): #This line used parts of code from attached GitHub in ReadME
        txtwriter.writerow(str(f"{Canidates[i]}: {str(Canidate_Percent_Vote[i])} ({str(Canidate_Votes[i])})"))

    txtwriter.writerow(str(f"Winner: {Winner}"))
    
