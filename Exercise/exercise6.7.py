person_1 = {'first_name': 'Juhoon', 'last_name': 'kim',
            'age': 18, 'city': 'Surabaya'}
person_2 = {'first_name': 'seonghyon', 'last_name': 'eom',
            'age': 17, 'city': 'Bandung'}
person_3 = {'first_name': 'keonho', 'last_name': 'ahn',
            'age': 17, 'city': 'Jakarta'}
 
people = [person_1, person_2, person_3]
 
for person in people:
    for key, value in person.items():
        print(f"{key.title()}: {value}")
    print()