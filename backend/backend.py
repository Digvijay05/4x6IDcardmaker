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
    images = convert_from_path(input_file)

    for i, image in enumerate(images):
        output_file = f"{output_directory}/aadhar_jpg{i + 1}.jpg"
        image.save(output_file, "JPG")


if __name__ == "__main__":
    input_file = "..\\d adhar.pdf"
    output_file = "..\\temp\\temp_adhar.pdf"
    output_directory = "temp"
    remove_password(input_file, output_file, password="")
    convert_to_images(output_file, output_directory)
