places = ['Japan', 'Iceland', 'Korea', 'China', 'Egypt']
 
print("Original order:")
print(places)
 
print("\nsorted() alphabetical:")
print(sorted(places))
print("Still original:")
print(places)
 
print("\nsorted() reverse alphabetical:")
print(sorted(places, reverse=True))
print("Still original:")
print(places)
 
places.reverse()
print("\nAfter reverse():")
print(places)
 
places.reverse()
print("\nAfter reverse() again:")
print(places)
 
places.sort()
print("\nAfter sort():")
print(places)
 
places.sort(reverse=True)
print("\nAfter sort(reverse=True):")
print(places)