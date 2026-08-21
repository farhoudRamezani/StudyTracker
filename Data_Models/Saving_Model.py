import csv

from .Diff_Model import Difficulty


class Databasesys:
    def __init__(self, data=None):
        if data is None:
            data = {}

        self.data = data
        self.secret_data = []

    def createdb(self, filename):
        with open(
            filename + ".csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["subject", "date", "difficulty"]
            )

            writer.writeheader()
            self.secret_data = []

            for subject, dates in self.data.items():
                for date, difficulty in dates.items():
                    difficulty_value = getattr(
                        difficulty,
                        "value",
                        difficulty
                    )

                    row = {
                        "subject": subject,
                        "date": date,
                        "difficulty": difficulty_value
                    }

                    writer.writerow(row)
                    self.secret_data.append(row)

    def addtodb(self, sub, filename):
        if sub.name in self.data:
            self.data[sub.name].update(sub.dates)
        else:
            self.data[sub.name] = sub.dates.copy()

        self.createdb(filename)

    def csvtodic(self, filename):
        self.data = {}
        self.secret_data = []

        try:
            with open(
                f"{filename}.csv",
                "r",
                newline="",
                encoding="utf-8"
            ) as file:
                reader = csv.DictReader(file)

                for row in reader:
                    name = row["subject"]
                    date = row["date"]
                    difficulty = Difficulty(row["difficulty"])

                    if name not in self.data:
                        self.data[name] = {}

                    self.data[name][date] = difficulty
                    self.secret_data.append(row)

        except FileNotFoundError:
            self.createdb(filename)

        return self.data

    def csvdel(self, filename, name, date):
        rows = []

        with open(
            f"{filename}.csv",
            "r",
            newline="",
            encoding="utf-8"
        ) as file:
            reader = csv.reader(file)

            for row in reader:
                if not (row[0] == name and row[1] == date):
                    rows.append(row)

        with open(
            f"{filename}.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    def delfromdb(self, sub, date, filename):
        for review in self.secret_data:
            if review["subject"] == sub and review["date"] == date:
                self.secret_data.remove(review)

                if sub in self.data and date in self.data[sub]:
                    del self.data[sub][date]

                    if not self.data[sub]:
                        del self.data[sub]

                self.csvdel(filename, sub, date)
                print("Review deleted.")
                return True

        print("Review not found.")
        return False

    def showall(self, sub):
        found = False

        for review in self.secret_data:
            if review["subject"] == sub:
                print(
                    f'{review["date"]}: '
                    f'{review["difficulty"].upper()}'
                )
                found = True

        if not found:
            print("Subject not found.")

        return found