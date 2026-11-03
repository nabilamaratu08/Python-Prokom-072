guests = ['Nabila Fakhriya', 'Nanda Artika', 'Aira Putri',
          'Kemala Dewi', 'Nasyauqi Isnani', 'Devreza']
 
print("Sorry, the new table won't arrive in time. I can invite only two people.")
 
# pop() sampai tersisa dua nama
removed = guests.pop()
print(f"Sorry {removed}, I can't invite you to dinner.")
removed = guests.pop()
print(f"Sorry {removed}, I can't invite you to dinner.")
removed = guests.pop()
print(f"Sorry {removed}, I can't invite you to dinner.")
removed = guests.pop()
print(f"Sorry {removed}, I can't invite you to dinner.")
 
# dua orang yang masih diundang
print(f"\n{guests[0]}, you are still invited to dinner!")
print(f"{guests[1]}, you are still invited to dinner!")
 
# del untuk mengosongkan list
del guests[0]
del guests[0]
print(f"\n{guests}")