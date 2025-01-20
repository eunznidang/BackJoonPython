def solution(priorities, location):
    answer = 0
    idx=0
    queue=[]

    for p in priorities:
      queue.append([idx, p])
      idx+=1
      
    priorities.sort(reverse=True)
    
    while True:
      q=queue.pop(0)
      print(q)
      if q[1]>=priorities[0]:
        if q[0]==location:
          return answer+1
        else:
          answer+=1
          priorities.pop(0)

      else:
        queue.append(q)

    return answer