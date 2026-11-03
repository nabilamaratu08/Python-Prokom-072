def make_album(artist, title, songs=None):
    """Return a dictionary describing a music album."""
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album
 
 
print(make_album('cortis', 'wyw'))
print(make_album('olivia rodrigo', 'drop dead'))
print(make_album('R city', 'locked away', songs=10))