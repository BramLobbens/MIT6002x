# MIT 6.00.2x Midterm Problem 3

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """

    first_song = songs[0]
    songs_copy = songs[1:]
    playlist = []
    disk_size = first_song[2]

    if disk_size > max_size:
        return []

    def get_smallest(songs_copy, playlist):
        size = max_size - first_song[2]
        smallest_song = None
        for song in songs_copy:
            if song[2] < size and song[0] not in playlist:
                smallest_song = song[0]
                size = song[2]
        return smallest_song, size

    while disk_size <= max_size:
        next_song, song_size = get_smallest(songs_copy, playlist)
        if (disk_size + song_size > max_size) or next_song == None:
            break
        playlist += [next_song]
        disk_size += song_size

    return [first_song[0]] + playlist