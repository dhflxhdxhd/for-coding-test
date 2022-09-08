# 순위 검색


def solution(info, query):
    info_list = [([] for i in range(5)) for i in range(len(info))]
    query_list = [([] for i in range(5)) for i in range(len(info))]
    
    for i in range(len(info)):
        info_list[i] = info[i].split(" ")

    for j in range(len(query)):
        query_list[j] = query[j].split(" ")

    fo
    for x in range(len(info_list)):
        for y in range(5):
            if info_list[x][y] == query_list[x][y]:
                


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info,query))



