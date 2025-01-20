def solution(progresses, speeds):
    answer = []
    arr = list(map(lambda x: 100 - x, progresses))
    arr = list(map(lambda x, y: (x+y-1) // y, arr, speeds))

    i=0
    sum=1

    while i < (len(arr)):
      if i == len(arr)-1:
        answer.append(sum)
        break

      j=i+1
      while j < (len(arr)) and arr[i] >= arr[j]:
          sum+=1
          j+=1
          
      answer.append(sum)
      sum=1
      i=j

      
    return answer