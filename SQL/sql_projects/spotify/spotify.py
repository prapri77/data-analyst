from spotipy.oauth2 import SpotifyClientCredentials
import spotipy 
import pandas as pd
import re
import matplotlib.pyplot as plt

#set as client credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id= 'ae2e171679c54b08af249491660986c1', #use client id from spotify developer
    client_secret= '8e3b7f5b0cf94f23b0a8d3249aaab71e' #use client secret
))

#full track links
track_url ="https://open.spotify.com/track/57IV0hLaFBsJItvjSLu601"
            
            

# Extract track ID directly from URL using regex
track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

# Fetch track details
track = sp.track(track_id)
print(track)
# Extract metadata
track_data = {
    'Track Name': track['name'],
    'Artist': track['artists'][0]['name'],
    'Album': track['album']['name'],
    'Popularity': track['popularity'],
    'Duration (minutes)': track['duration_ms'] / 60000
}

# Display metadata
print(f"\nTrack Name: {track_data['Track Name']}")
print(f"Artist: {track_data['Artist']}")
print(f"Album: {track_data['Album']}")
print(f"Popularity: {track_data['Popularity']}")
print(f"Duration: {track_data['Duration (minutes)']:.2f} minutes")

# Convert metadata to DataFrame
df = pd.DataFrame([track_data])
print("\nTrack Data as DataFrame:")
print(df)

# Save metadata to CSV
df.to_csv('spotify_track_data.csv', index=False)

# Visualize track data
features = ['Popularity', 'Duration (minutes)']
values = [track_data['Popularity'], track_data['Duration (minutes)']]

plt.figure(figsize=(8, 5))
plt.bar(features, values, color='skyblue', edgecolor='black')
plt.title(f"Track Metadata for '{track_data['Track Name']}'")
plt.ylabel('Value')
plt.show()