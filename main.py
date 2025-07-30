from moviepy import AudioFileClip, ImageClip, concatenate_audioclips


def main():
    audio_files = ["1.mp3", "2.mp3", "3.mp3"]
    image_file = "1.png"
    new_size = (1920, 1080)
    output_file = "output.mp4"

    clips = [AudioFileClip(f) for f in audio_files]
    combined = concatenate_audioclips(clips)
    image_clip = ImageClip(image_file).resized(new_size).with_duration(combined.duration)
    final = image_clip.with_audio(combined)
    final.write_videofile(
        output_file,
        codec="libx264",
        audio_codec="aac",
        fps=1,
    )


if __name__ == "__main__":
    main()
