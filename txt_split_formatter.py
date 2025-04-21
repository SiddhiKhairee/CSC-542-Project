import os
import shutil
import random
from tqdm import tqdm

og_dir = "CUB_200_2011/images"
output_dir = "CUB_split"
split_file = "CUB_200_2011/train_test_split.txt"
images_file = "CUB_200_2011/images.txt"

# Load image ID → filename mapping
id_to_filename = {}
with open(images_file, 'r') as f:
    for line in f:
        img_id, filename = line.strip().split()
        id_to_filename[img_id] = filename

# Load image ID → split mapping (1 = train, 0 = val)
id_to_split = {}
with open(split_file, 'r') as f:
    for line in f:
        img_id, split = line.strip().split()
        id_to_split[img_id] = "val" if split == "0" else "train"

# Copy images to their respective folders
for img_id, filename in tqdm(id_to_filename.items(), desc="Copying images"):
    split = id_to_split[img_id]
    class_name = filename.split('/')[0]
    image_name = os.path.basename(filename)

    src_path = os.path.join(og_dir, filename)
    dst_dir = os.path.join(output_dir, split, class_name)
    dst_path = os.path.join(dst_dir, image_name)

    os.makedirs(dst_dir, exist_ok=True)
    shutil.copy2(src_path, dst_path)