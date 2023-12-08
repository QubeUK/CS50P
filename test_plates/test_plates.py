from plates import is_valid

def main():
    test_is_valid()

def test_is_valid():
    assert is_valid("aa123")==True
    assert is_valid("abcde")==True
    assert is_valid("aa1123")==True
    assert is_valid("aa")==True
    assert is_valid("aa111123")==False
    assert is_valid("a")==False
    assert is_valid("aa123a")==False
    assert is_valid("")==False
    assert is_valid("123")==False
    assert is_valid("1-2-3")==False
    assert is_valid("aa0")==False
    assert is_valid("0")==False
    assert is_valid("!!!")==False
    assert is_valid("twotwo")==True
    assert is_valid("tot 12")==False



if __name__ == "__main__":
    main()
