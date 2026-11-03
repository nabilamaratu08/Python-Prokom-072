foods = ('rice', 'fried chicken', 'noodles', 'salad', 'soup')
 
for food in foods:
    print(food)
 
# Mencoba mengubah item tuple -> ditolak Python
try:
    foods[0] = 'bread'
except TypeError as error:
    print(f"\nPython rejected the change: {error}")
 
# Menu baru: tuple ditulis ulang (bukan diubah)
foods = ('rice', 'fried chicken', 'noodles', 'pasta', 'pudding')
 
print("\nRevised menu:")
for food in foods:
    print(food)