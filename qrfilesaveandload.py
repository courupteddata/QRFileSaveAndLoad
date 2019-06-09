"""
For Linux:
sudo apt-get install libzbar0

pip install pyzbar
pip install PyPNG

pip install pyqrcode

36 H 600
"""

import pyqrcode
import os
from pyzbar.pyzbar import decode
from PIL import Image

MAX_LENGTH = 600
OUTPUT_DIR = "output"
INPUT_DIR = "input"


def create(text_file_name: str):
    with open(text_file_name, "r") as f:
        contents = f.read()
    data = [contents[i: i + MAX_LENGTH] for i in range(0, len(contents), MAX_LENGTH)]

    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)

    count = 0
    for item in data:
        count += 1
        pyqrcode.create(item, error="H", version=36).png(f"{INPUT_DIR}/{count}-qr.png", scale=4)


def load(output_file_name):
    files = sorted(os.listdir(INPUT_DIR))
    data = []
    for file in files:
        temp = decode(Image.open(f"{INPUT_DIR}/{file}"))[0][0].decode()
        data.append(temp)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(OUTPUT_DIR + "/" + output_file_name, "w+") as f:
        f.write("".join(data))


if __name__ == "__main__":
    create("something.txt")
    load("something.txt")

