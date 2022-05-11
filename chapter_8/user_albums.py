def make_album(artist_name, album_title):
    while True:
        print("\nEnter 'quit' to end the program ")
        artist_name = input("Artist name: ")
        if artist_name == 'quit':
            break
        album_title = input("Album Title: ")
        if album_title == 'quit':
            break
        album = {'artist name': artist_name, 'album_title': album_title}
    return album
album_info = make_album('john', 'love')
print(album_info)
