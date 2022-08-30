print('my python pet ')


cat = {
'name' : 'pypet',
'age' : 5,
'weight' : 9.5,
'hungry' : True,
'photo' : '=^o.o^=__',
}


def feed(pet):
 if pet['hungry'] == True:
    pet['hungry'] = False
    pet['weight'] = pet['weight'] + 1 

 else:
    print ('The Pypet is not hungry!')

print (cat)
feed(cat)
print (cat)
