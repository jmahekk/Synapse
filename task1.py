jumbled_superheroes = ['DocToR_sTRAngE','sPidERmaN','MoON_KnigHT','caPTAIN_aMERIca','hULK']

print(f"Jumbled Superheroes are {jumbled_superheroes}")

indices=[]
decoded_names =[]
for i,value in enumerate(jumbled_superheroes):
    indices.append(i)
    decoded_names.append(value)

#print(indices)
#print(decoded_names)

#converting to lowercase
for i in range(len(decoded_names)):
    decoded_names[i] = decoded_names[i].lower()
#print(decoded_names)

#replacing _ with spaces
decoded_names = [e.replace("_", " ") for e in decoded_names]
#print(decoded_names)

name_lengths=list(map(lambda item: len(item), decoded_names))
#print(name_lengths)

indices.sort(key = lambda item: name_lengths[item])
#print(indices)

decoded_names = [i.title() for i in decoded_names]
#print(decoded_names)

print("Phase 5 Kickoff List:")

for i, value in enumerate(indices):
    print(f"{i + 1}. {decoded_names[value]}")