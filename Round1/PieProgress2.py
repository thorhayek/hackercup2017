# -*- coding: utf-8 -*-
"""
Created on Sat Jan 07 20:14:22 2017
pie progress FB hacker cup 1
@author: vishay
python 2.7
"""

import math
import time

def calc_total_cost(sale_dict):
    tot_cost = 0 
    #print sale_dict
    for sale_date in sale_dict.keys():
        sale_list = sale_dict[sale_date]
        num_items = len(sale_list)
        tot_cost += sum(sale_list) + num_items**2
    return tot_cost
    
def pie_cost(target_days, sale_per_day, cost_dict):
    
    day_pies = {} # contains the cost of pies bought along with day
    for day in xrange(1,target_days+1):
        
        total_pies = sum([len(x) for x in day_pies.values()])
        if(total_pies == target_days):
            return calc_total_cost(day_pies)
        # extra pies so far is total_pies - today's pies
        extra_pies = total_pies - day 
        if(extra_pies < 0): # we have to get a pie today
            # get the min cost pie for today
            if(day in day_pies):
                day_pies[day].append(cost_dict[day][0])
            else:
                day_pies[day] = [cost_dict[day][0]]
            #print day_pies,"added"
            extra_pies = 0
            #remove the pie bought today
            cost_dict[day].pop(0)
            #print cost_dict,"removed"
        
        # while pie's still available for the day
        while(len(cost_dict[day]) != 0 ):
            # look for more pies for future while piles are for sale
            # look for min in the values of today , today + extra pies so far , + past days
            total_pies = sum([len(x) for x in day_pies.values()])
            if(total_pies == target_days):
                return calc_total_cost(day_pies)
                
            sum_day = day+extra_pies +1 
            max_day  = sum_day if sum_day <= target_days else target_days
            selected_buy_day = None
            min_score = float('inf')
            
            for buy_day in xrange(1, max_day+1):
                remain_pies = len(cost_dict[buy_day])
                if ( remain_pies > 0 ):
                    curr_sold = sale_per_day - remain_pies
                    score = cost_dict[buy_day][0] + ((curr_sold+1)**2 - curr_sold**2) 
                    if (score < min_score):
                        min_score = score
                        selected_buy_day = buy_day
            
            if(selected_buy_day in day_pies):
                day_pies[selected_buy_day].append(cost_dict[selected_buy_day][0])
            else:
                day_pies[selected_buy_day] = [cost_dict[selected_buy_day][0]]
            #print day_pies,"added2"
            #remove the pie bought today
            cost_dict[selected_buy_day].pop(0)
            extra_pies += 1
            #print cost_dict,"removed2"
        total_pies = sum([len(x) for x in day_pies.values()])
    return calc_total_cost(day_pies)
        
# read input file 
#input_file = "pie_progress_example_input.txt"; # example input
input_file = "pie_progress.txt"; # real input
output_file = "output.txt";

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
        
    pie_days,pie_sale_per_day = map(lambda x: int(x), line.split())
    
    days_dict = {}
    for pday in xrange(1,pie_days+1):
        days_dict[pday] = sorted(map(lambda x:int(x),fi.readline().split()))        
    
    ans = pie_cost(pie_days,pie_sale_per_day,days_dict)
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
"""

