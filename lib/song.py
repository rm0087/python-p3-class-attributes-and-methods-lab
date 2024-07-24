class Song:
    count = 0
    genres = []
    genre_count = {}
    artists = []
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.name = name
        self.artist = artist
        self.genre = genre
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre, increment=1):
        if genre in cls.genre_count.keys():
            cls.genre_count[genre] += increment
        else:
            cls.genre_count[genre] = increment
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist, increment=1):
        if artist in cls.artist_count.keys():
            cls.artist_count[artist] += increment
        else:
            cls.artist_count[artist] = increment
            cls.artists.append(artist)
            

    
    
