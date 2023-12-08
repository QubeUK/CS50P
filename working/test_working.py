from working import convert
import pytest

def main():
    test_convert()

def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


    with pytest.raises(ValueError):
        convert("9 to 10")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")
    with pytest.raises(ValueError):
        convert("9AM to 10PM")


if __name__ == "__main__":
    main()
