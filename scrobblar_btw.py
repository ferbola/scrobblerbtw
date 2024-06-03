import pylast
import time

API_KEY = "6d29d8fd69b3e83269ae04546e625f59"
API_SECRET = "f7d1b67928c9ca5b18dadc574f9ecaa1"

from getpass import getpass
username = input("Usuário: ")
password = getpass("Senha: ")
artist = input("Artista: ")
title = input("Música: ")
loop_delay = float(input("Intervalo (segundos): "))
max_count = input("Repetições: ")
password_hash = pylast.md5(password)

loop_delay = float(loop_delay)
max_count = int(max_count)

lastfm = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                              username=username, password_hash=password_hash)

count = 0

while count < max_count:
    try:
        lastfm.scrobble(artist=artist, title=title, timestamp=int(time.time()))
        count += 1
        print(f"Scrobblado com sucesso! ({count})")
    except pylast.WSError as e:
        print("Erro: ", e)

    time.sleep(loop_delay)
