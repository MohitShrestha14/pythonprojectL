from typing import Annotated
import numpy as np
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
import cv2 as cv
from PIL import Image

# import sys

app = FastAPI()


@app.get("/")
def root():
    message = """Hello, Welcome to FastAPI..."""
    return message


extensions = {'png', 'jpg', 'jpeg'}


@app.post("/upload_image_and_opencv/")
async def upload_image(
        file: Annotated[UploadFile,
        File(description="An image "
                         "upload "
                         "file is "
                         "read as "
                         "UploadFile & display "
                         "feature using opencv")]
):
    for extension in extensions:
        if file.filename.endswith(extension):
            content = await file.read()
            nparray = np.frombuffer(content, np.uint8)
            img = cv.imdecode(nparray, cv.IMREAD_COLOR)
            window_name = "Uploaded_Image1"
            cv.namedWindow(window_name, cv.WINDOW_NORMAL)
            cv.imshow(window_name, img)
            cv.waitKey(0)
            cv.destroyAllWindows()
            return JSONResponse(status_code=200,
                                content={"Image displayed using OpenCV"})
            # return {"status": "Success",
            #         "message": "Image displayed using OpenCV"}

    else:
        return HTTPException(status_code=400, detail="Uploaded file is not "
                                                     "an "
                                                     "image")


@app.post("/upload_image_and_pil/")
async def upload_image2(file: Annotated[UploadFile,
File(description="An image "
                 "upload "
                 "file is "
                 "read as "
                 "UploadFile & display "
                 "feature using pillow")]
                        ):
    try:
        with Image.open(file.file) as im:
            im.load()
    except OSError:
        pass
    im.show()
    return {"status": "Success", "message": "Image displayed using PIL library"}


if __name__ == "__main__":
    uvicorn.run("fastapi_both:app", host="127.0.0.1", port=8000, reload=True)
