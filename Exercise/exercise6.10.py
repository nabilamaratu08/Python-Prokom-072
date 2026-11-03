favorite_numbers = {
    'juhoon': [7, 14],
    'seonghyon': [13],
    'keonho': [3, 9, 27],
    'james': [21, 5],
    'martin': [9, 1, 100],
}
 
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")