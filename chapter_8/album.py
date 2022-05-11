def make_album(artist_name, album_title, num_of_song = None):
    album = {'artist name': artist_name, 'title': album_title}
    if num_of_song:
        album['number of songs'] = num_of_song
    return album
album_info = make_album('john', 'love')
print(album_info)
