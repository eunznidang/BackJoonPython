def solution(s):
    answer = True
    
    a=[]
    for c in s:
      a.append(c)
    
    if a[0] == ')':
      return False

    else:
      count=0
      while len(a)>0:
        if a.pop()==')':
          count+=1
        else:
          count-=1
        
        if count<0:
          return False

      
      if count!=0:
        return False
      

    return True