from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from starlette.middleware.cors import CORSMiddleware
from pytube import YouTube
import os
import logging

some_file_path = "Tesla reversing sound.mp4"
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/download/")
def main(url: str, format: str):

    print(f"DOWNLOADING {url} in format {format}")

    YouTube(url).streams.get_highest_resolution().download()

    yt = YouTube(url)
    yt.streams.first().download()

    download_path = yt.streams.first().default_filename
    print(download_path)


    file_like = open(download_path, mode="rb")
    return StreamingResponse(file_like, media_type="video/mp4")

