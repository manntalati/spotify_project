SPOTIPY_CLIENT_ID = [hidden]
SPOTIPY_CLIENT_SECRET = [hidden]
SPOTIPY_URI = [hidden]
SCOPE = 'user-top-read'

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import helper

user_spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_URI, scope=SCOPE))

current_user_top_artists = user_spotify.current_user_top_artists(limit=10, offset=0)

genre_file = open('genre.txt', 'r')
mood_file = open('mood.txt', 'r')

user_genre = genre_file.readline()
user_mood = mood_file.readline()

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
    global total_list, cover_list
    total_list = {}
    cover_list = {}
    for artist in songs:
        all_id_list = []
        for song in range(len(songs[artist])):
            for id in songs[artist][song]:
                all_id_list.append(user_spotify.audio_features(songs[artist][song][id]))
        
        specifics = {}
        cover_specifics = {}
        for song2 in range(len(all_id_list)):
            danceability = all_id_list[song2][0]['danceability']
            energy = all_id_list[song2][0]['energy']
            valence = all_id_list[song2][0]['valence']
            id2 = all_id_list[song2][0]['id']
            if abs(user_danceability - danceability) + abs(user_energy - energy) + abs(user_valence - valence) < 0.4:
                track = user_spotify.track(id2)
                cover_art_url = track['album']['images'][0]['url']
                song_name = track['name']
                album_name = track['album']['name']
                specifics[album_name] = song_name
                total_list[artist] = specifics
                cover_specifics[song_name] = cover_art_url
                cover_list[artist] = cover_specifics
    return total_list

new_songs()

file = open('topsongs.txt', 'w')
for artist in total_list:
    for track in total_list[artist]:
        list2 = [artist, track, total_list[artist][track], cover_list[artist][total_list[artist][track]]]
        file.write(f"{list2}\n")

file.close()