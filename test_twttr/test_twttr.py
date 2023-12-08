from twttr import shorten

def main():
   test_twttr()

def test_twttr():
    assert shorten("hello world") == "hll wrld"
    assert shorten("1 world") == "1 wrld"
    assert shorten("hello world!") == "hll wrld!"
    assert shorten("hEllo world") == "hll wrld"






if __name__ == "__main__":
    main()
