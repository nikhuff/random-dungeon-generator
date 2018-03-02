import numpy as np
from PIL import Image

def combine_images(dungeon):
    horizontal_imgs = list()
    imgs_comb = None
    for i in range(0, len(dungeon[0])):
        list_imgs = dungeon[i]
        imgs = [Image.open(j) for j in list_imgs]
        min_shape = sorted([(np.sum(k.size), k.size) for k in imgs])[0][1]
        imgs_comb = np.hstack((np.asarray(l.resize(min_shape)) for l in imgs))
        horizontal_imgs.append(imgs_comb)

    # print(i.size for i in horizontal_imgs)
    imgs_comb = np.vstack(i for i in horizontal_imgs)
    imgs_comb = Image.fromarray(imgs_comb)

    imgs_comb.save('./assets/dungeon.png')

if __name__ == '__main__':
    dungeon = list()
    dungeon.append(['1.png'] * 10)
    dungeon.append(['2.png'] * 10)
    dungeon.append(['3.png'] * 10)
    dungeon.append(['4.png'] * 10)
    dungeon.append(['5.png'] * 10)
    dungeon.append(['6.png'] * 10)
    dungeon.append(['7.png'] * 10)
    dungeon.append(['8.png'] * 10)
    dungeon.append(['9.png'] * 10)
    dungeon.append(['10.png'] * 10)
    combine_images(dungeon)
