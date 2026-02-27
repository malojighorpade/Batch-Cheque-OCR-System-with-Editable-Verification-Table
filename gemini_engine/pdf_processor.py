from pdf2image import convert_from_path
import os


def pdf_to_images(pdf_path, output_folder="samples/pages"):
    os.makedirs(output_folder, exist_ok=True)

    pages = convert_from_path(
        pdf_path,
        poppler_path=r"D:\Release-25.12.0-0\poppler-25.12.0\Library\bin"
    )

    image_paths = []

    for i, page in enumerate(pages):
        image_path = os.path.join(output_folder, f"page_{i+1}.png")
        page.save(image_path, "PNG")
        image_paths.append(image_path)

    return image_paths