from random import randint
lst=['0001','0011','0101','1011','1101','1111']

diff=-9999
min_index=0
while(diff!=0):
    int_lst=[int(ele,2) for ele in lst]
    print(f'original int_lst is {int_lst}')
    while(len(int_lst)!=2):
        max_index=len(int_lst)-1
        i=randint(min_index,max_index)
        j=randint(min_index,max_index)
        #print(f'i is {i}, j is {j}')
        #print(f'int_lst[i] is {int_lst[i]},int_lst[j] is {int_lst[j]}')
        addn=int_lst[i]+int_lst[j]
        new_lst=[value for index, value in enumerate(int_lst) if index not in {i,j}]
        int_lst=[addn]+new_lst
        print(f'new int_lst is {int_lst}')
    print(f'int_lst after reduction is {int_lst}')
    diff=int_lst[0]-int_lst[1]
    if diff==0:
     print(f'diff is {diff}')

print('done')

