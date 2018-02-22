import os
import csv

#Since there are two spreadsheets , ask user which spreadsheet needs to be analyzed.

file_to_analyze = input("Which file do you want to analyze, budget_data_1.csv or budget_data_2.csv ?")
print("Ok, analyzing " + file_to_analyze)
print()

#budget = os.path.join("DataFiles", "budget_data_2.csv")
budget = os.path.join("DataFiles", file_to_analyze)

#initialize and declare section
tot_months = 0
tot_revenue = 0
avg_revenue_chg = 0
datesList = []
revenueList = list()
changeRevenueList = []
changeDateList = []

#####################READ the source file#####################################
with open(budget, newline="", encoding="utf8") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        #take the date from the CSV file and add it to lists
        #One list for dates , one list for revenue
        datesList.append(row[0])
        revenueList.append(row[1])

    #tot_months = tot_months + 1
    tot_months = len(datesList)
    #tot_revenue = tot_revenue + int(row[1])
    tot_revenue = sum(int(i) for i in revenueList)

    #To calculate the average change in revenue between months , loop thru the revenue list created above
    #and populate a new list called changeRevenueList with the difference of the next months revenue and the
    #current month revenue, (i+1) - i.
    #In addition populate a changeDate list with the next months date(i+1) date. We will use this date to flag the max and min
    #change revenues.
    for i in range(len(revenueList) - 1):
    #for i in range(5):
        changeRevenueList.append(int(revenueList[i+1]) - int(revenueList[i]))
        changeDateList.append(datesList[i+1])

    #The average revenue change will be the sum of the elements in changeRevenueList divided by the
    #number of elements in the changeRevenueList
    avg_revenue_chg = (sum(int(i) for i in changeRevenueList)) / len(changeRevenueList)
    #get the maximum value in chnage RevenueList
    max_avg_revenue = max(changeRevenueList)
    #Get the index of the max_avg_revenue
    max_avg_revenue_idx = changeRevenueList.index(max_avg_revenue)
    #Use the index of max average revenue to get the date at the same index
    max_avg_revenue_date = changeDateList[max_avg_revenue_idx]

    # get the minimum value in change RevenueList
    min_avg_revenue = min(changeRevenueList)
    # Get the index of the min_avg_revenue
    min_avg_revenue_idx = changeRevenueList.index(min_avg_revenue)
    # Use the index of min average revenue to get the date at the same index
    min_avg_revenue_date = changeDateList[min_avg_revenue_idx]

    #### Debug statements ####
    #print(max_avg_revenue)
    #print(max_avg_revenue_idx)
    #print(max_avg_revenue_date)

    #print(datesList)
    #print(revenueList)
    #print(changeRevenueList)
    #print(changeDateList)
    #print(len(changeRevenueList))
    #print(len(changeDateList))


print("Final Analysis")
print("---------------")
print("Total Months : " + str(tot_months))
print("Total Revenue: " + "$"+ str(tot_revenue))
print("Average Revenue Change: "+ "$"+ str(avg_revenue_chg))
print("Greatest Increase in Revenue: " + max_avg_revenue_date + " $(" + str(max_avg_revenue) + ")")
print("Greatest Decrease in Revenue: " + min_avg_revenue_date + " $(" + str(min_avg_revenue) + ")")

######################WRITE output#########################
output_file = os.path.join("DataFiles", "final_analysis.csv")
print("A copy of the analysis is in : " + output_file)

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile, delimiter=',')
    
    # Write the header row
    writer.writerow(["Total Months", "Total Revenue", "Average Revenue Change", "Greatest Increase in Revenue",
                     "Greatest Decrease in Revenue"])

    writer.writerow([str(tot_months),
                    str(tot_revenue),
                    str(avg_revenue_chg),
                    max_avg_revenue_date + " $(" + str(max_avg_revenue) + ")",
                    min_avg_revenue_date + " $(" + str(min_avg_revenue) + ")"])