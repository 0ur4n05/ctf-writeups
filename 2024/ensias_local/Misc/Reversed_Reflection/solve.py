from PIL import Image, ImageOps
import numpy as np

def h (challfile, r):


def rech(challfile, randomnum, r=1):
    if n == 0:
        return challfile
    else:
        return recursive_h(h(challfile, r), randomnum-1, r)

def decreate_challenge():
    flag = Image.open("./macos.png")
    chall = recursive_h(flag, np.random.randint(20, 31))  # Apply the transformation for 20~30 times :D
    chall.save("./zl.png")

