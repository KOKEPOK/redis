redis на С++. true-false с маленькой буквы

сборка великолепия из папки редиса
docker-compose build && docker-compose up

из бд:
curl -XGET http://127.0.0.1:3000/1?city=Finland
http://127.0.0.1:8080/1?city=Finland

C сервера:
curl -XGET http://127.0.0.1:3000/v1/current/city?q=Finland
http://127.0.0.1:8080/v1/current/city?q=Finland

запись в бд:
C сервера:
curl -X PUT -H "Content-Type: application/json" -d '{"City":"Finland", "weather": "21"}' "http://127.0.0.1:3000/2"

на реплике просмотр. Нужен режим кластера не забыть:
docker exec -it m_b bash
keys *
get key
get не робит с листами.
lrange название start stop  = читать лист.
lpush list 2   - вставить значение "2" в лист слева.
del key
redis-cli -p 6384 -c
redis-cli monitor
redis-server
shutdown


Если запросы от python не принимаются redis windows, то в redis-cli нужно снять защиту:
config set protected-mode no

Прочее:
INCR название_переменной   - переводит значение в integer и увеличивает на одну.
redis.client.incr('counter')  -название переменной
redis.client.incr('counter', 10)  -название переменной и на сколько увеличивать.

генератор - брать не сразу весь список, а по частям. СКАН ИТЕР:
print(redis_client.scan_iter('*')) - получить первую часть списка
print(next(redis_client.scan_iter('*'))) - получить список дальше
print(redis_client.scan_iter('*', count=10)) - получать по 10 строк за запрос.