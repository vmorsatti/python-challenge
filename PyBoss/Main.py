# Main.py in PyBoss
# Authored by Verna Orsatti May 2018 for University of Denver: DataAnalytics Bootcamp

# PRE-DEFINED ASSIGNMENT INSTRUCTIONS:
#In this challenge, you get to be the _boss_. You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation. The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.
#Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. Your script will need to do the following:

#* Import the `employee_data1.csv` and `employee_data2.csv` files, which currently holds employee records like the below:

#Emp ID,Name,DOB,SSN,State
#214,Sarah Simpson,1985-12-04,282-01-8166,Florida
#15,Samantha Lara,1993-09-08,848-80-7526,Colorado
#411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania

#* Then convert and export the data to use the following format instead:

# Emp ID,First Name,Last Name,DOB,SSN,State
# 214,Sarah,Simpson,12/04/1985,***-**-8166,FL
# 15,Samantha,Lara,09/08/1993,***-**-7526,CO
# 411,Stacy,Charles,12/20/1957,***-**-8526,PA

#* In summary, the required conversions are as follows:

#  * The `Name` column should be split into separate `First Name` and `Last Name` columns.
#  * The `DOB` data should be re-written into `MM/DD/YYYY` format.
#  * The `SSN` data should be re-written such that the first five numbers are hidden from view.
#  * The `State` data should be re-written as simple two-letter abbreviations.

# - AUTHOR'S (Verna) NOTES:____________________________________________
#   CREATE A NEW CSV FILE PER DATASET WITH NEW CONVERTED INFORMATION

#   ONE TIME FILE NAMES TO CONVERT - FILES MUST BE IN CURRENT DIRECTORY AS SCRIPT:  
#      employee_data1.csv  ->  conv_employee_data1.csv
#      employes_data2.csv  ->  conv-employee_data2.csv

import os, csv

states_codes = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL','Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND','Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',  'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'} # sett

# Get Current working directory
current_dir = os.getcwd() 
print(current_dir) # Display for user help

# - SETUP  Variables__________________________________________

old_header = ['Emp ID', 'Name', 'DOB', 'SSN', 'State'] # tested file original file and headers match
new_header = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']

files_r = ['employee_data1.csv', 'employee_data2.csv'] # read original files
files_w = ['conv_employee_data1.csv','conv_employee_data2.csv'] # write original files

for i in range(0,2):
    print("i in range = ",i)
    with open(files_w[i],"w") as fw:
        filewriter = csv.writer(fw, delimiter=',')
        filewriter.writerow(new_header) 
        #print(files_r[i])
        #print(files_w[i])
        with open(files_r[i],"r") as fr:    
            reader = csv.reader(fr, delimiter=',')
            next(reader)
            for row in reader:
                    # id - no change
                emp_id = row[0]
                    #name split 
                first = row[1].split()[0]
                last = row[1].split()[1]   
                    # Date of birth reformat
                yr = row[2].split("-")[0]
                mon = row[2].split("-")[1]
                day = row[2].split("-")[2]
                new_dob = (mon + "/" + day + "/" + yr)
                    # Format SSN as ***-**-1234
                last4_ssn = row[3].split("-")[2]
                new_ssn = ("***-**-" + str(last4_ssn))
                    # State name to state    
                state = row[4]
                state_code = states_codes[state]
                    # Display progress to let user know that it's working
                print("Processing employee ID: ", row[0],"  ",row[1]," in file ",files_r[i])
                    # Write to new
                new_row = [emp_id,first,last,new_dob,new_ssn,state_code]
                filewriter.writerow(new_row)

print()
print("Your new file files are ready and are named:")
print(files_w[0],"  ",files_w[1])
print()
print("The new files are located in the directory: ")
print(current_dir)
print()

# "Error is not a fault of our knowledge, 
# but a mistake of our judgment giving assent to that which is not true."
# --John Locke
       
       
