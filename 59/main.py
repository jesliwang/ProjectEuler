import os, sys


file = open(os.path.dirname(__file__) + "/clipher.txt")

line = file.readline()

encryText = ""
while line:
    encryText = encryText+line
    line = file.readline()

encryArray = encryText.split(",")

def unEncry(encryStr):
    st = ord('a')
    ed = ord('z')
    for a in range(st, ed + 1):
        for b in range(st, ed + 1):
            for c in range(st, ed + 1):
                unEryArray = [a,b,c]
                flag = True
                for index in range(0, len(encryStr)):
                    p = int(encryStr[index])^unEryArray[index%3]
                    if not (( p >= ord('a') and p <= ord('z')) or (p >= ord('A') and p <= ord('Z')) or (p == ord(' ') or (p == ord(',')) or (p==ord('.')) or (p==ord('-')) or ( p>=ord('1') and (p <= ord('9'))) or p == ord('"') or p == ord('\'') or p == ord('?') or p == ord('!') or p == ord(';') or p == ord(':') or p == ord('(') or p == ord(')'))) :
                        print chr(p),":",a,b,c,index
                        flag = False
                        break
                    print chr(p),p,ord('a'),ord('z'),ord('A'),ord('Z'),(( p >= ord('a') and p <= ord('z')) or (p >= ord('A') and p <= ord('Z')))

                if flag:
                    return [a,b,c]

    return []

ecyWord = unEncry(encryArray)

if len(ecyWord) != 3:
    print "Wrong"
else:
    message=""
    for index in range(0, len(encryArray)):
        p = int(encryArray[index])^ecyWord[index%3]
        print p,encryArray[index]
        message = message + chr(p)

    print message
