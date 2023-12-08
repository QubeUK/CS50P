import sys, csv

def main():
    filename_b, filename_a = read_argv()
    clean_list = clean_file(filename_b)
    student_list=[]
    with open(filename_a, 'w', newline='') as file:
        writer = csv.writer(file)
        file.write("first,last,house\n")
        for row in clean_list[1:]:
            house = str(row[1])
            last,first = str(row[0]).split(",",1)
            first = first.strip()
            student = first,last,house
            student_list.append(student)
            writer.writerow(student)

def clean_file(filename):
    with open(filename) as csvfile:
        clean_list = list(csv.reader(csvfile, delimiter=","))
    return clean_list

def read_argv():
    argv_in = 3 #Amount of expected command line arguments
    while True:
        try:
            if len(sys.argv) == argv_in and sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
                try:
                    with open(sys.argv[1]) as file:
                        return sys.argv[1], sys.argv[2]
                except FileNotFoundError:
                    sys.exit(f"Could not read {sys.argv[1]}")
            elif len(sys.argv) == argv_in and not sys.argv[1].endswith(".csv"):
                sys.exit("Not a CSV file")
            elif len(sys.argv) < argv_in:
                sys.exit("Too few command-line arguments")
            elif len(sys.argv) > argv_in:
                sys.exit("Too many command-line arguments")
            else:
                continue
        finally:
                pass

if __name__ == "__main__":
    main()
