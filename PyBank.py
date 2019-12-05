#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Py Bank
#Dependencies
import csv
import os

#Load Files & Output Files
file_to_load = os.path.join("budget_data.csv")
file_to_output = os.path.join("budget_analysis.txt")

#Keep track of various financial parameters.
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999999999999999999]
total_net = 0

# Read CSV file and convert into a list of dictionaries. 
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    
    # Read header row:
    header = next(reader)
    # print(header)
    
    # Extract first row to avoid appending net_change_list
    first_row = next(reader)
    # print(first_row)
    total_months = total_months + 1
    
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])
    # print(total_net)
    # print(prev_net)
    
    # print("Loop begins here:")
    #Loop through data.
    for row in reader:
        
        #Track total:
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        print(total_net)
        
        #Track net change:
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]
        #print net_change_list
        #print months_of_change
        
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
       
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
            
       # Calculate Average Net Change
        net_monthly_avg = sum(net_change_list) / len(net_change_list)
        
        output = (
            f"\nFinancial Analysis\n"
            f"======================"
            f"Total Months: {total_months}\n"
            f"Total: ${total_net}\n"
            f"Average Change: ${net_monthly_avg:.2f}\n"
            f"Greatest Increase in Profits {greatest_increase[0]}, (${greatest_increase[1]})\n"
            f"Greatest Decrease in Profits {greatest_decrease[0]}, (${greatest_decrease[1]})\n"    
        )
        
        print(output)
        
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
      


# In[ ]:





# In[ ]:




