# -*- coding: utf-8 -*-
"""
Created on Sat Jan 07 20:14:22 2017
pie progress FB hacker cup 1
@author: vishay
python 2.7
"""

import math
import time


def is_in_progress_chart(line):
    """
      shift origin coordinates  to 50,50
      interchange axis i.e +y becomes +x and +x becomes +y
      convert to polar coordinates
      check the polar coordinates to see if they lie inside the chart
    """
    split_val = line.split()
    radius_square = 50**2
    if(len(split_val) == 3):
        split_val = [int(val) for val in split_val]
        filled_angle = split_val[0]/100.0 * 360
        test_point = tuple(split_val[1:])
        #print filled_angle,test_point
        test_point = map(lambda x: x-50, test_point)
        
        # 50,50 is always inside the progress chart if filled_angle>0
        if(test_point[0] == 0 and test_point[1] == 0 and filled_angle > 0):
            return True
        # set the degree correction variable for conversion to polar
        elif(test_point[0] >= 0 and test_point[1] >= 0):
            quad_degree_correction = 0 
        elif(test_point[0] < 0 and test_point[1] >= 0):
            quad_degree_correction = 360
        else:
            quad_degree_correction = 180
        
        #convert to polar coordinates 
        if(test_point[1] == 0 and test_point[0] >= 0):
            x_by_y = float('inf')
        elif(test_point[1] == 0 and test_point[0] < 0):
            x_by_y = float('-inf')
        else:
            x_by_y = test_point[0]/float(test_point[1])
            
        #print "x/y",x_by_y
        test_point_rad = math.atan(x_by_y)
        
        #print "test rad angle",test_point_rad
        
        # convert angle in radians from the anchor line to degrees from anchor line
        test_point_deg = math.degrees(test_point_rad)
        
        #adjust the degree angle according to the quadrant of cartesian point
        test_point_deg = quad_degree_correction + test_point_deg
        
        test_point_rsquare = (test_point[0])**2 + test_point[1]**2
        
        #print "test point deg ",test_point_deg," test point rsquare ",test_point_rsquare
        if(test_point_deg <= filled_angle and test_point_rsquare <= radius_square): # check the edge cases
            return True
        return False
        

# read input file 
#input_file = "progress_pie_example_input.txt"; # example input
input_file = "progress_pie.txt"; # real input
output_file = "output.txt";

fi = open(input_file,'r');
fo = open(output_file, 'w');

case_count = int(fi.readline());
#print("case_count="+str(case_count));
#cases = fi.read();
curr_line = 1;
start_time = time.time()
for line in fi:
	#print("case="+line);
    
    ans = is_in_progress_chart(line)
    end_time = time.time()
    
    if(ans and curr_line <= case_count):
        print "Case #"+str(curr_line)+": " +"black"
        fo.write("Case #"+str(curr_line)+": " +"black\n")
         
    elif(not ans and curr_line <= case_count):
        print "Case #"+str(curr_line)+": " +"white"
        fo.write("Case #"+str(curr_line)+": " +"white\n")
    curr_line += 1
end_time = time.time()
print "time taken to solve 1000",end_time-start_time," seconds"
fo.close()



"""
tests 
"""

ans =  is_in_progress_chart("25 105 100")  
assert ans == False

ans =  is_in_progress_chart("55 105 105")  
assert ans == False

ans =  is_in_progress_chart("75 100 105") 
assert ans == False

ans =  is_in_progress_chart("100 105 105")  
assert ans == False

# progress 25%
ans =  is_in_progress_chart("25 55 55") # first quad (after shifting origin) 
assert ans == True
ans = is_in_progress_chart("25 55 35") # second quad (after shifting origin)
assert ans == False

ans = is_in_progress_chart("25 45 45") # third quad (after shifting origin)
assert ans == False

ans = is_in_progress_chart("25 45 50") # start of 4th quad i.e 270 deg (after shifting origin)
assert ans == False
ans = is_in_progress_chart("25 55 50") # start of 2nd quad i.e 90 deg (after shifting origin)
assert ans == True

