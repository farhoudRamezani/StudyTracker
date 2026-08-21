from Data_Models.Subject_Model import Subject
from Data_Models.Diff_Model import Difficulty
from Data_Models.Saving_Model import Databasesys
from Data_Models.Review_Model import ReviewSystem


name = "fully_secure_database"
database = Databasesys()
database.csvtodic(name)

main_menu = """
Welcome to your Study Tracker. How can I help?
    1) Open review log
    2) Add new review
    3) Delete review
    4) Show the entire database
    5) Exit

Choose an option: """

option2 = """
To add a new subject or review session,
write the subject name: """


while True:
    opt = input(main_menu).strip()

    if opt == "1":
        review_topics = ReviewSystem(database.data).train()[0:3]

        if not review_topics:
            print("No reviews found.")
        else:
            for subject_name, difficulty in review_topics:
                print(f"{subject_name}: {difficulty}")

    elif opt == "2":
        subject_name = input(option2).strip()

        if not subject_name:
            print("The subject name cannot be empty.")
            continue

        difficulty = input(
            "How difficult was it? (r = red, y = yellow, "
            "g = green, b = blue): "
        ).strip().lower()

        if difficulty == "r":
            difficulty = Difficulty.Red
        elif difficulty == "y":
            difficulty = Difficulty.Yellow
        elif difficulty == "g":
            difficulty = Difficulty.Green
        elif difficulty == "b":
            difficulty = Difficulty.Blue
        else:
            print("Invalid difficulty. Please use r, y, g, or b.")
            continue

        subject = Subject(subject_name, dates={})
        subject.logdata(diff=difficulty)
        database.addtodb(subject, name)

        print(f"Review added for {subject.name}.")

    elif opt == "3":
        subject_name = input(
            "What subject do you want to delete from? "
        ).strip()

        if database.showall(subject_name):
            date = input("What date do you want to delete? ").strip()
            database.delfromdb(subject_name, date, name)

    elif opt == "4":
        if not database.data:
            print("The database is empty.")
        else:
            for subject_name, dates in database.data.items():
                print(f"\n{subject_name}")

                for date, difficulty in dates.items():
                    print(f"  {date}: {difficulty.value.upper()}")

    elif opt == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose a number from 1 to 5.")