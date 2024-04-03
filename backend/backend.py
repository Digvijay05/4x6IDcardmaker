import os

from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path
from PIL import Image


def remove_password(input_file, output_file, password):
    with open(input_file, "rb") as f:
        pdf = PdfReader(f)
        if pdf.is_encrypted:
            pdf.decrypt(password)

        with open(output_file, "wb") as output:
            writer = PdfWriter()
            for page in pdf.pages:
                writer.add_page(page)
            writer.write(output)
            writer.close()


def convert_to_images(input_file, output_directory):
    images = convert_from_path(input_file, poppler_path="..\\poppler-24.02.0\\Library\\bin")

    for i, image in enumerate(images):
        output_file = f"..\\{output_directory}\\aadhar_{i + 1}.png"
        image.save(output_file, "PNG")
        crop_image(output_file)
        image.close()


def crop_image(input_file):
    # Opens a image in RGB mode
    im = Image.open(input_file)
    with open("crop.txt", "r") as f:
        lines = f.readlines()
        lines_list = []
        front = 0
        back = 0
        for line in lines:
            if line.strip() == "##front":
                front = 1
                back = 0
                continue
            elif line.strip() == "##back":
                back = 1
                front = 0
                continue
            if front == 1:
                lines_list.append(int(line.strip()))
            elif back == 1:
                lines_list.append(int(line.strip()))

        front_left = lines_list[0]
        front_right = lines_list[1]
        front_top = lines_list[2]
        front_bottom = im.height - lines_list[3]

        back_left = lines_list[4]
        back_right = im.width - lines_list[5]
        back_top = lines_list[6]
        back_bottom = im.height - lines_list[7]

    aadhar_front = im.crop((front_left, front_top, front_right, front_bottom))
    aadhar_back = im.crop((back_left, back_top, back_right, back_bottom))
    aadhar_front = aadhar_front.resize((1031, 658))
    aadhar_back = aadhar_back.resize((1035, 659))
    aadhar_back = aadhar_back.rotate(180)

    # Shows the image in image viewer
    # aadhar_back.show()
    # aadhar_front.show()
    create_image(aadhar_front, aadhar_back, "aadhar.png")
    im.close()
    aadhar_back.close()
    aadhar_front.close()


def delete_temp_data():
    os.remove("..\\temp\\aadhar_1.png")
    os.remove("..\\temp\\temp_adhar.pdf")


def create_image(front, back, output_file: str):
    im = Image.new("RGB", (1548, 1780), "white")
    front_left = 265
    front_right = im.width - 252
    front_top = 195
    front_bottom = im.height - 927
    back_left = 265
    back_right = im.width - 248
    back_top = 909
    back_bottom = im.height - 212
    im.paste(front, (front_left, front_top, front_right, front_bottom))
    im.paste(back, (back_left, back_top, back_right, back_bottom))  # , (back_left, back_top, back_right, back_bottom))
    im.save(f"..\\temp\\{output_file}", "PNG")
    im.close()
    # im.show()

# Testing Functionality
# if __name__ == "__main__":
#     input_file = "..\\d adhar.pdf"
#     output_file = "..\\temp\\temp_adhar.pdf"
#     output_directory = "temp"
#     password = ""
#     remove_password(input_file, output_file, password)
#     convert_to_images(output_file, output_directory)
#     delete_temp_data()
