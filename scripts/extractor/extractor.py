import configparser
import os.path

import moviepy.editor

# equivalent to ffmpeg -i '.\input.mp4' -f mp3 '.\output.mp3'

if __name__ == '__main__':

    dirname = os.path.dirname(os.path.abspath(__file__))

    ini = os.path.join(dirname, "extractor.ini")
    cfg = configparser.RawConfigParser()
    cfg.read(ini)

    settings = "settings"
    path = cfg.get(settings, "path")
    target_format = cfg.get(settings, "target_format")
    output_format = cfg.get(settings, "output_format")

    targets = []

    for item in os.scandir(path):
        if item.name.endswith(target_format) and os.path.isfile(item):
            target = item.path.split(".")[0] + output_format
            if not os.path.exists(target):
                clip = moviepy.editor.VideoFileClip(item.path)
                clip.audio.write_audiofile(item.path.split(".")[0] + output_format)
                targets.append(target)

    for done in targets:
        print(done)

    print("Done")
