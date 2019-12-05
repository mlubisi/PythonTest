def greet():
    print("Wassop (**,)")

def response(msg):
    print("------------------\n"+msg+"\n---------------------")

def userInput():
    cmd = input("Enter Command To Continue...\n")
    if cmd == "exit":
        print("Exiting... Bye")
        exit()
    else:
        return cmd

def newQuestion(f):
    ucm = input("Enter 'q' : To Set New Question...\nEnter 's' : To Save Test\n")
    if ucm == "q":
        Q = input("Enter Question\n")
        U = input("Set Unswer for: "+Q+"\n")
        f.write("[Q:"+Q+",U:"+U+"]")
    if ucm != 's':
        newQuestion(f)

def newTest():
    Test = input("Enter Test Name\n")
    f = open("tests/"+Test+".gotit", "a")
    newQuestion(f)
    f.close()
    return response("Test Created...")

def openTest(name):
    rawData = []
    print("Opening Test : "+ name)
    f = open("./tests/"+name+".gotit", "r")
    for x in f:
        tmp = x.split(']')
        for t in tmp:
            rawData.append(t)
            print(t)

def listTests():
    import os
    path = './tests/'
    files = []
    lcache = []
    i = 0
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.gotit' in file:
                files.append(os.path.join(r, file))
    for f in files:
        i += 1
        rinse = f.replace(".gotit", "")
        rinse = rinse.replace(path, "")
        lcache.append(rinse)
        print(i, end = '')
        print(" : "+rinse)
    if len(lcache) > 0:
        ucm = int(userInput())
        if type(ucm) == int:
            openTest(lcache[ucm-1])
    else:
        print("No Tests Available...")


def home():
    print("1 : To Create Test(s) \n2 : To Write Test(s) \nexit : to quit")
    ucm = userInput()
    if ucm == "1":
        newTest()
        home()
    elif ucm == "2":
       print("Select Test\n")
       listTests()
    else:
        print("Invalid Input")
        
greet()
home()