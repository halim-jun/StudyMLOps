import kagglehub
import shutil
import os
from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent

# Create raw data directory relative to this script
raw_data_dir = script_dir / "raw"
raw_data_dir.mkdir(parents=True, exist_ok=True)

# Download latest version
print("Downloading dataset...")
downloaded_path = kagglehub.dataset_download(
    "rakeshkapilavai/extrovert-vs-introvert-behavior-data"
)

print(f"Dataset downloaded to: {downloaded_path}")

# Copy files to your data folder
for file in Path(downloaded_path).glob("*"):
    if file.is_file():
        destination = raw_data_dir / file.name
        shutil.copy2(file, destination)
        print(f"Copied {file.name} to {destination}")

print(f"\nAll files copied to: {raw_data_dir.absolute()}")
print("Available files:")
for file in raw_data_dir.glob("*"):
    print(f"  - {file.name}")
