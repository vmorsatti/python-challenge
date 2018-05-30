# Verna_PyBank.py - Analyze financial records for the company. 
#  
# 2 sets of revenue data: 
# budget_data_1.csv  note that date form is Nov-12; Jeff said not to reformat 
# budget_data_2.csv  note that date form is 2-16; Jeff said not to reformat

#Task is to create a Python script that analyzes the records to calculate each of the following:

#   The total number of months included in THE dataset 
#   The total amount of revenue gained over the entire period
#   The average change in revenue between months over the entire period
#   The greatest increase in revenue (date & amount) over the entire period
#   The greatest decrease in revenue (date & amount) over the entire period

# NOTE:  Final script must be able to handle any such similarly structured dataset in the future 
# (your boss is going to give you more of these -- so your script has to work for the ones to come). 
# In addition, your final script should both print the analysis to the terminal 
# and export a text file with the results.

# NOTE   *** This refers the the dataset for getting report figures, and does not indicate anywhere 
#            that the datasets should be combined.

#READme by Verna
# This program is designed for input from the user to enter the file pathname of the csv file and expects 
# the user to provide the proper file format of a CSV

# User will >> enter csv file path name 
#   - error handling is included to verify file existance 
#   - code is supplie do verify file type is .csv file
# User will >> enter the desired path of the directory for the report file 
#   - error handling is included to verify the path is valid
#   - code is supplied to strip the '/' from the directory if entered for consistancy 
# User will >> enter a new .txt file name for the report created
#   - error handling is included to file doesn't already exist in the selected directory
#   - code is supplied to verify file name is a .txt file name

# Get Tools_______________________________
import os
import os.path
import csv
# from collections import defaultdict # not sure need this except for append function

# Get file_path_name_________________________
print()
print("This is PyBank - your Budget Analyzer")
print("You will need the following to proceed:")
print("    1) The full path name for the CSV dataset that you wish to analyze.")
print("    2) The path name of the directory that you want your report saved to.")
print("    2) The .txt file name you want to create for your report.")
print()

# Data Set file paths to cut and paste from my system for testing_______________
#    /Users/vernaorsatti/Documents/Bootcamp/Bootcamp Assignments/#3 Homework Assignment/budget_data_1.csv
#    /Users/vernaorsatti/Documents/Bootcamp/Bootcamp Assignments/#3 Homework Assignment/budget_data_2.csv

# Get valid csv file full path name from user__________________
file_test = "n"
while file_test == "n":
    budget_csv_path = input("Please enter the full file path name of the data set you wish to analyze: ")
    # make sure file exists, else show an error
    if (not os.path.isfile(budget_csv_path)): # file path verification
        print()
        print("Error: File not found. Please re-enter!" )
        print()
        file_test = "n"
    else:
        file_test = "y"
        
    if file_test == "y" :
        filename, file_extension = os.path.splitext(budget_csv_path)
        if (file_extension == ".csv"):
            print()
            print("You have entered a valid CSV file ")
            print(budget_csv_path)
            print()
        else:
            print()
            print("That was not a valid .CSV file, please try again!")
            print()
            file_test = "n"

# Get directory name from user________________________
dir_test = "n" 
while dir_test == "n":
    export_dir_path = input("Please enter the directory path name that you wish to save your report to: ")
    if export_dir_path.endswith('/'):
        export_dir_path = export_dir_path[:-1] # strip ending slash if present
    # check for valid directory
    # make sure does exist, else show an error
    if (not os.path.isdir(export_dir_path)): # dir path verification
        print()
        print("Entry Error: Directory does NOT exist. Please re-enter!" )
        print()
        dir_test = "n"
    else:
        dir_test = "y"

# Get report file name as a .txt file from user____________  
name_test = "n"     
while name_test == "n":
    report_name = input("Please enter a new .txt file name to save your report to: ")
    report_path_name = (export_dir_path + "/" + report_name)
    print()
   
    # make sure file does not exist, else show an error
    if os.path.isfile(report_path_name): # file path verification
        print()
        print("Entry Error: File already exists. Please re-enter!" )
        print()
        name_test = "n"
    else:
        name_test = "y"
        
    if name_test == "y":
        filename, file_extension = os.path.splitext(report_path_name)
        if (file_extension == ".txt"):
            print()
            print("You have entered a valid .txt file: ")
            print()
        else:
            print()
            print("That was not a valid .txt file, please try again!")
            print()
            name_test = "n"  

