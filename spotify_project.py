SPOTIPY_CLIENT_ID = [hidden]
SPOTIPY_CLIENT_SECRET = [hidden]
SPOTIPY_URI = 'http://localhost:3000/callback'

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import helper

scope = "user-top-read"

user_spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_URI, scope=scope))

current_user_top_artists = user_spotify.current_user_top_artists(limit=20, offset=0)

user_genre = input("What genre would you like to listen to? ")
user_mood = input("What mood would you like to listen to? ")

valence=helper.user_valence(user_mood)
danceability=helper.user_danceability(user_mood)
energy=helper.user_energy(user_mood)

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
        name_list = []
        for album in range(len(albums[track])):
            search = user_spotify.search(q='album:' + albums[track][album], type='album')
            album_id = search['albums']['items'][0]['id']
            album_tracks = user_spotify.album_tracks(album_id)
            track_total = album_tracks['total']
            for song in range(track_total):
                specifics = {}
                specifics[albums[track][album]] = album_tracks['items'][song]['name']
                song_list.append(specifics)
                name_list.append(track)
        songs[track] = song_list
    return songs

def find_song_id(songs=songs()):
    new_songs = songs
    for artist in songs:
        for song in range(len(songs[artist])):
            for track in songs[artist][song]:
                search = user_spotify.search(q='track:' + songs[artist][song][track], type='track')
                print(search)
                #! FIXXX
                for num in range(len(search['tracks']['items'])):
                    artist_name = search['tracks']['items'][num]['artists'][0]['name']
                    album_name = search['tracks']['items'][num]['album']['name']
                    if artist_name == songs[artist] and album_name == songs[artist][song]:
                        new_songs[artist][song] = search['tracks']['items'][num]['id']
    return new_songs

def top5(songs=songs()):
    for artist in songs:
        for song in range(len(songs[artist])):
            for track in songs[artist][song]:
                search = user_spotify.search(q='track:' + songs[artist][song][track], type='track')
                print(search['tracks'])

#print(find_song_id())
#results = user_spotify.search(q='track:' + songs()['Travis Scott'][0]['UTOPIA'], type='track')
#print(len(results['tracks']))
#print(results['tracks']['items'][0]['artists'][0]['name'])
#print(results['tracks']['items'][0]['id'])
#print(results['tracks']['items'][0]['album']['name'])

#* 1. Find the song id for each spotify track from the album through search and make sure the artist and album are the same
#* 2. Find the top5 songs that would fit based on the valence, energy, danceability through the process below (absolute value of each variable and add together)
#* 3. ^^also incorporate margin of error
#* 4. Make tkinter screen with buttons that would corespond to each item (mood should be selected based on buttons same with genre)
#* 5. this should help spit back out 5 songs that give song, artist, and album

#print(search)
#? use margin of error to find value and then find the top 5 values that would fit best either through iterating a list or something

# absoulte value of valence - valence, energy - energy, danceability - danceability
# add these three together and the lowest value would mean the best song

#? Take the albums made by the artists and check all of the songs in the albums to see if they will fit the requirement
#? if songs fit in the second function

#danceability = print(user_spotify.audio_features("6rqhFgbbKwnb9MLmUQDhG6")[0]['danceability'])
#valence = print(user_spotify.audio_features("6rqhFgbbKwnb9MLmUQDhG6")[0]['valence'])
#energy = print(user_spotify.audio_features("6rqhFgbbKwnb9MLmUQDhG6")[0]['energy'])