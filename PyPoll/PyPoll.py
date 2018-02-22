import os
import csv

#define list for each column in the spreadsheet
voterIdList = []
countyList = []
candidateList = []
allCandidates = []

#define a dictionary to store the name and statistics of each candidate
candidates_dict = {}
candidates_winner = {}

#Read the excel file
poll1 = os.path.join("DataFiles", "election_data_2a.csv")

with open(poll1, newline="", encoding="utf8") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")

    #Exclude the first row
    next(csvreader, None)

    for row in csvreader:
        with open(poll1, newline="", encoding="utf8") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")

            # Exclude the first row
            next(csvreader, None)

            voterIdList.append(row[0])
            countyList.append(row[1])
            allCandidates.append(row[2])

            #Getting a list of UNIQUE candidate names
            #start off with an empty list and keep adding candidate names to the list. If the name is in candidateList then don't add it
            if row[2] not in candidateList:
                candidateList.append(row[2])

    tot_votes_cast = len(voterIdList) #Takes care of the question where Total Votes is being asked.

    #Loop thru the unique data set of candidates
    for i in range(len(candidateList)):
        #Counter for each candidates statistics. resets to zero as soon as the candidate name changes.
        cnt = 0
        for j in range(len(allCandidates)):
            if (candidateList[i] == allCandidates[j]):
                cnt = cnt + 1
                #Creating a dictionary, where the key is the name of the candidate
                #and the value is the percentage of votes the candidate got AND the total vote count for the candidate
                candidates_dict[candidateList[i]] = str((cnt/tot_votes_cast)*100) + "%" + " " + "(" + str(cnt) + ")"
                candidates_winner[candidateList[i]] = cnt
                #Anything to the left of the = sign i.e. [candidateList[i]] is the KEY of the dictionary
                #Anything to the right of the = sign i.e. str((cnt/tot_votes_cast)*100) + "%" + " " + "(" + str(cnt) + ")"
                #is the VALUE of the dictionary, making a KEY / VALUE pair


   #start dumping the results

    print("****Election Results****")
    print(" ")

    print("Total Votes cast: "+ str(tot_votes_cast))
    print("-------------------")
    print(" ")

    print("Participating Candidates")
    print("------------------------")
    for candidate in candidateList:
        print (candidate, end= " ")

    print(" ")
    print(" ")

    print("Candidate Stats")
    print("-----------------")
    for (k,v) in candidates_dict.items():
        print(k + ":", str(v))

    print(" ")
    print("Winner")
    print("------")
    maxval = 0
    for (k,v) in candidates_winner.items():
        if v > maxval:
            maxval = v
            winner = k
    print ("Winner is : "+ winner)
