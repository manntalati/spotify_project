moods = {
    "happy": {
        "valence": 1.0,
        "danceability": 1.0,
        "energy": 0.7,
    },
    "sad": {
        "valence": 0.0,
        "danceability": 0.0,
        "energy": 0.0,
    },
    "anger": {
        "valence": 0.0,
        "danceability": 0.5,
        "energy": 1.0,
    },
    "energetic": {
        "valence": 0.7,
        "danceability": 0.8,
        "energy": 1.0,
    },
    "relaxation": {
        "valence": 0.7,
        "danceability": 0.0,
        "energy": 0.0,
    },
    "triumph": {
        "valence": 1.0,
        "danceability": 0.5,
        "energy": 0.7,
    },
}

def user_valence(mood):
    for x in moods:
        if x == mood:
            valence = moods[x]['valence']
    return valence

def user_danceability(mood):
    for x in moods:
        if x == mood:
            danceability = moods[x]['danceability']
    return danceability

def user_energy(mood):
    for x in moods:
        if x == mood:
            energy = moods[x]['energy']
    return energy