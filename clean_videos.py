import os
from moviepy import editor


IN_DIRECTORY = '../original'
OUT_DIRECTORY = '../dest'
PERCENTAGE = 5.5


def get_filenames(directory):
    """
    Get all .mp4 files from directory
    """
    ret = []
    for item in os.walk(directory):
        for filename in item[2]:
            if '.mp4' in filename:
                ret.append(
                    os.path.abspath(os.path.join(item[0], filename)))
    return ret


def ensure_dirs(directory):
    try:
        os.makedirs(directory)
    except FileExistsError:
        pass


def get_dest_path(path, indirectory, outdirectory):
    directory, filename = os.path.split(path)
    part = directory.replace(os.path.abspath(indirectory), '')
    if part and part[0] == '/':
        part = part[1:]
    outdir = os.path.abspath(os.path.join(outdirectory, part))
    ensure_dirs(outdir)
    return os.path.abspath(os.path.join(outdir, filename))


def cut_image(image):
    percentage = PERCENTAGE
    height = len(image)
    cut = int(height * percentage/100)
    width = len(image[0])
    ratio = width/height
    new_height = height-cut
    new_width = int(new_height * ratio)
    offset = int((width-new_width)/2)
    rightoffset = width if offset==0 else 0-offset
    return image[cut:, offset:rightoffset]


if __name__ == '__main__':
    files = get_filenames(IN_DIRECTORY)
    for filename in files:
        clip = editor.VideoFileClip(filename)
        modified = clip.fl_image(cut_image)
        modified = modified.resize(clip.size)
        outname = get_dest_path(filename, IN_DIRECTORY, OUT_DIRECTORY)
        print(outname)
        modified.write_videofile(outname)
        modified.preview()
