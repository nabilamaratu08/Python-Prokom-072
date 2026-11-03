favorite_languages = {
    'james': 'python',
    'juhoon': 'c',
    'seonghyon': 'rust',
    'keonho': 'python',
}
 
people_to_poll = ['james', 'juhoon', 'seonghyon', 'keonho']
 
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you for responding to the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take our poll!")