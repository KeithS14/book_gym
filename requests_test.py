import requests

url = "https://app.glofox.com/portal/#/branch/5b6dd1a5e90c2d1f403fccb6/classes-day-view?header=classes,courses"  # Replace with your desired URL

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    html_content = response.text
    print(html_content)
else:
    print(f"Failed to retrieve HTML. Status code: {response.status_code}")
