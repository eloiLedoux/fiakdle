from PIL import Image

def crop_image(input_image_path, output_image_path, coordinates):
    """
    Crop an image based on given coordinates and save the cropped image.
    
    Parameters:
        input_image_path (str): Path to the input image.
        output_image_path (str): Path to save the cropped image.
        coordinates (tuple): Tuple containing the (left, upper, right, lower) coordinates of the crop region.
    """
    # Open the input image
    input_image = Image.open(input_image_path)

    # Crop the image
    cropped_image = input_image.crop(coordinates)

    # Save the cropped image
    cropped_image.save(output_image_path)

# Example usage:
if __name__ == "__main__":
    input_image_path  = "./images/hiboux.png"
    output_image_path = "./images/cropped_hiboux.png"
    coordinates       = (74,237,490,522)  # (left, upper, right, lower)

    crop_image(input_image_path, output_image_path, coordinates)