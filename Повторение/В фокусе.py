from PIL import Image

im = Image.open('image.png')
pix = im.load()
x, y = im.size
background_color = pix[0, 0]
mi_x, ma_x, mi_y, ma_y = int, int, int, int
for i in range(x):
    for j in range(y):
        r, g, b = pix[i, j]
        if (r, g, b) != background_color:
            if all(map(lambda _: _ == int, [ma_y, ma_x, mi_y, mi_x])):
                mi_x, ma_x, mi_y, ma_y = i, i, j, j
            else:
                if i < mi_x:
                    mi_x = i
                if i > ma_x:
                    ma_x = i
                if j < mi_y:
                    mi_y = j
                if j > ma_y:
                    ma_y = j

ma_x += 1
ma_y += 1
im = im.crop((mi_x, mi_y, ma_x, ma_y))
im.save('res.png')
