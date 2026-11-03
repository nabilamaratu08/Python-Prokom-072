favorite_places = {
    'juhoon': ['Bali', 'Yogyakarta'],
    'seonghyon': ['Surabaya'],
    'keonho': ['Lombok', 'Raja Ampat', 'Bromo'],
}
 
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place}")