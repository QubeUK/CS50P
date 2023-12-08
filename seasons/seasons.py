from datetime import date
import sys, inflect

p = inflect.engine()

def main():
    print(convert(input("Date of birth (YYYY-MM-DD): ")))

def convert(dob):
    try:
        dob = date.fromisoformat(dob)
        today = date.today()
        delta = today - dob
        minutes = delta.days*60*24
        minutes = p.number_to_words(minutes, andword="").capitalize()
        minutes = minutes + " minutes"
        return minutes
    except:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
