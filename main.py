import os
from rembg import remove
from PIL import Image


def AI_rem():
    # change_background_mp = mp.solutions.selfie_segmentation

    # change_bg_segment = change_background_mp.SelfieSegmentation()
    print("Started1 !")
    input_folder = 'input'
    img = os.listdir(input_folder)

    print("Started !")
    # print(img)

    # Loop through all files in the input folder
    for filename in img:
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + ".png"  # Change the output file extension to .png
        output_path = os.path.join('output/', output_filename)

        # Open the input image
        with Image.open(input_path) as img:
            # Remove the background
            result = remove(img)

            # Save the result to the output folder
            result.save(output_path, "PNG")
        print(f"Processed {filename}")

        break

print("Hi")
AI_rem()