# Create writable file before running report 
#   & interact with user to note filename__________________________
f= open(report_path_name,"w+")
print("You have created your report file name as: ")
print(report_path_name)
print()
answer = input("Please note your file name.  Press any key to proceed! ")

# Munch data for report_______________________________________
with open(budget_csv_path) as f:
    reader = csv.reader(f)
    next(reader)
    data = list(reader)
    #row_count = sum(1 for row in data) 
    first_read = "y"
    total_revenue_gain = 0
    change_sum = 0
    amt1 = 0
    amt2 = 0
     
    for row in data:
        rev_amt = eval(row[1])
        total_revenue_gain += rev_amt  # is working 
        amt2 = rev_amt # is working
        if first_read == "y":
            max_increase_amt = rev_amt
            max_decrease_amt = rev_amt
            max_increase_dates = row[0]
            max_decrease_dates = row[0]
            amt1 = amt2
            first_read = "n"
        else:
            change_amt = amt2 - amt1
            if change_amt > max_increase_amt:
                max_increase_amt = change_amt
                max_increase_dates = row[0]
            elif change_amt == max_increase_amt:
                max_increase_amt = max_increase_amt
                # max_increase_dates.append(row[0])
            else:
                max_increase_amt = max_increase_amt

            if change_amt < max_decrease_amt:
                max_decrease_amt = change_amt
                max_decrease_dates = row[0]
            elif change_amt == max_decrease_amt:
                max_decrease_amt = max_decrease_amt
                #max_decrease_dates.append(row[0])
            else:
                max_decrease_amt = max_decrease_amt

            change_sum += change_amt
            row.append(change_amt) # just for display to cross test data in excel
            amt1 = amt2
        

# Original data Tuples [['Oct-12', '1154293'], ['Nov-12', '885773'], ['Dec-12', '-448704'], ['Jan-13', '563679'], ['Feb-13', '555394'], ['Mar-13', '631974'], ['Apr-13', '957395'], ['May-13', '1104047'], ['Jun-13', '693464'], ['Jul-13', '454932'], ['Aug-13', '727272'], ['Sep-13', '125016'], ['Oct-13', '339251'], ['Nov-13', '78523'], ['Dec-13', '977084'], ['Jan-14', '1158718'], ['Feb-14', '332681'], ['Mar-14', '-341227'], ['Apr-14', '173826'], ['May-14', '742611'], ['Jun-14', '1189806'], ['Jul-14', '607363'], ['Aug-14', '-1172384'], ['Sep-14', '587993'], ['Oct-14', '295198'], ['Nov-14', '-300390'], ['Dec-14', '468995'], ['Jan-15', '698452'], ['Feb-15', '967828'], ['Mar-15', '-454873'], ['Apr-15', '375723'], ['May-15', '1140526'], ['Jun-15', '83836'], ['Jul-15', '413189'], ['Aug-15', '551363'], ['Sep-15', '1195111'], ['Oct-15', '657081'], ['Nov-15', '66659'], ['Dec-15', '803301'], ['Jan-16', '-953301'], ['Feb-16', '883934']]
# Appended data with revenue change data [['Jan-2009', '943690'], ['Feb-2009', '1062565', 118875], ['Mar-2009', '210079', -852486], ['Apr-2009', '-735286', -945365], ['May-2009', '842933', 1578219], ['Jun-2009', '358691', -484242], ['Jul-2009', '914953', 556262], ['Aug-2009', '723427', -191526], ['Sep-2009', '-837468', -1560895], ['Oct-2009', '-146929', 690539], ['Nov-2009', '831730', 978659], ['Dec-2009', '917752', 86022], ['Jan-2010', '800038', -117714], ['Feb-2010', '1117103', 317065], ['Mar-2010', '181220', -935883], ['Apr-2010', '120968', -60252], ['May-2010', '844012', 723044], ['Jun-2010', '307468', -536544], ['Jul-2010', '502341', 194873], ['Aug-2010', '-748679', -1251020], ['Sep-2010', '-1063151', -314472], ['Oct-2010', '111367', 1174518], ['Nov-2010', '889322', 777955], ['Dec-2010', '1028794', 139472], ['Jan-2011', '-705201', -1733995], ['Feb-2011', '457393', 1162594], ['Mar-2011', '358440', -98953], ['Apr-2011', '110092', -248348], ['May-2011', '1111337', 1001245], ['Jun-2011', '691712', -419625], ['Jul-2011', '669603', -22109], ['Aug-2011', '527608', -141995], ['Sep-2011', '1057492', 529884], ['Oct-2011', '109267', -948225], ['Nov-2011', '1106492', 997225], ['Dec-2011', '531744', -574748], ['Jan-2012', '1134360', 602616], ['Feb-2012', '-401260', -1535620], ['Mar-2012', '1141606', 1542866], ['Apr-2012', '594289', -547317], ['May-2012', '51905', -542384], ['Jun-2012', '415204', 363299], ['Jul-2012', '467130', 51926], ['Aug-2012', '270918', -196212], ['Sep-2012', '589902', 318984], ['Oct-2012', '1056793', 466891], ['Nov-2012', '250079', -806714], ['Dec-2012', '91344', -158735], ['Jan-2013', '431100', 339756], ['Feb-2013', '801964', 370864], ['Mar-2013', '50115', -751849], ['Apr-2013', '525242', 475127], ['May-2013', '55136', -470106], ['Jun-2013', '-497774', -552910], ['Jul-2013', '360731', 858505], ['Aug-2013', '391243', 30512], ['Sep-2013', '339680', -51563], ['Oct-2013', '809253', 469573], ['Nov-2013', '924494', 115241], ['Dec-2013', '998347', 73853], ['Jan-2014', '-524902', -1523249], ['Feb-2014', '747765', 1272667], ['Mar-2014', '197783', -549982], ['Apr-2014', '131625', -66158], ['May-2014', '1016992', 885367], ['Jun-2014', '-930753', -1947745], ['Jul-2014', '714387', 1645140], ['Aug-2014', '201005', -513382], ['Sep-2014', '655535', 454530], ['Oct-2014', '845108', 189573], ['Nov-2014', '101736', -743372], ['Dec-2014', '-93063', -194799], ['Jan-2015', '984921', 1077984], ['Feb-2015', '-362343', -1347264], ['Mar-2015', '940457', 1302800], ['Apr-2015', '216399', -724058], ['May-2015', '363036', 146637], ['Jun-2015', '672160', 309124], ['Jul-2015', '783533', 111373], ['Aug-2015', '1079882', 296349], ['Sep-2015', '288933', -790949], ['Oct-2015', '894500', 605567], ['Nov-2015', '411593', -482907], ['Dec-2015', '789575', 377982], ['Jan-2016', '355838', -433737], ['Feb-2016', '437489', 81651]]

