from um import count

def main():
    test_count()

def test_count():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


if __name__ == "__main__":
    main()

