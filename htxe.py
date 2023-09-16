import os
def starthtxe():
    print("Humanity TextEditor 0.0.4")
    print("c. Create file")
    print("o. Open file and show entires")
    print("ow. Open file and write")
    a = input()
    if (a == "c"):
        print("Filename")
        filename = input(":") + ".htf"
        print("Data")
        data = input(":")
        with open(filename, 'w') as f:
            f.write(data)
        print("Ok")
        b = input(":")
        if (b == "close"):
            print("Ok")
        elif (b == "open"):
            ficus = open(filename, mode='r', encoding='utf-8')
            print(ficus.read())
            print("Ok")
    elif (a == "o"):
        print("Filename (FILE EXTENSION WILL BE AUTOMATICLY .htf, please dont type extension!)")
        filename = input(":") + ".htf"
        ficus = open(filename, mode='r', encoding='utf-8')
        print(ficus.read())
        print("Ok")
    elif (a == "ow"):
        print("Filename")
        filename = input(":") + ".htf"
        print("Data")
        data = input(":")
        ficuss = open(filename, mode='r', encoding='utf-8')
        print(ficuss.read())
        with open(filename, 'w') as f:
            f.write(data)
        ficus = open(filename, mode='r', encoding='utf-8')
        print(ficus.read())








