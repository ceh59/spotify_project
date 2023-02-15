import spotipy
import spotipy.util as util
import csv
import boto3
from datetime import datetime
from spotipy.oauth2 import SpotifyOAuth
import random
from urllib.error import HTTPError

# Your Spotify API credentials
client_id = "fa9f9e09e79c4b2e8f3f3b0e22242e2b"
client_secret = "5f35c6bb8f5842dd846b9b4127d6f91d"
redirect_uri = "https://www.spotify.com/auth/callback"
username = "12166081114"

# Request an access token using spotipy
scope = "user-read-private"
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

# Use the access token to initialize the spotipy client
sp = spotipy.Spotify(auth=token)

# Request the user data for a specific user
user_id = "12166081114"
user_data = sp.user(user_id)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='fa9f9e09e79c4b2e8f3f3b0e22242e2b',
                                                 client_secret='5f35c6bb8f5842dd846b9b4127d6f91d',
                                                 redirect_uri='https://www.spotify.com/auth/callback',
                                                 username='12166081114'))

#Generate a random list of 11 digit ids to be tried as valid usernames
ids = []
count = 0
successes = 0
while len(ids) <= 100:
    count = count + 1
    id_first = "121660"
    id_second = random.randint(10**4,10**5-1)
    id = "{}{}".format(id_first,id_second)
    print("Tries:{} Successes:{}".format(count, successes))
    try:
        user = sp.user(id)
        ids.append(id)
        successes = successes + 1
    except spotipy.SpotifyException:
        continue
print(ids)
# user = sp.user('12166081119')
# print(user)

# Print the user data
#print(user_data)


