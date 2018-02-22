import os
import csv

which_file = input("Which file do you want to adjust - employee_data1.csv  OR employee_data2.csv : ")
print("OK, please note that the output file will be in folder Datafiles(pyboss_output1.csv)")
boss = os.path.join("DataFiles", which_file)

#States Dictionary to convert state to abbreviated format e.g. output Florida as FL
dict_states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

#define all the lists to gather data from original spreadsheet.
empID = []
fname = []
lname = []
dob = []
ssn = []
state = []

#define functions to take care of repetitive work
def appendparams(param1, param2, param3, separator):
    retstr = str(param1) + separator + str(param2) + separator + str(param3)
    return retstr

def concatparams(param1, param2):
    return(str(param1 + str(param2)))

with open(boss, newline="", encoding="utf8") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")

    #Exclude the first row
    next(csvreader, None)

    for row in csvreader:

        empID.append(row[0])

        splitname = row[1].split(" ")
        fname.append(splitname[0])
        lname.append(splitname[1])

        splitdob = row[2].split("-")
        dd = splitdob[2]
        mm = splitdob[1]
        yyyy = splitdob[0]

        r = appendparams(str(dd), str(mm), str(yyyy), '/')
        #dob.append(str(dd) + "/" + str(mm) + "/" + str(yyyy))
        dob.append(r)

        ssn_str = row[3]
        str1 = '***-**-'
        #output_ssn_str = str1 + ssn_str[7:11]
        output_ssn_str = concatparams(str1, ssn_str[7:11])

        ssn.append(output_ssn_str)

        for (k,v) in dict_states.items():
            if row[4] in v:
                abbrev_state = k

        state.append(abbrev_state)

    #print(empID)
    #print(fname)
    #print(lname)
    #print(dob)
    #print(ssn)
    #print(state)

    #Zip all lists
    final = zip(empID, fname, lname, dob, ssn, state)

    #Start writing output
    output_file = os.path.join("DataFiles", "pyboss_output1.csv")

    #  Open the output file
    with open(output_file, "w", newline="") as datafile:
        writer = csv.writer(datafile, delimiter=',')

        # Write the header row
        writer.writerow(["Employeee ID", "First Name", "Last Name", "DateOfBirth","maskedSSN", "State"])

        for finalrows in final:
            writer.writerow(finalrows)