# Define some things for the report________________________
row_count = sum(1 for row in data) 
ave_rev_change = round(change_sum / (row_count - 1),0)
#   Note: For the following strings: this method of creating a string to print was cosmetic &
#       intentional to mimic the sample for how the sample looks for formatting amounts.
#       Other inline printing produces spaces inside the ()s and other.
max_inc = ("Greatest Increase in Revenue: " + max_increase_dates + " ($" + str(max_increase_amt) + ")")
max_dec = ("Greatest Decrease in Revenue: " + max_decrease_dates + " ($" + str(max_decrease_amt) + ")")
tot_rev = ("Total Revenue: $" + str(total_revenue_gain))
ave_rev = ("Average Revenue Change: $" + str(int(ave_rev_change)))

# Print the Analysis to the terminal____________________
print()
print("Financial Analysis")
print("---------------------")
print("Total Months:",row_count)
print(tot_rev)
print(ave_rev)
print(max_inc)
print(max_dec)

# Print report to display_______________________________
line_1 = ("Financial Analysis" + '\n')
line_2 = ("______________________" + '\n')
line_3 = ("Total Months: " + str(row_count) + '\n') 
line_4 = ("Total Revenue: $" + str(total_revenue_gain) + '\n')
line_5 = ("Average Revenue Change: $" + str(int(ave_rev_change)) + '\n')
line_6 = ("Greatest Increase in Revenue: " + max_increase_dates + " ($" + str(max_increase_amt) + ")" + '\n')
line_7 = ("Greatest Decrease in Revenue: " + max_decrease_dates + " ($" + str(max_decrease_amt) + ")" + '\n')
print()

# Write report to user-selected text file________________
file = open(report_path_name,'w')
file.write(line_1)
file.write(line_2)
file.write(line_3)
file.write(line_4)
file.write(line_5)
file.write(line_6)
file.write(line_7)

file.close()
