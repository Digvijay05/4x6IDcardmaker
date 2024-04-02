from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path


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
        output_file = f"..\\{output_directory}\\aadhar_jpg{i + 1}.png"
        image.save(output_file, "PNG")
        crop_image(output_file)


def crop_image(input_file):
    # Importing Image class from PIL module
    from PIL import Image

    # Opens a image in RGB mode
    im = Image.open(input_file)


    # Setting the points for cropped image
    # front_left = 87
    # right = 827
    # top = 1624
    # bottom = 253
    front_left = 87
    front_right = 827
    front_top = 1624
    front_bottom = 2086

    # Cropped image of above dimension
    # (It will not change original image)
    aadhar_front = im.crop((front_left, front_top, front_right, front_bottom))

    back_left = 825
    back_right = 1653-90
    back_top = 1624
    back_bottom = 2086

    # Cropped image of above dimension
    # (It will not change original image)
    aadhar_back = im.crop((back_left, back_top, back_right, back_bottom))

    # Shows the image in image viewer
    aadhar_back.show()
    aadhar_front.show()


if __name__ == "__main__":
    input_file = "..\\d adhar.pdf"
    output_file = "..\\temp\\temp_adhar.pdf"
    output_directory = "temp"
    remove_password(input_file, output_file, password="")
    convert_to_images(output_file, output_directory)
