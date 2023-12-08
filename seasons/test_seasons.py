from seasons import convert
import pytest

def main():
    test_convert()

def test_convert():
    assert convert("2022-11-10") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert("2021-11-10") == "One million, fifty-one thousand, two hundred minutes"
    with pytest.raises(SystemExit):
        convert("hello")

if __name__ == "__main__":
    main()
