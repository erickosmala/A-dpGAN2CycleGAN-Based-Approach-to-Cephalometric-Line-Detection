from PIL import Image
import argparse
import os
import re
from tqdm import tqdm


def extract_mask_number(filename):
    match = re.search(r"_mask_(\d+)", filename)
    return int(match.group(1)) if match else -1


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run model on input data.")
    parser.add_argument('--path_to_masks', type=str, required=True, help='Path to the folder containing masks')
    parser.add_argument('--path_to_images', type=str, required=True, help='Path to the folder containing images')
    parser.add_argument('--output', type=str, required=True, help='Path to the output folder')

    args = parser.parse_args()

    images_path = args.path_to_images
    masks_path = args.path_to_masks
    output_path = args.output

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    MAIN_FOLDER = ["A", "B"]
    SUB_FOLDERS = ["train", "val", "test"]

    for fold in range(0, 16):
        if not os.path.exists(f"{output_path}\\cephalo_line_{fold}"):
            os.mkdir(f"{output_path}\\cephalo_line_{fold}")
        for mf in MAIN_FOLDER:
            if not os.path.exists(f"{output_path}\\cephalo_line_{fold}\\{mf}"):
                os.mkdir(f"{output_path}\\cephalo_line_{fold}\\{mf}")
            for sf in SUB_FOLDERS:
                if not os.path.exists(f"{output_path}\\cephalo_line_{fold}\\{mf}\\{sf}"):
                    os.mkdir(f"{output_path}\\cephalo_line_{fold}\\{mf}\\{sf}")

    for idm, model in enumerate(tqdm(os.listdir(masks_path), total=len(os.listdir(masks_path)))):
        sorted_files = sorted(os.listdir(os.path.join(masks_path, model)), key=extract_mask_number)
        for idf, file in enumerate(sorted_files):

            # IMAGE
            image_path = f"{images_path}/{file}"
            image_path = re.sub(r"_mask_(\d+)", "", image_path)
            image = Image.open(image_path)
            image = image.resize((640, 800))

            # MASK
            mask_path = f"{masks_path}/{model}/{file}"
            img = mask_path.split('/')[-1]
            mask = Image.open(mask_path)
            mask = mask.resize((640, 800))

            if idm < 1200:
                image.save(
                    f"{output_path}\\cephalo_line_{idf}\\{MAIN_FOLDER[0]}\\{SUB_FOLDERS[0]}\\{img}"
                )
                mask.save(
                    f"{output_path}\\cephalo_line_{idf}\\{MAIN_FOLDER[1]}\\{SUB_FOLDERS[0]}\\{img}"
                )
            elif 1200 <= idm < 1500:
                image.save(
                    f"{output_path}\\cephalo_line_{idf}\\{MAIN_FOLDER[0]}\\{SUB_FOLDERS[1]}\\{img}"
                )
                mask.save(
                    f"{output_path}\\cephalo_line_{idf}\\{MAIN_FOLDER[1]}\\{SUB_FOLDERS[1]}\\{img}"
                )
            else:
                image.save(
                    f"{output_path}\\cephalo_line_{idf}\\{MAIN_FOLDER[0]}\\{SUB_FOLDERS[2]}\\{img}"
                )
                mask.save(
                    f"{output_path}\\cephalo_line_{idf}\\{MAIN_FOLDER[1]}\\{SUB_FOLDERS[2]}\\{img}"
                )
