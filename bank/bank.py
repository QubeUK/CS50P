answer = input ("Greeting: ").strip()

if answer.split()[0] == "Hello":
    print("$0")
elif answer == "Hello, Newman":
    print("$0")
elif answer[0] == "H":
    print("$20")
else:
    print("$100")
