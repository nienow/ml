import os
import urllib.request

def download_dataset(directory, files):
    path = os.path.join("data")
    if not os.path.isdir(path):
        os.makedirs(path)
    for filename in files:
        filepath = os.path.join(path, filename)
        if not os.path.isfile(filepath):
            print("Downloading", filename)
            urllib.request.urlretrieve(directory + '/' + filename, filepath)
