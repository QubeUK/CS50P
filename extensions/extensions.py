import os
filename = input("File name: ").lower().strip()
ext = os.path.splitext(filename)[1]
match ext:
    case ".jpg" | ".jpeg":
        print("image/jpeg")
    case ".gif":
        print("image/gif")
    case ".png":
        print("image/png")
    case ".txt":
        print("text/plain")
    case ".pdf":
        print("application/pdf")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
