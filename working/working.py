import re, sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit(ValueError)

def convert(s):

    if "-" in s:
        raise ValueError

    single_digit = re.search(r'^(\d+)\D(\w+)\s([A-Z\-]+)\s(\S+)\s+(\w+)\D$',s ,re.IGNORECASE)
    double = re.search(r'^(\d+)\D(\w+)\s([A-Z\-]+)\s(\S+)\s+(\w+):(\d+)\s(\w+)$',s,re.IGNORECASE)

    if single_digit:
        start=single_digit.group(1)
        end=single_digit.group(4)
        ampm_start=single_digit.group(2)
        ampm_end=single_digit.group(5)
        try:
            x=int(start)
        except ValueError:
            raise ValueError
        if int(start) < 12 and ampm_start == "PM":
            start = int(start) + 12
        if int(start) == 12 and ampm_start == "AM":
            start = "00"
        if int(end) < 12 and ampm_end == "P":
            end = int(end) + 12
        if int(end) == 12 and ampm_end == "AM":
            end = "00"

        start = str(start).zfill(2)+":00"
        end = str(end).zfill(2)+":00"
        hours = start+" to "+end
        return hours

    if double:
        start=double.group(1)
        start_min=double.group(2)
        ampm_start=double.group(3)
        end=double.group(5)
        end_min=double.group(6)
        ampm_end=double.group(7)

        if int(start_min) > 59 or int(end_min) >59:
            raise ValueError
        if int(start) < 12 and ampm_start == "PM":
            start = int(start) + 12
        if int(start) == 12 and ampm_start == "AM":
            start = "00"
        if int(end) < 12 and ampm_end == "PM":
            end = int(end) + 12
        if int(end) == 12 and ampm_end == "AM":
            end = "00"

        start = str(start).zfill(2)+":"+str(start_min)
        end = str(end).zfill(2)+":"+str(end_min)
        hours = start+" to "+end
        return hours

    raise ValueError
if __name__ == "__main__":
    main()
