def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge=[]
    for i in range(bridge_length):bridge.append(-1)

    now_weight=0
    while len(bridge)>0:
      out_truck=bridge.pop(0)
      if out_truck>0: 
        now_weight-=out_truck
      
      if len(truck_weights)>0:
        if now_weight+truck_weights[0] <= weight:
         in_truck=truck_weights.pop(0)
         bridge.append(in_truck)
         now_weight+=in_truck
        else: bridge.append(-1)
      answer+=1


    return answer