from datetime import datetime
from .Diff_Model import Difficulty
class Subject:
    def __init__(self,name,dates=None):
        self.name=name
        if dates is None:
            current_time = datetime.now().strftime("%H:%M - %d.%m.%Y")
            self.dates = {current_time: Difficulty.Blue}
        else:
            self.dates = dates
    def logdata(self,date=None,diff=None):
        """           if diff is None:
                        print(f"this is the dates {self.dates}")
                        self.dates[date]=Difficulty.Red
                    else:
        """
        ###"22:30 - 31.07.2026"
        if date is None:
            current_time = datetime.now().strftime("%H:%M - %d.%m.%Y")
            self.dates[current_time]=diff
        else:
            self.dates[date]=diff




    def returnlast(self):
        date_format = "%H:%M - %d.%m.%Y"

        latest_key = max(
            self.dates,
            key=lambda date: datetime.strptime(date, date_format)
        )

        return latest_key
    def returnlvl(self):
        key=self.returnlast()
        return self.dates[key]

algo1 = Subject(
    "Algorithms",
    dates={
        "10:30 - 10.07.2026": Difficulty.Blue,
        "14:45 - 20.07.2026": Difficulty.Green,
        "09:15 - 25.07.2026": Difficulty.Red,
    }
)

algo1.logdata("18:30 - 30.07.2026", Difficulty.Yellow)

print(algo1.dates)
print("Latest difficulty:", algo1.returnlast(),algo1.returnlvl())





