import ctypes
import os
import requests

query = f"https://api.unsplash.com/photos/random/?client_id=y-hzyEOUk8piZsPGvkqM_l33UOGkh44BCeJ2rW4MpW8"
response = requests.get(query)
picture_url = response.json()["urls"]["full"]
picture = requests.get(picture_url)

directory = f"C:\\Users\\{os.getlogin()}\\Wallpaper"

if not os.path.exists(directory):
    os.makedirs(directory)

image_path = os.path.abspath(f"{directory}\\{response.json()['id']}.png")
with open(image_path, "wb") as file:
    file.write(picture.content)

ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

current_image_id = response.json()["id"]
current_image_filename = f"{current_image_id}.png"

for filename in os.listdir(directory):
    image_path = os.path.join(directory, filename)

    if filename != current_image_filename:
        os.remove(image_path)

for filename in os.listdir(directory):
    image_path = os.path.join(directory, filename)
    print(image_path)
