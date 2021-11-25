from shutil import copy
import os


class cd:
  def __init__(self, new_path):
    self.new_path = os.path.expanduser(new_path)
    self.saved_path = None

  def __enter__(self):
    self.saved_path = os.getcwd()
    os.chdir(self.new_path)

  def __exit__(self, etype, value, traceback):
    os.chdir(self.saved_path)


def copy_directory(src, dest):
  for src_dir, _, files in os.walk(src):
    dst_dir = src_dir.replace(src, dest, 1)
    if not os.path.exists(dst_dir):
      os.makedirs(dst_dir)
    for f in files:
      src_file = os.path.join(src_dir, f)
      dst_file = os.path.join(dst_dir, f)
      if os.path.exists(dst_file):
        os.remove(dst_file)
      copy(src_file, dst_dir)
