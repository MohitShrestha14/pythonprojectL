from PIL import Image

filename = "strawberry.jpeg"
with Image.open(filename) as img:
    img.load()
print(type(img))
print(isinstance(img, Image.Image))
img.show()
# Split the image into individual bands
red, green, blue = img.split()

# Zero out the red band
# zeroed_red_band = red.point(lambda _: 0)
# zeroed_blue_band = blue.point(lambda _: 0)
zeroed_green_band = green.point(lambda _: 0)

# Merge the bands back, replacing the red band with the zeroed band
merged_img1 = Image.merge("RGB", (red, zeroed_green_band, blue))
# merged_img2 = Image.merge("RGB", (zeroed_green_band, green, zeroed_green_band))
# merged_img3 = Image.merge("RGB", (zeroed_green_band, zeroed_green_band, blue))

# Show the new image
merged_img1.show()
# merged_img2.show()
# merged_img3.show()








# from PIL import Image
#
# filename = "2.png"
# with Image.open(filename) as img:
#     img.load()
# print(type(img))
# print(isinstance(img, Image.Image))
# img.show()
# print(img.format)
# print(img.size)
# print(img.mode)

# # cropped image
# cropped_img = img.crop((300, 150, 700, 600))
# print(cropped_img.size)
# cropped_img.show()
# cropped_img_rgb = cropped_img.convert("RGB")
# cropped_img_rgb.save("cropped_img.jpeg")
#
# # resized image
# low_res_img = cropped_img.resize(
#     (cropped_img.width//4, cropped_img.height//4)
# )
# low_res_img.show()
# print(low_res_img.size)
# low_res_img_rgb = low_res_img.convert("RGB")
# low_res_img_rgb.save("low_res_img.jpg")
#
# # reduce image
# reduce_img = img.reduce(4)
# reduce_img.show()
# print(reduce_img.size)
# reduce_img.save("reduce_img.png")
#
# # thumbnail image
# img.thumbnail((200, 200))
# img.show()
# print(img.size)
# img.save("thumbnail_img.png")







