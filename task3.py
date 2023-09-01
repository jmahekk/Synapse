def explode_chains(encoded_lists):
    output=[]
    for i in encoded_lists:
        new=remove_consecutive(i)
        #print(new)  basically prints sublist [4,6] etc
        output.append(new)

    return output


def remove_consecutive(i):
    output=[]

    index=0
    length=len(i)

    while index<length:
        if index+2<length:
            if (i[index]-i[index+1]==-1 and
                i[index+1]-i[index+2]==-1):
                
                if (index+3)<length:
                    index=index+3
                else:
                    index=length+1
            else:
               
                output.append(i[index])
                index=index+1
        else:
            
            output=output+i[index:]
            index=length+1

    return output


encoded_lists=[
    [1,2,3,4,6],
    [5,7,8,9,15],
    [12,14,16,18],
    [10,11,12,13,16,17,18,20]
]
result=explode_chains(encoded_lists)

print(result)