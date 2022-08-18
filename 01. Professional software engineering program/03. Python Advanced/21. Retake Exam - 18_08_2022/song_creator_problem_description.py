def add_songs(*args):
    album = {}

    for element in args:
        song_title = element[0]
        song_lyrics = element[1]

        if song_title not in album:
            album[song_title] = []
            album[song_title] = song_lyrics
        else:
            album[song_title].extend(song_lyrics)

    total_result = ''

    for title, lyrics in album.items():
        result = f'- {title}' + '\n'
        if lyrics:
            for text in lyrics:
                result += text + '\n'

        total_result += result

    return total_result


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))