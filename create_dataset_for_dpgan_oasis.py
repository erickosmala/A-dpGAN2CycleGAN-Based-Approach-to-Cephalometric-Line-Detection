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
    parser.add_argument('--type', type=str, required=True, help='Value: "train"/"test"')
    parser.add_argument('--output', type=str, required=True, help='Path to the output folder')

    args = parser.parse_args()

    images_path = args.path_to_images
    masks_path = args.path_to_masks
    dataset_type = args.type
    output_path = f"{args.output}_{dataset_type}"

    MAIN_FOLDERS = [ "images", "annotations"]
    SUB_FOLDERS = ["train", "val"]

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    for fold in range(0, 16):
        if not os.path.exists(f"{output_path}\\cephalo_line_{fold}"):
            os.mkdir(f"{output_path}\\cephalo_line_{fold}")
        for mf in MAIN_FOLDERS:
            if not os.path.exists(f"{output_path}\\cephalo_line_{fold}\\{mf}"):
                os.mkdir(f"{output_path}\\cephalo_line_{fold}\\{mf}")
            for sf in SUB_FOLDERS:
                if not os.path.exists(f"{output_path}\\cephalo_line_{fold}\\{mf}\\{sf}"):
                    os.mkdir(f"{output_path}\\cephalo_line_{fold}\\{mf}\\{sf}")

    # sorted_models = sorted(os.listdir(masks_path), key=extract_mask_number)
    for idm, mask_folder in enumerate(tqdm(os.listdir(masks_path), total=len(os.listdir(masks_path)))):
        sorted_files = sorted(os.listdir(f"{masks_path}/{mask_folder}"), key=extract_mask_number)
        for idx, file in enumerate(sorted_files):
            if dataset_type == "train":
                if idm >= 1500:
                    break

                # IMAGE
                image_path = f"{images_path}/{mask_folder}.png"
                image = Image.open(image_path)
                image = image.resize((512, 648))

                # MASK
                mask_path = f"{masks_path}/{mask_folder}/{file}"
                mask = Image.open(mask_path)
                mask = mask.resize((512, 648))
                if idm < 1200:
                    image.save(f"{output_path}/cephalo_line_{idx}/{MAIN_FOLDERS[0]}/{SUB_FOLDERS[0]}/{file}")
                    mask.save(f"{output_path}/cephalo_line_{idx}/{MAIN_FOLDERS[1]}/{SUB_FOLDERS[0]}/{file}")
                else:
                    image.save(f'{output_path}/cephalo_line_{idx}/{MAIN_FOLDERS[0]}/{SUB_FOLDERS[1]}/{file}')
                    mask.save(f'{output_path}/cephalo_line_{idx}/{MAIN_FOLDERS[1]}/{SUB_FOLDERS[1]}/{file}')
            else:
                if idm < 1500:
                    continue

                image_path = f"{images_path}/{mask_folder}.png"
                image = Image.open(image_path)
                image = image.resize((512, 648))

                # MASK
                mask_path = f"{masks_path}/{mask_folder}/{file}"
                mask = Image.open(mask_path)
                mask = mask.resize((512, 648))

                image.save(f'{output_path}/cephalo_line_{idx}/{MAIN_FOLDERS[0]}/{SUB_FOLDERS[1]}/{file}')
                mask.save(f'{output_path}/cephalo_line_{idx}/{MAIN_FOLDERS[1]}/{SUB_FOLDERS[1]}/{file}')
