SPOTIPY_CLIENT_ID = [hidden]
SPOTIPY_CLIENT_SECRET = [hidden]
SPOTIPY_URI = [hidden]

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import helper
import gui
from PIL import Image
from urllib.request import urlopen

scope = "user-top-read"

user_spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_URI, scope=scope))

current_user_top_artists = user_spotify.current_user_top_artists(limit=20, offset=0)

user_genre = gui.user_genre
user_mood = gui.user_mood

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

def albums(top_artists2=find_top_artists()):
    artist_albums = {}
    for name in top_artists2:
        for genres in top_artists2[name]:
            if user_genre == genres:
                search = user_spotify.search(q='artist:' + name, type='artist')
                artist_id = search['artists']['items'][0]['id']
                aalbums = user_spotify.artist_albums(artist_id, album_type='album')
                albums2 = []
                for album in range(len(aalbums)):
                    albums2.append(aalbums['items'][album]['name'])
                artist_albums[name] = albums2
    return artist_albums

#def songs(albums=albums()):
#    songs = {}
#    for artist in albums:
#        total_list = []
#        for song in range(len(albums[artist])):
#            search = user_spotify.search(q='album:' + albums[artist][song], type='album')
#            album_id = search['albums']['items'][0]['id']
#            album_tracks = user_spotify.album_tracks(album_id)
#            track_total = album_tracks['total']
#            album_name = albums[artist][song]
#            for song in range(track_total):
#                song_name = album_tracks['items'][song]['name']
#                search2 = user_spotify.search(q='track:' + song_name, type='track')
#                for num in range(len(search2['tracks']['items'])):
#                    specifics = {}
#                    artist_name = search2['tracks']['items'][num]['artists'][0]['name']
#                    track_album_name = search2['tracks']['items'][num]['album']['name']
#                    id = search2['tracks']['items'][num]['id']
#                    audio_features = user_spotify.audio_features(id)
#                    if artist_name == artist and track_album_name == album_name:
#                        danceability = audio_features[0]['danceability']
#                        energy = audio_features[0]['energy']
#                        valence = audio_features[0]['valence']
#                        specifics[album_name] = abs(user_danceability - danceability) + abs(user_energy - energy) + abs(user_valence - valence)
#                        total_list.append(specifics)
#        songs[artist] = total_list
#    return songs
main_dict = {
    'Travis Scott': {'UTOPIA': 'HYAENA'},
    'Drake': {'Views': 'Childs Play'},
    'Kendrick Lamar': {'DAMN.': 'BLOOD.'},
    '21 Savage': {'American Dream': 'Dark Days'},
}
cover_art_dict = {
    'Travis Scott': user_spotify.track('5iUTVWEbtWJUTp2numATGg')['album']['images'][0]['url'],
    'Drake': user_spotify.track('3NxAG2ni1lLa8RKL6a0INc')['album']['images'][0]['url'],
    'Kendrick Lamar': user_spotify.track('1n4jwRVXdkK2U34nBDUKKT')['album']['images'][0]['url'],
    '21 Savage': user_spotify.track('18eTC8x3COqWP7od8kW3KQ')['album']['images'][0]['url'],
}

file = open('top5songs.txt', 'w')
for artist in main_dict:
    for track in main_dict[artist]:
        list2 = [artist, track, main_dict[artist][track], cover_art_dict[artist]]
        file.write(f"{list2}\n")

file.close()

#Image.Image.show(Image.open(urlopen('https://i.scdn.co/image/ab67616d0000b2739162764a6017634fb155498d')))
