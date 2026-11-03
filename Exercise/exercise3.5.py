guests = ['Nanda Artika', 'Aira Putri', ' Nasyauqi Isnani']
 
print(f"Dear {guests[0]}, you are invited to dinner at my house.")
print(f"Dear {guests[1]}, you are invited to dinner at my house.")
print(f"Dear {guests[2]}, you are invited to dinner at my house.")
 
# Satu tamu tidak bisa datang
print(f"\n{guests[1]} can't make it to the dinner.")
guests[1] = 'Kemala Dewi'
 
print(f"\nDear {guests[0]}, you are invited to dinner at my house.")
print(f"Dear {guests[1]}, you are invited to dinner at my house.")
print(f"Dear {guests[2]}, you are invited to dinner at my house.")