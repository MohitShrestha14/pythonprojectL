from typing import Annotated
from fastapi import FastAPI, File, UploadFile
import uvicorn
import cv2 as cv
import numpy as np

app = FastAPI()



if __name__ == '__main__':
    uvicorn.run("testingimageupload:app", host="127.0.0.1", port=8000, reload=True)