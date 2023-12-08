def main():
    try:
        my_list = []
        while True:
            my_list.append(input().upper())
    except:
        my_list.sort()
        ulist = list(dict.fromkeys(my_list))
        for item in ulist:
            print(my_list.count(item),item)

main()
