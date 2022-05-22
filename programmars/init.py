z = ["zero"]
o = ["one"]
t = ["two", "three"]
f = ["four", "five"]
s = ["six", "seven"]
e = ["eight"]
n = ["nine"]

def checkNum(num):
    if num[0] == "z":
        initNum = 0
    elif num[0] == "o":
        initNum = 1
    elif num[0] == "e":
        initNum = 8
    elif num[0] == "n":
        initNum = 9
    elif num[0] == "t":
        if num[1] == "w":
            initNum = 2
        else:
            initNum = 3
    elif num[0] == "f":
        if num[1] == "o":
            initNum = 4
        else:
            initNum = 5
    elif num[0] == "s":
        if num[1] == "i":
            initNum = 6
        else:
            initNum = 7
    return initNum
    
def solution(s):

    
    num = ""
    answer = []
    for str in s:
        if isdigit(str) :
            if num != "":
                answer.append(checkNum(num))
            answer.append(int(str))
        else:
            num += str

    return answer


solution("one4seveneight")
    