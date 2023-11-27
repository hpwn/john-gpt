import requests
from urllib.parse import urlencode

# Replace these with your actual client_id and client_secret
client_id = "ubmdsee1juxoh3s3q8br2zoydt2xob"
client_secret = "80wht7p6l989yx69vg3dh6m6m21jeh"
redirect_uri = "http://localhost"  # The redirect URI set for your application
scopes = ["chat:read", "chat:edit"]  # The scopes your application requires

# Step 1: Direct user to the Twitch authorization page
params = {
    "client_id": client_id,
    "redirect_uri": redirect_uri,
    "response_type": "code",
    "scope": " ".join(scopes),
}
url = f"https://id.twitch.tv/oauth2/authorize?{urlencode(params)}"
print(f"Go to this URL and authorize the application: {url}")

# Step 2: User will be redirected to the redirect_uri with a code in the query string
# This part will be done manually by the user, and you'll need to obtain the 'code' parameter from the redirected URL

# Step 3: Exchange the code for an access token
code = input("Enter the code from the URL: ")
token_url = "https://id.twitch.tv/oauth2/token"
token_data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "code": code,
    "grant_type": "authorization_code",
    "redirect_uri": redirect_uri,
}
token_r = requests.post(token_url, data=token_data)
token_response = token_r.json()

access_token = token_response.get("access_token")
refresh_token = token_response.get("refresh_token")  # Retrieve the refresh token
print(f"Your access token is: {access_token}")
print(f"Your refresh token is: {refresh_token}")
