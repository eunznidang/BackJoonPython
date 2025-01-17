def solution(arr):
    answer = []
    
    new = -1
    for a in arr:
      if new != a:
        answer.append(a)
        new=a
    
    return answer