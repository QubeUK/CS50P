import re

def main():
    print(parse(input("HTML: ")))

def parse(s):

    iframe = re.search(re.compile(r'<\s*iframe[^>]*src=\"(.*?)\"[^>]*\/*>'),s)
    if not iframe:
        return

    matches = re.search(re.compile(r'([A-Za-z]+://)([-\w]+(?:\.\w[-\w]*)+)(:\d+)?(/[^.!,?"<>\[\]{}\s\x7F-\xFF]*(?:[.!,?]+[^.!,?"<>\[\]{}\s\x7F-\xFF]+)*)?'),s)
    if matches.group(2) == "www.youtube.com" or matches.group(2) =="youtube.com":
        url = str(matches.group(2,4)).replace("'","")
        url = "https://"+url
        url = url.replace("www.youtube.com","youtu.be")
        url = url.replace("youtube.com","youtu.be")
        url = url.replace("/embed","")
        url = url.replace(", ","")
        url = url.replace("(","")
        url = url.replace(")","")
        return url

if __name__ == "__main__":
    main()
