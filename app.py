import json

import nekos
import requests
from flask import Flask, jsonify, make_response, request


class http:
    @staticmethod
    def status(message, status_code):
        return make_response(jsonify(message), status_code)


app = Flask(__name__)


class api:
    version = '1'

#GET / response


@app.route(f"/v{api.version}")
def home():
    return http.status({'status': 200, 'message': 'Welcome to nekos.life RESTful API.', 'version': '1.0'}, 200)


@app.route(f'/v{api.version}/cat')
def cat():
    return http.status({'url': nekos.cat()}, 200)


@app.route(f'/v{api.version}/8ball')
def eightball():
    return http.status(nekos.eightball(), 200)


@app.route(f'/v{api.version}/img/nsfw/<string:target>')
def nsfw(target):
    possible = [
        'anal', 'bj', 'blowjob', 'boobs', 'classic', 'cum', 'cum_jpg', 'ero', 'erofeet', 'erok', 'erokemo', 'eron', 'eroyuri', 'feet', 'feetg', 'femdom', 'futanari', 'hentai', 'holoero', 'hololewd', 'keta', 'kuni', 'les', 'lewd', 'lewdk', 'lewdkemo', 'nsfw_avatar', 'nsfw_neko_gif', 'pussy', 'pussy', 'pussy_jpg', 'pwankg', 'random_hentai_gif', 'smallboobs', 'solo', 'solog', 'tits', 'trap', 'yuri'
    ]
    return http.status({'url': nekos.img(target)}, 200)


@app.route(f'/v{api.version}/img/gen/<string:target>')
def general(target):
    possible = [
        'avatar', 'baka', 'cuddle', 'feed', 'fox_girl', 'gasm', 'gecg', 'holo', 'hug', 'kemonomimi', 'kiss', 'lizard', 'meow', 'neko', 'ngif', 'pat', 'poke', 'slap', 'smug', 'tickle', 'waifu', 'wallpaper'
    ]

    print(sorted(possible))
    return http.status({'url': nekos.img(target)}, 200)

@app.errorhandler(404)
def not_found():
    return http.status({'message': '404 not found'}, 404)

@app.errorhandler(500)
def Interal_Server_Error(e):
    if e is None:
        return http.status({'status_codde':500,'message':'500 Interal Server Error'} , 500)
    return http.status({'status_codde':500,'message':str(e)} , 500)

if __name__ == "__main__":
    app.run()
