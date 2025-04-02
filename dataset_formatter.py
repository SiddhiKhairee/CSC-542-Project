import os
import shutil
import random
from tqdm import tqdm

og_dir = "CUB_200_2011/images"
output_dir = "CUB_formatted"
train_ratio = 0.8

random.seed(1234)

for class_name in tqdm(os.listdir(og_dir), desc="Formatting dataset"):
    class_path = os.path.join(og_dir, class_name)
    if not os.path.isdir(class_path):
        continue

    images = os.listdir(class_path)
    random.shuffle(images)

    train_cutoff = int(len(images) * train_ratio)
    train_images = images[:train_cutoff]
    val_images = images[train_cutoff:]

    for split_name, split_images in [("train", train_images), ("val", val_images)]:
        split_class_dir = os.path.join(output_dir, split_name, class_name)
        os.makedirs(split_class_dir, exist_ok=True)
        
        for image_name in split_images:
            src_path = os.path.join(class_path, image_name)
            dst_path = os.path.join(split_class_dir, image_name)
            shutil.copy2(src_path, dst_path)