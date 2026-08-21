from datetime import datetime

from .Diff_Model import Difficulty


class Subject:
    def __init__(self, name, dates=None):
        self.name = name

        if dates is None:
            current_time = datetime.now().strftime("%H:%M - %d.%m.%Y")
            self.dates = {current_time: Difficulty.Blue}
        else:
            self.dates = dates.copy()

    def logdata(self, date=None, diff=None):
        if diff is None:
            diff = Difficulty.Blue

        if date is None:
            date = datetime.now().strftime("%H:%M - %d.%m.%Y")

        self.dates[date] = diff

    def returnlast(self):
        date_format = "%H:%M - %d.%m.%Y"

        latest_key = max(
            self.dates,
            key=lambda date: datetime.strptime(date, date_format)
        )

        return latest_key

    def returnlvl(self):
        key = self.returnlast()
        return self.dates[key]