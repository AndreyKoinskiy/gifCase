import os
import sys

import imageio
from moviepy.editor import *


def get_upload_path(instance, filename):
  return os.path.join("user_%d" % 1, "car_%s" % instance.slug, filename)


def to_gif(path):
  clip = (VideoFileClip(path))
  clip.write_gif(path[:-4]+'.gif', fps=1)
