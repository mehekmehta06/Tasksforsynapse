# -*- coding: utf-8 -*-


jumbled_superheroes=['DocTor_sTRAngE','sPidERmaN','MoON_KnigHT','caPTAIN_aMERIca','hULK']

indices=[]
for index,element in enumerate(jumbled_superheroes):
    indices.append(index)
    
#print(indices)

decoded_names=[]
no_underscore= [initial.replace('_', ' ') for initial in jumbled_superheroes]
for initial in no_underscore:
   
    decoded_names.append(initial.lower())
           
print(decoded_names)

 

length= lambda x : len(x)


name_lengths = list(map(length, decoded_names))
#print(name_lengths)

indices.sort(key=lambda x: name_lengths[x])
#print(indices)

new_jumbled_superheroes= [no_underscore[i] for i in indices]

text_title=[text.title() for text in new_jumbled_superheroes]

print('Phase 5 Kickoff list:')
for index,text in enumerate(text_title, start=1):
    print(f'{index}.{text}')
  






    
    

