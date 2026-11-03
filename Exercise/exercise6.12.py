favorite_languages = {
    'james': {'languages': ['python', 'rust'], 'years': 3},
    'juhoon': {'languages': ['c'], 'years': 5},
    'seonghyon': {'languages': ['rust', 'go', 'python'], 'years': 2},
    'keonho': {'languages': ['python', 'haskell'], 'years': 7},
}
 
for name, info in favorite_languages.items():
    print(f"{name.title()} has been programming for {info['years']} years.")
    print("  Favorite languages:")
    for language in info['languages']:
        print(f"    - {language.title()}")
    print()