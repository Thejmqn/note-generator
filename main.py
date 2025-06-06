import os

NOTE_NUM = 2
IMAGE_TYPES = ["jpg", "png", "gif", "webp", "svg"]

def get_images(directory):
    files = os.listdir(directory)
    images = []
    for file in files:
        for image_type in IMAGE_TYPES:
            if file.endswith("." + image_type):
                images.append(os.path.join(directory, file))
    return images

def open_file():
    with open("output.jsx", "w") as f:
        f.write("testing")

def main():
    images = get_images(r'C:\Users\jav3fh\Programming\personal-site\src\notes\0')
    print(images)

if __name__ == "__main__":
    main()
