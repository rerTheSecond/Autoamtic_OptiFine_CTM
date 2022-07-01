import cv2
from os import mkdir
from time import time


def draw_outline(corner1, corner2, corner3, corner4, side1, side2, side3, side4, frames, outlinelength, texture,
                 outline):
    image = texture.copy()
    sidelength = len(texture[0])

    for n in range(frames):
        if corner1:
            for x in range(outlinelength):
                for y in range(outlinelength):
                    image[y + sidelength * n][x] = outline[y + sidelength * n][x]
        if corner2:
            for x in range(sidelength - outlinelength, sidelength):
                for y in range(outlinelength):
                    image[y + sidelength * n][x] = outline[y + sidelength * n][x]
        if corner3:
            for x in range(outlinelength):
                for y in range(sidelength - outlinelength, sidelength):
                    image[y + sidelength * n][x] = outline[y + sidelength * n][x]
        if corner4:
            for x in range(sidelength - outlinelength, sidelength):
                for y in range(sidelength - outlinelength, sidelength):
                    image[y + sidelength * n][x] = outline[y + sidelength * n][x]
        if side1:
            for x in range(outlinelength, sidelength - outlinelength):
                for y in range(outlinelength):
                    image[y + sidelength * n][x] = outline[y + sidelength * n][x]
        if side2:
            for x in range(outlinelength):
                for y in range(outlinelength, sidelength - outlinelength):
                    image[y + sidelength * n][x] = outline[y + sidelength * n][x]
        if side3:
            for x in range(sidelength - outlinelength, sidelength):
                for y in range(outlinelength, sidelength - outlinelength):
                    image[y + sidelength * n][x] = outline[y + sidelength * n][x]
        if side4:
            for x in range(outlinelength, sidelength - outlinelength):
                for y in range(sidelength - outlinelength, sidelength):
                    image[y + sidelength * n][x] = outline[y + sidelength * n][x]
    return image


def main():
    t = cv2.imread('texture.png')
    o = cv2.imread('outline.png')
    animation_frames = len(t) // len(t[0])
    while True:
        try:
            w = int(input('Outline width: '))
            start = time()
            break
        except ValueError:
            print("Please enter an integer!")
    if len(t) == len(o):
        try:
            mkdir("result")
        except FileExistsError:
            ...
        with open("connected_tile.txt", "r") as f:
            lines = f.readlines()
            for i in range(47):
                result = draw_outline(bool(int(lines[i][0])), bool(int(lines[i][1])), bool(int(lines[i][2])),
                                      bool(int(lines[i][3])), bool(int(lines[i][4])), bool(int(lines[i][5])),
                                      bool(int(lines[i][6])), bool(int(lines[i][7])), animation_frames, w, t, o)
                cv2.imwrite(f"result/{str(i)}.png", result)
        input(f"Finished in {int(100*(time() - start))} milliseconds. Press ENTER to leave.")
    else:
        input('Width of texture.png and outline.png does not match.\nPress ENTER to leave')


if __name__ == '__main__':
    main()
