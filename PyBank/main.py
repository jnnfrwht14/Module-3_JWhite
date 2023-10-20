#Import the modules
import os
import csv

#Creating an object out of the CSV file

csvpath = "Resources/budget_data.csv"

#Reading in the file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)


#Values
    Totalmonths = []
    ProfitLoss = []
    ProfitLossChanges = []
    TotalProfitLoss = 0
    GreatestIncProfitLossChanges = 0
    GreatestDecProfitLossChanges = 0
    GreatestIncProfitLossMonth = ''
    GreatestDecProfitLossMonth = ''

    for row in csvreader:
        Totalmonths.append(row[0])
        ProfitLoss.append(float(row[1]))
        ProfitLossChanges += float(row[1])

        #mins/maxes
    for x in range(1, len(ProfitLoss)):
        ProfitLossChanges.append(ProfitLoss[x] - ProfitLoss[x - 1])
        if (ProfitLoss[x] - ProfitLoss [x - 1]) > GreatestIncProfitLossChanges:
            GreatestIncProfitLossChanges = (ProfitLoss[x] - ProfitLoss[x - 1])
            GreatestIncProfitLossMonth = Totalmonths[x]
        if (ProfitLoss[x] - ProfitLoss [x - 1]) < GreatestDecProfitLossChanges:
            GreatestDecProfitLossChanges = (ProfitLoss[x] - ProfitLoss[x - 1])
            GreatestDecProfitLossMonth = Totalmonths[x]

            averageProfitLossChanges = round(
                sum(ProfitLossChanges) / len(ProfitLossChanges), 2)
            
        print("Financial Analysis")
        print("------------------")
        print("All Months: " + str(len(Totalmonths)))
        print("Total Revenue: " + '${:,.2f}'.format(TotalProfitLoss))
        print("Average Revenue Change: " + '${:,.2f}'.format(averageProfitLossChanges))
        print("Greatest Increase: " + str(GreatestIncProfitLossMonth) + 
              " " + '${:,.2f}'.format(GreatestIncProfitLossChanges))
        print("Greatest Decrease: " + str(GreatestDecProfitLossMonth) + 
              " " + '${:,.2f}'.format(GreatestDecProfitLossChanges))
        
        output = "py_bank_results.txt"
        with open(output, "w+") as file:
            file.write("Financial Analysis\n")
            file.write(" ----------------------------\n")
            file.write("Total Months: " + str(len(Totalmonths))+"\n")
            file.write("Total Revenue: " + '${:,.2f}'.format(TotalProfitLoss)+"\n")
            file.write("Average Revenue Change: " +
               '${:,.2f}'.format(averageProfitLossChanges)+"\n")
            file.write("Greatest Increase in Profits: " + str(GreatestIncProfitLossMonth) +
                    " " + '${:,.2f}'.format(GreatestIncProfitLossChanges)+"\n")
            file.write("Greatest Decrease in Profits: " + str(GreatestDecProfitLossMonth) +
               " " + '${:,.2f}'.format(GreatestDecProfitLossChanges)+"\n")

