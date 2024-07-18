# from fastapi.responses import HTMLResponse
import cv2
from fastapi import FastAPI, File, UploadFile
import cv2 as cv
import numpy as np
import uvicorn

app = FastAPI()


@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    # Convert the image data to a numpy array
    npimage = np.frombuffer(contents, np.uint8)
    # Decode the image
    image = cv.imdecode(npimage, cv.IMREAD_COLOR)
    # Save the image to display later
    cv.imwrite("uploaded_image.jpg", image)
    return {"filename": file.filename}


@app.get("/show-image/")
async def show_image():
    # Read the image from the file
    image = cv.imread("uploaded_image.jpg")
    if image is None:
        return {"error": "No image uploaded"}
    # Display the image using OpenCV
    cv.namedWindow("Uploaded Image", cv.WINDOW_NORMAL)
    cv.imshow("Uploaded Image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return {"status": "Image displayed"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# @app.get("/")
# async def main():
#     content = """
#     <body>
#     <form action="/upload-image/" enctype="multipart/form-data" method="post">
#     <input name="file" type="file">
#     <input type="submit">
#     </form>
#     </body>
#     """
#     return HTMLResponse(content=content)
