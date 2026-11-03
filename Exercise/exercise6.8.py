pet_1 = {'animal': 'horse', 'owner': 'juhoon'}
pet_2 = {'animal': 'bird', 'owner': 'seonghyon'}
pet_3 = {'animal': 'cat', 'owner': 'keonho'}
 
pets = [pet_1, pet_2, pet_3]
 
for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value}")
    print()