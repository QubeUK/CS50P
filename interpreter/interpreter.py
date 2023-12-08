a,b,c = input("Expression: ").strip().split()
a = float(a)
c = float(c)

match b:
    case "+":
        res = a + c
    case "-":
        res = a - c
    case "*":
        res = a * c
    case "/":
        res = a / c

print(res)
