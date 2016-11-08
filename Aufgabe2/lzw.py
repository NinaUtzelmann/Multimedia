#!/usr/bin/python

input = []
outputCoding = []
outputEncoding = []


def readIn():
    fobj = open("text.txt", "r")

    for line in fobj:
        for char in line:
            input.append(char)

    fobj.close()

def coding():
    index = 1
    count = 7
    i = 0
    dic = {}
    dic["/"] = 1
    dic["W"] = 2
    dic["E"] = 3
    dic["D"] = 4
    dic["B"] = 5
    dic["T"] = 6

    s = input[0]

    while i < len(input):
        i += 1

        if index is len(input):
            outputCoding.append(dic[s])
            break

        c = input[index]

        if (s + c) in dic.keys():
            s = s + c
            index += 1

        else:
            outputCoding.append(dic[s])
            dic[s+c] = count

            s = c
            index += 1
            count += 1



    return dic

def encoding():
    dic = {}
    dic[1] = "/"
    dic[2] = "W"
    dic[3] = "E"
    dic[4] = "D"
    dic[5] = "B"
    dic[6] = "T"

    i = outputCoding[0]
    counter = 1

    a = 0
    count = 7
    outputEncoding.append(dic[i])

    while a < len(outputCoding) - 1:
        a += 1

        j = outputCoding[counter]

        if j in dic.keys():
            dic[count] = dic[i] + dic[j][0]
            outputEncoding.append(dic[j])
            count += 1
            counter += 1

        else:
            dic[count] = dic[i] + dic[i][0]
            outputEncoding.append(dic[i] + dic[i][0])
            count += 1
            counter += 1

        i = j
    return dic

if __name__ == "__main__":
    readIn()
    dicIn = coding()
    print("Eingabetext: \t\t\t\t%s" %input)
    print("---------------------------------------------------Codierung---------------------------------------------------")
    print("Entstandenes Dictionary: \t%s" %sorted(dicIn.items(), key=lambda x:x[1]))
    print("Entstandene Codierung: \t\t%s" %outputCoding)
    print("---------------------------------------------------Encodierung---------------------------------------------------")
    dicOut = encoding()
    print("Entstandenes Dictionary: \t%s" %sorted(dicOut.items()))
    print("Entstandene Decodierung: \t%s" %outputEncoding)









