def solution(participant, completion):
    answer = ''
        
    dic={}

    for name in participant:
      dic[name]=dic.get(name, 0) +1
    
    for name in completion:
      dic[name]-=1
    
    for name, count in dic.items():
      if count==1:
        answer=name
    
    return answer