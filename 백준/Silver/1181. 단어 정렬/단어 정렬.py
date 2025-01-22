N=int(input())
dic={}
for i in range(N):
    word=input()
    dic[word]=len(word)

# 딕셔너리 value 정렬 후 key 정렬
answer=dict(sorted(dic.items(), key=lambda x:(x[1], x[0])))
for key in answer.keys():
    print(key)