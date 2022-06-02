import requests
import redis
import rediscluster
from flask import Flask, request, json
from configparser import ConfigParser
from rediscluster import RedisCluster

parser = ConfigParser()
parser.read("settings.ini")

app = Flask(__name__)
redis_host,redis_port = '172.19.0.7', 6379
#redis_client = redis.Redis(host= redis_host, port= redis_port, decode_responses=True)
startup_nodes =[{"host": "172.19.0.7", "port": "6379"},
                {"host": "172.19.0.6", "port": "6380"},
                {"host": "172.19.0.5", "port": "6381"},
                {"host": "172.19.0.4", "port": "6382"},
                {"host": "172.19.0.3", "port": "6383"},
                {"host": "172.19.0.2", "port": "6384"}
                ]
redis_client = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
time_storage = 60*10

@app.route('/2', methods = ['PUT'])
def puts():
    if request.headers['Content-Type'] == 'application/json':
        a=request.get_json()
        try:
            citz = a["City"]
            weath = a["weather"]
            redis_client.set(name=citz, value=weath)
            return 'Изменения в REDIS внесены. ' + 'В городе ' +citz+' установлена температура '+weath+' градусов.'
        except:
            return f'Ошибка получения погоды для города'

@app.route('/1')
def getc():
    citz = request.args.get('city')
    try:
        result = 'Температура в ' + citz + ' составляет ' + redis_client.get(name=citz) +' градусов!'
        return result
    except:
        result2 = 'Город ' + citz + ' не найден в базе данных REDIS'
        return result2

@app.route('/v1/current/city')
def current():
    city = request.args.get('q')
    print(city)
    response = requests.get(parser.get('API', 'weather'),
                            params={'q': city, 'appid': parser.get('token', 'open_weather_token'), 'units': 'metric'})
    data = response.json()
    city1 = data["main"]["temp"]
    names = data["name"]
    redis_client.set(name=names, value=city1)
    if data.get('cod') != 200:
        message = data.get('message', '')
        return f'Город {city.title()} не найден на карте.'

    current_temperature = data.get('main', {}).get('temp')

    if not current_temperature:
        return f'Ошибка получения погоды для города {city.title()}'
    else:
        return {names:city1}

if __name__ == '__main__':
    app.run(host=parser.get('connect', 'ip'),port = parser.get('connect', 'port'), debug=True)