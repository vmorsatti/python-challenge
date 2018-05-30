## Option 3: PyBoss

#![Boss](Images/boss.jpg)

#In this challenge, you get to be the _boss_. You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation. The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.

#Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. Your script will need to do the following:

#* Import the `employee_data1.csv` and `employee_data2.csv` files, which currently holds employee records like the below:


#```
#Emp ID,Name,DOB,SSN,State
#214,Sarah Simpson,1985-12-04,282-01-8166,Florida
#15,Samantha Lara,1993-09-08,848-80-7526,Colorado
#411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
#```

#* Then convert and export the data to use the following format instead:


#```
#Emp ID,First Name,Last Name,DOB,SSN,State
#214,Sarah,Simpson,12/04/1985,***-**-8166,FL
#15,Samantha,Lara,09/08/1993,***-**-7526,CO
#411,Stacy,Charles,12/20/1957,***-**-8526,PA
#```

#* In summary, the required conversions are as follows:

#  * The `Name` column should be split into separate `First Name` and `Last Name` columns.

#  * The `DOB` data should be re-written into `MM/DD/YYYY` format.

#  * The `SSN` data should be re-written such that the first five numbers are hidden from view.

#  * The `State` data should be re-written as simple two-letter abbreviations.

#* Special Hint: You may find this link to be helpful—[Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5).


# - MY_NOTES:____________________________________________
#   CREATE A NEW CSV FILE PER DATASET WITH NEW CONVERTED INFORMATION

#   FILE NAMES TO CONVERT:  
#      /Users/vernaorsatti/Downloads/UDEN201805DATA1-master 3/Week3 - Python/Python HW/PyBoss/raw_data/employee_data1.csv
#      /Users/vernaorsatti/Downloads/UDEN201805DATA1-master 3/Week3 - Python/Python HW/PyBoss/raw_data/employes_data2.csv

# Link to Create and Write to CSV files:   https://pythonspot.com/files-spreadsheets-csv/


# 
import os, csv


states_codes = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL','Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND','Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',  'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'} # sett

# Get Current working directory
current_dir = os.getcwd() # Get Current working directory
print(current_dir)

# - SETUP  Variables__________________________________________

#employee_data1_path = current_dir + "/" + "employee_data1.csv"
#employee_data2_path = current_dir + "/" + "employee_data2.csv"
#employee_data1 = "employee_data1.csv"
#employee_data2 = "employee_data2.csv"



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
                emp_id = row[0]
                #name split 
                first = row[1].split()[0]
                last = row[1].split()[1]
                # conver dob    
                
                yr = row[2].split("-")[0]
                mon = row[2].split("-")[1]
                day = row[2].split("-")[2]
                
                new_dob = (mon + "/" + day + "/" + yr)
                # Format SSN as ***-**-1234
                last4_ssn = row[3].split("-")[2]
                new_ssn = ("***-**-" + str(last4_ssn))
                # State name     
                state = row[4]
                print(state," i = ",i)
                state_code = states_codes[state]
                    
                

                new_row = [emp_id,first,last,new_dob,new_ssn,state_code]
                filewriter.writerow(new_row)


       
