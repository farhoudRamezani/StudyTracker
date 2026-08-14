from Data_Models.Diff_Model import Difficulty
from Data_Models.Review_Model import ReviewSystem


def test_train_uses_last_three_entries_from_each_subject():
    dummy_data = {
        "Algorithms": {
            "date1": Difficulty.Green,   # Should be ignored
            "date2": Difficulty.Red,
            "date3": Difficulty.Yellow,
            "date4": Difficulty.Blue,
        },
        "Databases": {
            "date1": Difficulty.Blue,    # Should be ignored
            "date2": Difficulty.Green,
            "date3": Difficulty.Yellow,
            "date4": Difficulty.Red,
        },
    }

    review_system = ReviewSystem(dummy_data)

    result = review_system.train()

    expected = [
        Difficulty.Red,
        Difficulty.Blue,
        Difficulty.Red,
        Difficulty.Yellow,
        Difficulty.Yellow,
        Difficulty.Green,
    ]

    assert result == expected
print("done")