ans = is_in_progress_chart("25 55 45") # 2nd quad (after shifting origin)
assert ans == False 

ans = is_in_progress_chart("25 50 55") # start of 1st quad (after shifting origin)
assert ans == True 

ans = is_in_progress_chart("25 50 35") # start of 3rd quad (after shifting origin)
assert ans == False 

ans = is_in_progress_chart("20 50 50") # origin (after shifting origin)
assert ans == True

ans = is_in_progress_chart("25 45 55") # 4th quad (after shifting origin)
assert ans == False

# progress 50 %

ans =  is_in_progress_chart("50 55 55") # first quad (after shifting origin) 
assert ans == True
ans = is_in_progress_chart("50 55 35") # second quad (after shifting origin)
assert ans == True

ans = is_in_progress_chart("50 45 45") # third quad (after shifting origin)
assert ans == False

ans = is_in_progress_chart("50 45 50") # start of 4th quad i.e 270 deg (after shifting origin)
assert ans == False
ans = is_in_progress_chart("50 55 50") # start of 2nd quad i.e 90 deg (after shifting origin)
assert ans == True

ans = is_in_progress_chart("50 55 45") # 2nd quad (after shifting origin)
assert ans == True 

ans = is_in_progress_chart("50 50 55") # start of 1st quad (after shifting origin)
assert ans == True 

ans = is_in_progress_chart("50 50 35") # start of 3rd quad 180 deg (after shifting origin)
assert ans == True 

ans = is_in_progress_chart("50 50 50") # origin (after shifting origin)
assert ans == True

ans = is_in_progress_chart("50 45 55") # 4th quad (after shifting origin)
assert ans == False

# progress 75 %

ans =  is_in_progress_chart("75 55 55") # first quad (after shifting origin) 
assert ans == True
ans = is_in_progress_chart("75 55 35") # second quad (after shifting origin)
assert ans == True

ans = is_in_progress_chart("75 45 45") # third quad (after shifting origin)
assert ans == True

ans = is_in_progress_chart("75 45 50") # start of 4th quad i.e 270 deg (after shifting origin)
assert ans == True
ans = is_in_progress_chart("75 55 50") # start of 2nd quad i.e 90 deg (after shifting origin)
assert ans == True

ans = is_in_progress_chart("75 55 45") # 2nd quad (after shifting origin)
assert ans == True 

ans = is_in_progress_chart("75 50 55") # start of 1st quad (after shifting origin)
assert ans == True 

ans = is_in_progress_chart("75 50 35") # start of 3rd quad 180 deg (after shifting origin)
assert ans == True 

ans = is_in_progress_chart("75 50 50") # origin (after shifting origin)
assert ans == True

ans = is_in_progress_chart("75 45 55") # 4th quad (after shifting origin)
assert ans == False


# progress 100%

ans =  is_in_progress_chart("100 55 55") # first quad (after shifting origin) 
assert ans == True
ans = is_in_progress_chart("100 55 35") # second quad (after shifting origin)
assert ans == True

ans = is_in_progress_chart("100 45 45") # third quad (after shifting origin)
assert ans == True

ans = is_in_progress_chart("100 45 50") # start of 4th quad i.e 270 deg (after shifting origin)
assert ans == True
ans = is_in_progress_chart("100 55 50") # start of 2nd quad i.e 90 deg (after shifting origin)
assert ans == True

ans = is_in_progress_chart("100 55 45") # 2nd quad (after shifting origin)
assert ans == True 

ans = is_in_progress_chart("100 50 55") # start of 1st quad (after shifting origin)
assert ans == True 

ans = is_in_progress_chart("100 50 35") # start of 3rd quad 180 deg (after shifting origin)
assert ans == True 

ans = is_in_progress_chart("100 50 50") # origin (after shifting origin)
assert ans == True

ans = is_in_progress_chart("100 45 55") # 4th quad (after shifting origin)
assert ans == True

#try out divide by zero case and border cases
ans = is_in_progress_chart("100 50 50") # 4th quad (after shifting origin)
assert ans == True
ans = is_in_progress_chart("0 50 50") # 4th quad (after shifting origin)
assert ans == False