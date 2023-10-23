import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#Lists to store data
VotesCast = 0
Candidates = []
NameCandidate = []
PercentageWon = []
NumberofVotes = []

#read the csv
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        print(csvreader)
        csv_header = next(csvreader)
        print(csv_header)

        for row in csvreader:
            VotesCast = VotesCast + 1
            Candidates.append(row[2])

        for d in set(Candidates):
            NameCandidate.append(d)
            k = Candidates.count(d)
            NumberofVotes.append(k)
            g = (k/VotesCast)*100
            PercentageWon.append(g)
#Calculate winner
        WinnerCount = max(NumberofVotes)    
        Winner = NameCandidate[NumberofVotes.index(WinnerCount)]

#print results
        print("Election Results")
        print("----------------")
        print("Total Votes: " +str(VotesCast))
        for i in range(len(NameCandidate)):
            print(NameCandidate[i] + ": " 
                  +str(round(PercentageWon[i],3)) +"% (" 
                  +str(NumberofVotes[i])+ ")")
        print("----------------")
        print("Winner: "+Winner)
        print("----------------")

#create output file
        output = "Election_Results.txt"
        with open(output,"w+") as file:
               file.write("Election Results\n")
               file.write("----------------\n")
               file.write("Total Votes: " +str(VotesCast) + "\n")
               file.write("----------------\n")
               for i in range(len(NameCandidate)):
                 file.write(NameCandidate[i] + ": " 
                            +str(round(PercentageWon[i],3)) +"% (" 
                            +str(NumberofVotes[i])+ ")\n")
               file.write("----------------\n")
               file.write("Winner: " +Winner + "\n")
               file.write("----------------\n")