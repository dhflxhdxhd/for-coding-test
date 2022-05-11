# def solution(id_list, report, k):
#     answer = []
#     report_id = [0]*len(id_list)
#     answer = [0]*len(id_list)  
#     answers = [0]*len(id_list) 
#     idx = []
    
#     for r in report:
#         arr = r.split()
#         if arr[1] == id_list[0]:
#             report_id[0] += 1
#         elif arr[1] == id_list[1]:
#             report_id[1] += 1
#         elif arr[1] == id_list[2]:
#             report_id[2] += 1
#         else:
#             report_id[3] += 1

#     for i,id in enumerate(report_id):
#         if id >= k:
#             idx.append(i)
#             answer[i] += 1

#     print(report)
#     print(answer)
#     for r in report:
#         arr = r.split()
#         for ans in answer:
#             if arr[1] == id_list[ans]:
#                 answers[id_list.index(arr[0])] += 1
                
#     print(answer)
#     print(answers)
#     return answer

# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2

# solution(id_list, report, k)