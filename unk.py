import pandas as pd
import os

# Paths
txt_path = "listUNK.txt"      # path to your txt file
csv_path = "competition/train.csv"      # path to your CSV
images_dir = "UNK"    # folder containing the .png files

# Read filenames from TXT
with open(txt_path, "r") as f:
    filenames = [line.strip() for line in f if line.strip()]

# Remove ".png" for matching
uuids_to_check = [name.replace(".png", "") for name in filenames]

# Load CSV
df = pd.read_csv(csv_path)

# Check and remove
for filename, uuid in zip(filenames, uuids_to_check):
    match = df[df["uuid"] == uuid]
    if not match.empty:
        file_path = os.path.join(images_dir, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{filename} ✅ Found in CSV and deleted.")
        else:
            print(f"{filename} ✅ Found in CSV but file not found on disk.")
    else:
        print(f"{filename} ❌ Not Found in CSV.")
