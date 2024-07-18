from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
import cv2
import numpy as np
import uvicorn
import os

app = FastAPI()

UPLOAD_FOLDER = "uploaded_images"

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Allowed image file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[
        1].lower() in ALLOWED_EXTENSIONS


@app.post("/upload-images/")
async def upload_images(files: list[UploadFile] = File(...)):
    filenames = []
    for file in files:
        # Validate file extension
        if not allowed_file(file.filename):
            raise HTTPException(status_code=400,
                                detail="Only images (png, jpg, jpeg, gif) are allowed.")

        contents = await file.read()
        # Convert the image data to a numpy array
        nparr = np.frombuffer(contents, np.uint8)
        # Decode the image
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # Save the image to display later
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        cv2.imwrite(file_path, image)
        filenames.append(file.filename)
    return JSONResponse(content={"filenames": filenames})


@app.get("/show-images/")
async def show_images():
    images = [os.path.join(UPLOAD_FOLDER, filename) for filename in
              os.listdir(UPLOAD_FOLDER)]
    if not images:
        return {"error": "No images uploaded yet"}

    # Display each uploaded image sequentially
    for image_path in images:
        image = cv2.imread(image_path)
        if image is None:
            return {"error": f"Failed to load image {image_path}"}

        # Display the image using OpenCV
        cv2.imshow("Uploaded Image", image)
        cv2.waitKey(0)  # Wait indefinitely until a key is pressed
        cv2.destroyAllWindows()

    return {"status": "All images displayed"}

if __name__ == "__main__":
    uvicorn.run("mainmultiple:app", host="0.0.0.0", port=8000, reload=True)

# from fastapi import FastAPI, File, UploadFile
# from fastapi.responses import HTMLResponse, JSONResponse
# import cv2
# import numpy as np
# import uvicorn
# import os
#
# app = FastAPI()
#
# UPLOAD_FOLDER = "uploaded_images"
#
# # Ensure the upload folder exists
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)
#
# @app.post("/upload-images/")
# async def upload_images(files: list[UploadFile] = File(...)):
#     filenames = []
#     for file in files:
#         contents = await file.read()
#         # Convert the image data to a numpy array
#         nparr = np.frombuffer(contents, np.uint8)
#         # Decode the image
#         image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#         # Save the image to display later
#         file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#         cv2.imwrite(file_path, image)
#         filenames.append(file.filename)
#     return JSONResponse(content={"filenames": filenames})
#
#
# @app.get("/show-images/")
# async def show_images():
#     images = [os.path.join(UPLOAD_FOLDER, filename) for filename in
#               os.listdir(UPLOAD_FOLDER)]
#     if not images:
#         return {"error": "No images uploaded yet"}
#
#     # Display each uploaded image sequentially
#     for image_path in images:
#         image = cv2.imread(image_path)
#         if image is None:
#             return {"error": f"Failed to load image {image_path}"}
#
#         # Display the image using OpenCV
#         cv2.imshow("Uploaded Image", image)
#         cv2.waitKey(0)  # Wait indefinitely until a key is pressed
#         cv2.destroyAllWindows()
#
#     return {"status": "All images displayed"}
#
#
# # @app.get("/show-images/")
# # async def show_images():
# #     images = [os.path.join(UPLOAD_FOLDER, filename) for filename in os.listdir(UPLOAD_FOLDER)]
# #     for image_path in images:
# #         image = cv2.imread(image_path)
# #         if image is None:
# #             return {"error": f"Failed to load image {image_path}"}
# #         # Display the image using OpenCV
# #         cv2.imshow("Uploaded Image", image)
# #         cv2.waitKey(0)  # Show each image for 1 second
# #     cv2.destroyAllWindows()
# #     return {"status": "All images displayed"}
#
# @app.get("/")
# async def main():
#     content = """
#     <body>
#     <form action="/upload-images/" enctype="multipart/form-data" method="post">
#     <input name="files" type="file" multiple>
#     <input type="submit">
#     </form>
#     </body>
#     """
#     return HTMLResponse(content=content)
#
# if __name__ == "__main__":
#     uvicorn.run("mainmultiple:app", host="0.0.0.0", port=8000, reload=True)
