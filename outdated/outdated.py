def main():
    udate = get_input().strip()
    try:
        m,d,y = udate.split("/")
        if m.isalpha():
            main()
        elif len(y)==4 and int(d)>0 and int(d)<32 and int(m) >0 and int(m)<13:
            print(y,str(m).zfill(2),str(d).zfill(2),sep="-")
        else:
            main()
    except:
        m,d,y = udate.split(" ")
        if "," not in d:
            main()
        d = d.replace(",","")
        m = m.title()
        if m in months and len(y)==4 and int(d)>0 and int(d)<32:
            month = (months.index(m)) +1
            print(y,str(month).zfill(2),str(d).zfill(2),sep="-")
        else:
            main()

def get_input():
    while True:
            try:
                udate = input("Date: ")
            except ValueError:
                pass
            else:
                return udate
months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

main()
