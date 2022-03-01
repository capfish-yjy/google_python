
#!/usr/bin/env python3

import sys
import os
from PIL import Image

for file in os.listdir("./supplier-data/images"):
    print(file)
    try:
        with Image.open("./supplier-data/images/"+file) as im:
            print(im.format)
            im.resize((600,400)).convert('RGB').save("./supplier-data/images/"+file.replace(".tiff",".jpeg"), "JPEG" )
    except OSError as e:
        print(e)
        pass
