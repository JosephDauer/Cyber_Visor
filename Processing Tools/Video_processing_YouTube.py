import os
import argparse
from moviepy.editor import VideoFileClip # type: ignoire

# Parse arguments
parser = argparse.ArgumentParser(description="Batch process videos for YouTube.")
parser.add_argument('--input_dir', type=str, required=True, help="Path to Video Folder.")
parser.add_argument('--output_dir', type=str, required=True, help="Path to the Save Folder.")
parser.add_argument('--width', type=int, default=1920, help="Width of the output video (default: 1920).")
parser.add_argument('--height', type=int, default=1080, help="Height of the output video (default: 1080).")
parser.add_argument('--format', type=str, default='mp4', help="Output video format (default: mp4).")
args = parser.parse_args()

# Ensure the output directory exists
os.makedirs(args.output_dir, exist_ok=True)

# Process all videos in the input directory
for filename in os.listdir(args.input_dir):
    if filename.endswith('.mp4') or filename.endswith('.mov') or filename.endswith('.avi'):
        input_path = os.path.join(args.input_dir, filename)
        output_filename = os.path.splitext(filename)[0] + f".{args.format}"
        output_path = os.path.join(args.output_dir, output_filename)

        print(f"Processing {filename}...")

        # Load the video
        clip = VideoFileClip(input_path)

        # Resize the video
        resized_clip = clip.resize(newsize=(args.width, args.height))

        # Write the video to the output directory
        resized_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

        # Close the clip to free resources
        clip.close()
        resized_clip.close()

print("Batch video processing complete!")