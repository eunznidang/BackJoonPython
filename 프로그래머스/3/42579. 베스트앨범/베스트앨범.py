def solution(genres, plays):
    answer = []

    music={}
    i=0
    sum={}

    for genre in genres:
      dic=music.get(genre, {})
      dic[i]=plays[i]
      music[genre]=dic
      sum[genre]=sum.get(genre, 0)+plays[i]
      i+=1
    
    sum=dict(sorted(sum.items(), key=lambda x: -x[1]))
    
    for genre in sum.keys():
      keys=sorted(music[genre].items(), key=lambda x: -x[1])
      if len(keys) >=2:
        answer.append(keys[0][0])
        answer.append(keys[1][0])
      else:
        answer.append(keys[0][0])

    return answer