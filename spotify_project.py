SPOTIPY_CLIENT_ID = '482ddfd255024d6ea41fd723acf0f6be'
SPOTIPY_CLIENT_SECRET = '47dee8b88d2c42af93fb03a03f82193d'
SPOTIPY_URI = 'http://localhost:3000/callback'

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import helper
import gui

#* SPOTIFY_PROJECT TASKS
#TODO: 2. Find the top5 songs that would fit based on the valence, energy, danceability through the process below (absolute value of each variable and add together)
#* 3. ^^also incorporate margin of error
#* 5. this should help spit back out 5 songs that give song, artist, and album
#* 6. when recommending songs make sure to ensure that the same one isnt already there (in the set)

scope = "user-top-read"

user_spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_URI, scope=scope))

current_user_top_artists = user_spotify.current_user_top_artists(limit=20, offset=0)

#user_genre = page.user_genre
#user_mood = page.user_mood

user_genre = input("What genre would you like to listen to? ")
user_mood = input("What mood would you like to listen to? ")

user_valence = helper.user_valence(user_mood)
user_danceability = helper.user_danceability(user_mood)
user_energy = helper.user_energy(user_mood)

def find_top_artists():
    top_artists = {}
    for num in range(len(current_user_top_artists['items'])):
        genres = []
        for num2 in range(len(current_user_top_artists['items'][num]['genres'])):
            genres.append(current_user_top_artists['items'][num]['genres'][num2])
        top_artists[(current_user_top_artists['items'][num]['name'])] = genres
    return top_artists

def artists(top_artists2=find_top_artists()):
    artists_to_use = []
    for name in top_artists2:
        for genres in top_artists2[name]:
            if user_genre == genres:
                artists_to_use.append(name)
    return artists_to_use

def albums(artists=artists()):
    artist_albums = {}
    for name in artists:
        search = user_spotify.search(q='artist:' + name, type='artist')
        artist_id = search['artists']['items'][0]['id']
        aalbums = user_spotify.artist_albums(artist_id, album_type='album')
        albums2 = []
        for album in range(len(aalbums)):
            albums2.append(aalbums['items'][album]['name'])
        artist_albums[name] = albums2
    return artist_albums

def songs(albums=albums()):
    songs = {}
    for track in albums:
        song_list = []
        for album in range(len(albums[track])):
            search = user_spotify.search(q='album:' + albums[track][album], type='album')
            album_id = search['albums']['items'][0]['id']
            album_tracks = user_spotify.album_tracks(album_id)
            track_total = album_tracks['total']
            for song in range(track_total):
                specifics = {}
                specifics[albums[track][album]] = album_tracks['items'][song]['name']
                song_list.append(specifics)
        songs[track] = song_list
    return songs

def find_song_id(songs=songs()):
    new_songs = {}
    for artist in songs:
        id_list = []
        for song in range(len(songs[artist])):
            for track in songs[artist][song]:
                search = user_spotify.search(q='track:' + songs[artist][song][track], type='track')
                for num in range(len(search['tracks']['items'])):
                    dict2 = {}
                    artist_name = search['tracks']['items'][num]['artists'][0]['name']
                    album_name = search['tracks']['items'][num]['album']['name']
                    if artist_name == artist and album_name == track:
                        dict2[album_name] = search['tracks']['items'][num]['id']
                        id_list.append(dict2)
        new_songs[artist] = id_list
    return new_songs

def top5(songs=find_song_id()):
    top5_songs = set()
    for artist in songs:
        for song in range(len(songs[artist])):
            for id in songs[artist][song]:
                search = user_spotify.search(q='track:' + songs[artist][song], type='track')
                print(search['tracks'])

#print(find_song_id())
print(user_spotify.audio_features(find_song_id()['Travis Scott'][0]))
results = user_spotify.search(q='track:' + songs()['Travis Scott'][0]['UTOPIA'], type='track')
#print(len(results['tracks']))
#print(results['tracks']['items'][0])
print(results['tracks']['items'][0]['id'])
print(user_spotify.audio_features(results['tracks']['items'][0]['id']))
#print(results['tracks']['items'][0]['album']['name'])

#? use margin of error to find value and then find the top 5 values that would fit best either through iterating a list or something

# absoulte value of valence - valence, energy - energy, danceability - danceability
# add these three together and the lowest value would mean the best song

#? check all of the songs in the albums to see if they will fit the requirement
#? if songs fit in the second function

#danceability = print(user_spotify.audio_features("6rqhFgbbKwnb9MLmUQDhG6")[0]['danceability'])
#valence = print(user_spotify.audio_features("6rqhFgbbKwnb9MLmUQDhG6")[0]['valence'])
#energy = print(user_spotify.audio_features("6rqhFgbbKwnb9MLmUQDhG6")[0]['energy'])