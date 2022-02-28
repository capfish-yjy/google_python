
#!/usr/bin/env python
import subprocess
from multiprocessing import Pool
import os

def run(dir):
  src = "./data/prod/"
  dest = "./data/prod_backup/"

  subprocess.call(["rsync", "-arq", dir, dest])


if __name__ == "__main__":
  src = "./data/prod/"
  filesdir = [os.path.join(src, file) for file in os.listdir(src)]
  p = Pool(len(filesdir))
  p.map(run,filesdir)
