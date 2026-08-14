from Data_Models.Subject_Model import Subject
from Data_Models.Diff_Model import Difficulty
from Data_Models.Saving_Model import Databasesys
from Data_Models.Review_Model import ReviewSystem
from Data_Models.Log_Model import LogSystem
import csv
from Data_Models.Diff_Model import Difficulty
from pprint import pprint

subjects = {
    "Algorithms": {
        "10:30 - 10.07.2026": Difficulty.Blue,
        "14:45 - 20.07.2026": Difficulty.Green,
        "09:15 - 25.07.2026": Difficulty.Red,
    },

    "Databases": {
        "11:00 - 11.07.2026": Difficulty.Green,
        "16:20 - 19.07.2026": Difficulty.Yellow,
        "13:40 - 27.07.2026": Difficulty.Blue,
    },

    "Operating Systems": {
        "08:45 - 12.07.2026": Difficulty.Red,
        "12:30 - 22.07.2026": Difficulty.Yellow,
        "18:10 - 01.08.2026": Difficulty.Green,
    },

    "Computer Networks": {
        "15:15 - 13.07.2026": Difficulty.Blue,
        "10:25 - 23.07.2026": Difficulty.Green,
        "17:50 - 02.08.2026": Difficulty.Yellow,
    },

    "Linear Algebra": {
        "09:30 - 14.07.2026": Difficulty.Yellow,
        "14:10 - 24.07.2026": Difficulty.Red,
        "11:45 - 03.08.2026": Difficulty.Green,
    },

    "Calculus": {
        "13:20 - 15.07.2026": Difficulty.Green,
        "18:30 - 25.07.2026": Difficulty.Blue,
        "08:15 - 04.08.2026": Difficulty.Yellow,
    },

    "Software Engineering": {
        "10:50 - 16.07.2026": Difficulty.Blue,
        "15:40 - 26.07.2026": Difficulty.Green,
        "19:00 - 03.08.2026": Difficulty.Blue,
    },

    "Artificial Intelligence": {
        "12:10 - 17.07.2026": Difficulty.Red,
        "09:55 - 28.07.2026": Difficulty.Yellow,
        "16:35 - 04.08.2026": Difficulty.Green,
    },

    "Computer Architecture": {
        "14:30 - 18.07.2026": Difficulty.Yellow,
        "11:25 - 29.07.2026": Difficulty.Red,
        "17:15 - 03.08.2026": Difficulty.Yellow,
    },

    "Discrete Mathematics": {
        "08:20 - 19.07.2026": Difficulty.Green,
        "13:55 - 30.07.2026": Difficulty.Blue,
        "18:45 - 04.08.2026": Difficulty.Green,
    },
}
name="fully_secure_database"
database= Databasesys(subjects)
database.createdb(name)

lbox=ReviewSystem(subjects)
sorted_box=lbox.train()
review_topics=sorted_box[0:3]
#print(f"This is your results{review_topics}")
print("this here:")
pprint(review_topics)

#CLI
# the user options
main="""
    Welcome to your study tracker , how can I help?
        1)Open Review log
        2)Add new review
        3)Delete Review
        4)Show the entire database
        5)Exit

"""
option2="""
    To add a new Subject / new Review Session 
    write its name: 
"""
"""
import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])
    """
while True:
    opt=input(main)
    if int(opt)==1:
        for i in review_topics:
            f=i[0]
            print(f)
    elif int(opt)==2:
        x=input(option2)
        y=input("how difficult was it?")
        if y is "r":
            y=Difficulty.Red
        subj= Subject(x)
        subj.logdata(diff=y)
        test1=subj.name
        test2=subj.dates
        print(f"{test1} has the following revies and diff: {test2}")
        database.addtodb(subj,name)
    elif int(opt)==3:
            k=input("what topic you wanna delete")
            database.showall(k)
            j=input("What date do you wanna delet")
            database.delfromdb(k,j,name)
    elif int(opt)==4:
            
            with open(f"{name}.csv","r") as f:
                reader=csv.DictReader(f)
                printed=[]
                for row in reader:
                    if row["subject"] not in printed:
                        printed.append(row["subject"])
                for i in printed:
                    print(i)
                    
    elif int(opt)==1:
                pass
    else:
        pass

