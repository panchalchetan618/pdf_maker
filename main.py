from PIL import Image
import os


def images_to_pdf(image_folder, output_pdf):
    image_files = [
        f
        for f in os.listdir(image_folder)
        if f.lower().endswith(("jpg", "jpeg", "png", "bmp", "tiff"))
    ]

    image_files.sort()

    images = []

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)

        try:
            with Image.open(image_path) as img:
                img = img.convert("RGB")
                images.append(img)
        except Exception as e:
            print(f"Error opening {image_file}: {e}")

    if images:
        try:
            output = os.path.join(image_folder, output_pdf)
            images[0].save(
                output,
                save_all=True,
                append_images=images[1:],
                resolution=100.0,
                quality=75,
            )
            print(f"PDF saved as {output_pdf}")
        except Exception as e:
            print(f"Error saving PDF: {e}")
    else:
        print("No valid images found.")


input_path = input("Where are images? ")
file_name = input("Give a name to file (e.g., output.pdf): ")

if not file_name.lower().endswith(".pdf"):
    file_name += ".pdf"

images_to_pdf(input_path, file_name)
