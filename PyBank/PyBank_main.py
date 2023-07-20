# PyBank main.py
import os
import csv

#Creating lsits to hold info 
Total_Months = 0
Value = 0
Profit_Loss = 0
Dates = []
Profits = []

#set path for the file
csvpath = os.path.join("PyBank", "Resources", "xbudget_data.csv")

#opening csv file
with open(csvpath, encoding = "UTF-8") as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ",")
    
    csvheader = next(csvreader)

    first_row = next(csvreader)
    
    Total_Months +=1
    
    Value = int(first_row[1])

    for row in csvreader:
        
        Dates.append(row[0])
        
        Change = int(row[1]) - Value
        
        Profits.append(Change)
        
        Value = int(row[1])
        
        Total_Months += 1

        Profit_Loss = Profit_Loss + int(row[1])

Greatest_Increase = max(Profits)

Greatest_List = Profits.index(Greatest_Increase)

Greatest_Date = Dates[Greatest_List]

Greatest_Decrease = min(Profits)

Lowest_List = Profits.index(Greatest_Decrease)

Lowest_Date = Dates[Lowest_List]

Average_Change = sum(Profits)/len(Profits)

print(f"Total Months: {str(Total_Months)}")  #This line used parts of code from attached GitHub in ReadME

print(f"Total: ${str(Profit_Loss)}")

print(f"Average Change: ${str(round(Average_Change,2))}")

print(f"Greatest Increase in Profits: {Greatest_Date} (${str(Greatest_Increase)})")

print(f"Greatest Decrease in Profits: {Lowest_Date} (${str(Greatest_Decrease)})")

Export_Path = os.path.join("PyBank", "Analysis", "results.txt")

with open(Export_Path, "w") as txt_file:

    txtwriter = csv.writer(txt_file)

    txtwriter.writerow(str(f"Total Months: {str(Total_Months)}"))

    txtwriter.writerow(str(f"Total $: {str(Profit_Loss)}"))

    txtwriter.writerow(str(f"Average Change: {str(round(Average_Change,2))}"))

    txtwriter.writerow(str(f"Greatest Increase in Profits: {Greatest_Date} (${str(Greatest_Increase)})"))

    txtwriter.writerow(str(f"Greatest Decrease in Profits: {Lowest_Date} (${str(Greatest_Decrease)})"))