def solution(clothes):
    answer = 1

    category={}
    for cloth in clothes:
      category[cloth[1]]=category.get(cloth[1], 0)+1


    for cloth, count in category.items():
      answer*=(count+1)
    
    answer-=1

    return answer