from PIL import Image

im = Image.open('image.bmp')
pix = im.load()
x, y = im.size
ho_step, he_step = x // 4, y // 4
matrix = []
for _ in range(1, 5):
    __ = list(map(lambda g: tuple(list(g[::-1])), list(enumerate([_, _, _, _], 1))))
    matrix.append(__)

matrix[3].pop()

print(ho_step, he_step)

sx = 0
sy = 0
for ___ in matrix:
    for p in ___:
        im1 = im.crop((sx, sy, sx + ho_step, sy + ho_step))
        im1.save(f"image{p[0]}{p[1]}.bmp")
        sx += he_step
    sx = 0
    sy += he_step
