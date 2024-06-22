SPOTIPY_CLIENT_ID = '482ddfd255024d6ea41fd723acf0f6be'
SPOTIPY_CLIENT_SECRET = '47dee8b88d2c42af93fb03a03f82193d'
SPOTIPY_URI = 'http://127.0.0.1:9090'

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import helper
import time
import gui

#* SPOTIFY_PROJECT TASKS
#TODO: 2. Find the top5 songs that would fit based on the valence, energy, danceability through the process below (absolute value of each variable and add together)
#* 3. ^^also incorporate margin of error
#* 5. this should help spit back out 5 songs that give song, artist, and album
#* 6. when recommending songs make sure to ensure that the same one isnt already there (in the set)

scope = "user-top-read"

user_spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_URI, scope=scope))

current_user_top_artists = user_spotify.current_user_top_artists(limit=20, offset=0)

user_genre = gui.user_genre
user_mood = gui.user_mood

print(user_genre)
print(user_mood)

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
    for artist in albums:
        id_list = []
        for song in range(len(albums[artist])):
            search = user_spotify.search(q='album:' + albums[artist][song], type='album')
            album_id = search['albums']['items'][0]['id']
            album_tracks = user_spotify.album_tracks(album_id)
            track_total = album_tracks['total']
            album_name = albums[artist][song]
            for song in range(track_total):
                song_name = album_tracks['items'][song]['name']
                search2 = user_spotify.search(q='track:' + song_name, type='track')
                for num in range(len(search2['tracks']['items'])):
                    specifics = {}
                    artist_name = search2['tracks']['items'][num]['artists'][0]['name']
                    track_album_name = search2['tracks']['items'][num]['album']['name']
                    if artist_name == artist and track_album_name == album_name:
                        specifics[album_name] = search2['tracks']['items'][num]['id']
                        id_list.append(specifics)
        songs[artist] = id_list
    return songs

def new_songs(songs=songs()):
    updated_songs = {}
    for artist in songs:
        total_list = []
        for song in range(len(songs[artist])):
            for id in songs[artist][song]:
                dict2 = {}
                time.sleep(30)
                audio_features = user_spotify.audio_features(songs[artist][song][id])
                danceability = audio_features[0]['danceability']
                energy = audio_features[0]['energy']
                valence = audio_features[0]['valence']
                dict2[user_spotify.track(songs[artist][song][id])['name']] = abs(user_danceability - danceability) + abs(user_energy - energy) + abs(user_valence - valence)
                total_list.append(dict2)
        updated_songs[artist] = total_list
    return updated_songs

def top5(songs=new_songs()):
    total_list = []
    top5_list = []
    for artist in songs:
        for song in range(len(songs[artist])):
            for total in songs[artist][song]:
                if songs[artist][song][total] > -0.4 and songs[artist][song][total] < 0.4:
                    total_list.append(songs[artist][song][total])

    for num in range(5):
        min_num = min(total_list)
        top5_list.append(min_num)
        total_list.remove(total_list.index(min_num))

    return top5_list

print(top5())

#find what is closest to 0 in the updated songs dict
# add these three together and the lowest value would mean the best song

# CONSOLIDATE NEW SONGS, FIND_SONG_ID, SONGS

#? use margin of error to find value and then find the top 5 values that would fit best either through iterating a list or something
#? check all of the songs in the albums to see if they will fit the requirement
#? if songs fit in the second function