import csv


class Databasesys:
    def __init__(self, data=None):
        if data is None:
            data = {}

        self.data = data
        self.secret_data={}

    def createdb(self, filename):
        with open(
            filename + ".csv",
            "r+",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=["subject", "date", "difficulty"]
            )

            writer.writeheader()

            for subject, dates in self.data.items():
                for date, difficulty in dates.items():
                    writer.writerow({
                        "subject": subject,
                        "date": date,
                        "difficulty": difficulty.value
                    })
            file.seek(0)
            reader = csv.DictReader(file)
            self.secret_data= list(reader)
            #print(self.secret_data)

    def addtodb(self, sub, filename):
        if sub.name in self.data:
            # Add the new dates to the existing subject
            self.data[sub.name].update(sub.dates)
        else:
            # Add a completely new subject
            self.data[sub.name] = sub.dates.copy()

        # Save the updated dictionary
        self.createdb(filename)

    def delfromdb(self,sub,date,filename):
        """
        This takes the list created during the databse creation
        and uses it to delte a specific aspect of it.
        It lokks like the following:
        {'subject': 'Algorithms', 
        'date': '10:30 - 10.07.2026', 'difficulty': 'b'}, 
        {'subject': 'Algorithms', 
        'date': '14:45 - 20.07.2026', 'difficulty': 'g'}, 
        and similar like this
        
        """
        #lst_topic=[]
        for i in self.secret_data:
            if i["subject"] == sub and i["date"] == date:
                self.secret_data.remove(i)
                break
        self.createdb(filename)
    
    def showall(self,sub):
        """
        This method takes the name of the sub , finds it and 
        visualize their info
        
        """
        sub_list=[]
        for i in self.secret_data:
            if i["subject"]==sub:
                sub_list.append(i)
        for j in sub_list:
            print(j["date"])

