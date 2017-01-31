# -*- coding: utf-8 -*-
"""
Created on Sat Jan 07 20:14:22 2017
pie progress FB hacker cup 1
@author: vishay
python 2.7
"""


import sys 
import time

def allPairsShortestPath(g):

    dist = {}
    pred = {}
    for u in g:
        dist[u] = {}
        pred[u] = {}
        for v in g:
            dist[u][v] = float('inf')
            pred[u][v] = None

        dist[u][u] = 0
        pred[u][u] = None

        for v in g[u]:
            dist[u][v] = g[u][v]
            pred[u][v] = u

    for mid in g:
        for u in g:
            for v in g:
                newlen = dist[u][mid] + dist[mid][v]
                if newlen < dist[u][v]:
                    dist[u][v] = newlen
                    pred[u][v] = pred[mid][v]

    return (dist,pred)

        
def constructShortestPath(s, t, pred):
    
    path = [t]

    while t != s:
        t = pred[s][t]
        
        if t is None:
            return None
        path.insert(0, t)
    
    return path

def get_gas(graph_dict, tup_lst):
    dist_dict,prev_dict = allPairsShortestPath(graph_dict)
    #sum_gas = dist_dict[1][tup_lst[0][0]]
    start_node = 1
    #print sum_gas,"star gas"
    sum_gas = 0
    tup_idx = 0
    while(tup_idx < len(tup_lst)):
        #print tup_idx,"idx"
        tup = tup_lst[tup_idx]
        #transition to new source 
        sum_gas += dist_dict[start_node][tup[0]]
        #print sum_gas,"gas0"
        if(sum_gas == float('inf')):
            return -1
            
        # go from source to dest
        min_gas = dist_dict[tup[0]][tup[1]]
        if(min_gas == float('inf')):
            return -1
        path_lst = constructShortestPath(tup[0],tup[1],prev_dict)
        #print path_lst,"path, gas",min_gas  
        sum_gas += min_gas    
        #print sum_gas,"gas1"
            
        #check next delivery
        if tup_idx+1 < len(tup_lst):
            next_tup = tup_lst[tup_idx+1]
            if(next_tup[0] in path_lst and next_tup[1] == tup[1]): # case where next tup goes to same dest
                #print "same as prev or midway pickup",tup_lst[tup_idx+1]
                tup_idx +=1
            elif(next_tup[0] in path_lst[:-1] and next_tup[1] != tup[1] ):
                #print "start midway end after"
                sum_gas += dist_dict[tup[1]][next_tup[1]]
                if(sum_gas == float('inf')):
                    return -1
                tup_idx += 1
                tup = next_tup
                
            #print "min_gas",dist_dict[tup[1]][next_tup[0]]
            #print sum_gas,"gas2"
        start_node = tup[1]
        tup_idx += 1
    return sum_gas
        
# read input file 
input_file = "manic_moving_example_input.txt"; # example input
#input_file = "manic_moving.txt"; # real input
#input_file = "manicmoving.txt"; # real input
output_file = "output_gas.txt";

fi = open(input_file,'r');
fo = open(output_file, 'w');

case_count = int(fi.readline());
#print("case_count="+str(case_count));
#cases = fi.read();
curr_line = 1;
start_time = time.time()
while True:
    #print("case="+line);
    line = fi.readline()
    if not line: break
        
    nodes,edges,moves = map(lambda x: int(x), line.split())
    graph_dict = {node:{} for node in xrange(1,nodes+1)}
    val = sys.maxint
    for _ in xrange(edges):
        edge_lst = map(lambda x:int(x),fi.readline().split())
        if edge_lst[1] in graph_dict[edge_lst[0]]:
            val = graph_dict[edge_lst[0]][edge_lst[1]]
            #print edge_lst,"problem" # TODO check this works
        graph_dict[edge_lst[0]][edge_lst[1]] = min(val,edge_lst[2]) 
        graph_dict[edge_lst[1]][edge_lst[0]] = graph_dict[edge_lst[0]][edge_lst[1]]

    tup_lst = []    
    for _ in xrange(moves):
        mv_tup = tuple(map(lambda x:int(x),fi.readline().split()))
        tup_lst.append(mv_tup)
    
    #print graph_dict
    #print tup_lst
    
    ans = get_gas(graph_dict,tup_lst)
    
    print "Case #"+str(curr_line)+": " +str(ans)
    if(curr_line < case_count):
        fo.write("Case #"+str(curr_line)+": "+str(ans)+"\n")
    else:
        fo.write("Case #"+str(curr_line)+": "+str(ans))
    curr_line += 1
fo.close()
end_time = time.time()
print "time taken to solve",end_time-start_time," seconds"
#fo.close()


"""
tests 
graph = {0: {1: 2, 4:4},
         1: {2:3},
         2: {3:5, 4:1 },
         3: {0: 8},
         4: {3:3}}
"""

