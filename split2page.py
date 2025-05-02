import pyautogui as auto
import time
import pyperclip
import random
import os
from PIL import Image

def split_two_page_image(input_folder, output_folder):
    """
    Split two-page PNG images into left and right pages and save them separately.
    
    Args:
        input_folder: Folder containing the two-page PNG images
        output_folder: Folder to save the split images
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get list of PNG files in input folder
    png_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]
    
    # Process each PNG file
    for file_name in png_files:
        # Full path to the input file
        input_path = os.path.join(input_folder, file_name)
        
        try:
            # Open the image
            img = Image.open(input_path)
            width, height = img.size
            
            # Split the image in half
            left_half = img.crop((0, 0, width // 2, height))
            right_half = img.crop((width // 2, 0, width, height))
            
            # Generate output file names
            base_name = os.path.splitext(file_name)[0]
            left_output = os.path.join(output_folder, f"{base_name}_1.png")
            right_output = os.path.join(output_folder, f"{base_name}_2.png")
            
            # Save split images
            left_half.save(left_output)
            right_half.save(right_output)
            
            print(f"Successfully split {file_name} into left and right pages")
            
            # Add a small random delay between processing files (0.5 to 2 seconds)
            time.sleep(random.uniform(0.5, 2))
            
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

def main():
    # Define input and output folders
    input_folder = "input"  # Change this to your input folder path
    output_folder = "output"  # Change this to your output folder path
    
    print(f"Starting to process images from {input_folder}")
    split_two_page_image(input_folder, output_folder)
    print(f"Processing complete. Split images saved to {output_folder}")

if __name__ == "__main__":
    main()