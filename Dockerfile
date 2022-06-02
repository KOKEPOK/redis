
FROM ubuntu

RUN apt update
RUN apt install git -y
RUN apt install python3 -yd
EXPOSE 3000
WORKDIR /home/app/

RUN apt install python3-pip -y
RUN pip3 install fastapi
RUN pip3 install uvicorn
RUN pip3 install pyowm
RUN pip3 install redis

RUN pip3 install redis-py-cluster

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["weather_api_1.py"] 1