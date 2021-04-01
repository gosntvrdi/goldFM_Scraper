FROM python:3.7-slim
COPY . /app/
WORKDIR /app/
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt install ffmpeg -y
#ENTRYPOINT ["tail", "-f", "/dev/null"]
CMD [ "python", "./goldFM_Scraper.py" ]