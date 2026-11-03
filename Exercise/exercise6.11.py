cities = {
    'tokyo': {
        'country': 'japan',
        'population': 14000000,
        'fact': 'It is one of the largest cities in the world.',
    },
    'reykjavik': {
        'country': 'iceland',
        'population': 140000,
        'fact': 'It is the northernmost capital of a sovereign state.',
    },
    'santiago': {
        'country': 'chile',
        'population': 6000000,
        'fact': 'The Andes mountains are visible from the city.',
    },
}
 
for city, info in cities.items():
    print(f"\n{city.title()}")
    print(f"  Country: {info['country'].title()}")
    print(f"  Population: about {info['population']:,}")
    print(f"  Fact: {info['fact']}")