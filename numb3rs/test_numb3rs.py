from numb3rs import validate

def main():
    test_validate()

def test_validate():
    assert validate("10.10.10.10") == True
    assert validate("")== False
    assert validate("cat")== False
    assert validate("10.10.10.10.10")== False
    assert validate("10.10.10.1000")== False
    assert validate("259.10.10.100")== False
    assert validate("10.259.10.100")== False
    assert validate("10.10.259.100")== False


if __name__ == "__main__":
    main()
