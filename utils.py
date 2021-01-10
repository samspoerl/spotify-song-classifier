def songs_and_features(auth, playlist_id):
    '''Return the songs and their audio features from a Spotify playlist'''

    # Import dependencies
    import pandas as pd

    # Playlist JSON
    results = auth.playlist_tracks(playlist_id=playlist_id, market='US')

    # Name of playlist to label song genre
    pl_name = results['name']

    # Sub JSONs
    tracks = results['tracks']
    items = tracks['items']

    # Issues slicing; convert to df first
    df_items = pd.DataFrame.from_records(items)

    # DataFrame of songs including id for audio feature lookup
    df_songs = pd.DataFrame.from_records(df_items['track'])

    # Add playlist ID and name to dataset
    df_songs['playlist_id'] = playlist_id
    df_songs['playlist_name'] = pl_name

    # Get song IDs into list
    song_ids = [song for song in df_songs['id']]

    # Get audio features to be used to build model
    features = auth.audio_features(tracks=song_ids)
    df_features = pd.DataFrame.from_records(features)

    # Get name and popularity from left and audio features from right
    df_songs_and_features = df_songs.merge(df_features, on=['id', 'uri'], how='outer', suffixes=[None, '_y'])

    # Fields for model
    fields = [
        'playlist_id',
        'playlist_name',
        'id',
        'name',
        'popularity',
        'acousticness',
        'danceability',
        'duration_ms',
        'energy',
        'instrumentalness',
        'key',
        'liveness',
        'loudness',
        'mode',
        'speechiness',
        'tempo',
        'time_signature',
        'valence'
    ]

    # Sliced DF
    df = df_songs_and_features[fields]

    return df