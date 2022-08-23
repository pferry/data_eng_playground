import requests

URL = "https://data.gharchive.org/"

def download_file(file):
    r = requests.get(URL+file)
    return r