# -*- coding: utf-8 -*-

list1=['0001','0011','0101','1011','1101','1111']

new_list = [int(b, 2) for b in list1]
#print(new_list)
new_list.sort()


for i in range(0,len(new_list)-2):
    small=new_list.pop(0)
    sec_small=new_list.pop(0)
    
    new_number= small+ sec_small
    new_list.append(new_number)

new_list.sort(reverse=True)

diff= new_list[0]- new_list[1]
print(diff)

          

            
    





  



    


