import requests, sys, json

def main():
    num = read_argv()
    amount = check_price()
    amount = float(amount.replace(",","")) * num
    print(f"${amount:,.4f}")

def check_price():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data=json.loads(response.text)
    amount = data['bpi']['USD']['rate']
    return amount

def read_argv():
    while True:
        try:
            if len(sys.argv) == 2:
                num=float(sys.argv[1])
                return num
            else:
                sys.exit("Missing command-line argument")
        except ValueError:
            sys.exit("Command-line argument is not a number")

if __name__ == "__main__":
    main()
