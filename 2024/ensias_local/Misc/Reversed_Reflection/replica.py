from PIL import Image, ImageOps
import numpy as np

def invert_colors(rgb_image):
    return ImageOps.invert(rgb_image)

def g(i, r=1):
    H = i.size[0] // 2
    A = i.crop((0, 0, H, i.size[1]))
    B = i.crop((H, 0, 2*H, i.size[1]))
    if r == 1:
        return (ImageOps.mirror(A), ImageOps.mirror(B))
    else:
        return (A, B)

def f(x, y, r=1):
    if x.size[0] == 1:
        return Image.new('RGB', (x.size[0] + y.size[0], x.size[1]), (0, 0, 0)).paste(x).paste(y, (x.size[0], 0))
    else:
        a, b = g(x, r)
        p, q = g(y, r)
        return f(q, a, r).paste(f(b, p, r), (q.size[0], 0))

def h(i, r=1):
    x, y = g(invert_colors(i), r)
    return f(x, y, r)

def recursive_h(i, n, r=1):
    if n == 0:
        return i
    else:
        return recursive_h(h(i, r), n-1, r)

def create_challenge():
    flag = Image.open("./macos.png")
    chall = recursive_h(flag, np.random.randint(20, 31))  # Apply the transformation for 20~30 times :D
    chall.save("./zl.png")

create_challenge()
