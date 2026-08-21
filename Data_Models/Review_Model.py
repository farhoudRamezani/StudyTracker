class ReviewSystem:
    def __init__(self, dic):
        self.dic = dic

    def train(self):
        redbox = []
        yellowbox = []
        greenbox = []

        for subject_name, subject_dates in self.dic.items():
            last_three = list(subject_dates.values())[-3:]

            for difficulty in last_three:
                difficulty_value = getattr(
                    difficulty,
                    "value",
                    difficulty
                )

                result = (
                    subject_name,
                    difficulty_value.upper()
                )

                if difficulty_value in ("r", "b"):
                    redbox.append(result)
                elif difficulty_value == "y":
                    yellowbox.append(result)
                else:
                    greenbox.append(result)

        allboxes = redbox + yellowbox + greenbox
        return allboxes