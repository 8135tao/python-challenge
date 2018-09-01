import os
import csv

# define the average function, used to caculate the average in a list
def average(list):
    average =  sum(list)/len(list)
    return average



open_bank_csv = os.path.join("Resources", "budget_data.csv")

output_bank_csv = os.path.join("Output", "bank_report.csv")

with open(open_bank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)    


    bank_data = list(csvreader)


    enumerated_bankdata = list(enumerate(bank_data))
    row_count = 0
    net_total = 0


    #create a list to store the average change by using enumerate

    list_avgchange = [int(bankrow[1])-int(bank_data[i-1][1]) 
                      for i, bankrow in enumerated_bankdata][1:]
    # can also do the same using zip (more elegant!):  https://stackoverflow.com/questions/5314241/difference-between-consecutive-elements-in-list
    # list_raw = [int(bankrow[1]) for bankrow in bank_data]
    # list_avgchange = [j-i for i,j in zip(list_raw,list_raw[1:])]
    
    list_avgchange.insert(0,-100000000.00)

    average_change = average(list_avgchange[1:])    
    max_change = max(list_avgchange[1:])
    min_change = min(list_avgchange[1:])
    max_index = list_avgchange.index(max_change)
    min_index = list_avgchange.index(min_change)
    for i,bankrow in enumerated_bankdata:
        row_count +=1         
        net_total += int(bankrow[1])


    # create the list of things to report.
    reports = [
        "Total number of months: " + str(row_count), 
        "Total: " + str("${:10.2f}".format(net_total)),
        "Greatest increase in profits at: " +bank_data[max_index][0] +" (" +str("${:10.2f}".format(max_change)) +")",
        "Greatest decrease in profits at: " +bank_data[min_index][0] +" (" +str("${:10.2f}".format(min_change)) +")",
        f"Average change: ${average_change:.2f}"
      ]

    print("Financial Analysis \n")
    print("-------------------------------- \n")
    print(*reports, sep = "\n")


# can also output not using the csv class
# with open(output_bank_csv,"w", newline="") as export:
#     export.write("Financial Analysis\n")
#     export.write("--------------------------\n")

#     for report in reports:
#         export.write("{}\n".format(report))

with open(output_bank_csv,"w", newline="") as outputfile:        
    csvwriter = csv.writer(outputfile, lineterminator='\n')

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["---------------------------"])
    
    for report in reports:
        csvwriter.writerow([report])