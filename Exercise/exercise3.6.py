guests = ['Nanda Artika', 'Kemala Dewi', 'Nasyauqi Isnani']
 
print("I found a bigger table!")
 
guests.insert(0, 'Nabila Fakhriya')                 # awal list
guests.insert(len(guests) // 2, 'Aira Putri')  # tengah list
guests.append('Devreza')                 # akhir list
 
print(f"Dear {guests[0]}, you are invited to dinner at my house.")
print(f"Dear {guests[1]}, you are invited to dinner at my house.")
print(f"Dear {guests[2]}, you are invited to dinner at my house.")
print(f"Dear {guests[3]}, you are invited to dinner at my house.")
print(f"Dear {guests[4]}, you are invited to dinner at my house.")
print(f"Dear {guests[5]}, you are invited to dinner at my house.")