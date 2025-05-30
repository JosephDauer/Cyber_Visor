import os
import tensorflow as tf
import argparse 

#parse arguments
parser = argparse.ArgumentParser(description='Processing images for InstaGram...')
parser.add_argument('--image', type=str, required=True, help='Path to the image file')
parser.add_argument('--output', type=str, required=True, help='Path to the output file')
parser.add_argument('--height', type=int, default=1080, help='Height of the output image')
parser.add_argument('--width', type=int, default=1080, help='Width of the output image')
args = parser.parse_args()

os.makedirs(args.output_dir, exist_ok=True)

#processing images in set directory
#rezize image to 1080x1080 (Instagram size)
for filename in os.listdir(args.input_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(args.input_dir, filename)
        output_path = os.path.join(args.output_dir, filename)

        # Read and process the image
        image = tf.io.read_file(image_path)
        image = tf.image.decode_jpeg(image, channels=3)
        image = tf.image.resize(image, [args.height, args.width])
        image = tf.image.convert_image_dtype(image, tf.float32)

        #option 1: Apply Filters
        #image = tf.image.adjust_brightness(image, delta=0.1)
        #image = tf.image.adjust_constrast(image, contrast_factor=1.2)

        # Save the processed image
        encoded_image = tf.image.encode_jpeg(tf.cast(image * 255, tf.uint8))
        tf.io.write_file(output_path, encoded_image)

print("Batch processing complete!")


