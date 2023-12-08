from project import create_dice
from project import DiceFactory
from project import check_dice
from project import roll_dice


def main():
    test_create_dice()
    test_save()
    test_roll_dice()


def test_create_dice():
    dice1 = DiceFactory("d1", 0)
    dice2 = DiceFactory("d2", 0)
    assert dice1.name == "d1"
    assert dice2.name == "d2"
    assert dice1.value == 0
    assert dice2.value == 0
    assert dice1.save == False
    assert dice2.save == False

def test_save():
    dice1=DiceFactory("d1", 0)
    dice1.save = True
    assert dice1.save == True

def test_roll_dice():
    dice1 = DiceFactory("d1", 0)
    dice2 = DiceFactory("d2", 0)
    dice1.roll()
    dice2.roll()
    assert dice1.value > 0
    assert dice1.value < 7
    assert dice2.value > 0
    assert dice2.value < 7

if __name__ == "__main__":
    main()
