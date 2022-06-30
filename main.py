import cv2
from os import mkdir


def draw_outline(name, corner1, corner2, corner3, corner4, side1, side2, side3, side4, frames, outlinelength, texture,
                 outline):
    image = texture.copy()
    sidelength = len(texture[0])

    for n in range(frames):
        if corner1:
            for width in range(outlinelength):
                for length in range(outlinelength):
                    image[width + sidelength * n][length] = outline[width + sidelength * n][length]
        if corner2:
            for length in range(sidelength - outlinelength, sidelength):
                for width in range(outlinelength):
                    image[width + sidelength * n][length] = outline[width + sidelength * n][length]
        if corner3:
            for width in range(sidelength - outlinelength, sidelength):
                for length in range(outlinelength):
                    image[width + sidelength * n][length] = outline[width + sidelength * n][length]
        if corner4:
            for width in range(sidelength - outlinelength, sidelength):
                for length in range(sidelength - outlinelength, sidelength):
                    image[width + sidelength * n][length] = outline[width + sidelength * n][length]
        if side1:
            for length in range(outlinelength, sidelength - outlinelength):
                for width in range(outlinelength):
                    image[width + sidelength * n][length] = outline[width + sidelength * n][length]
        if side2:
            for length in range(outlinelength):
                for width in range(outlinelength, sidelength - outlinelength):
                    image[width + sidelength * n][length] = outline[width + sidelength * n][length]
        if side3:
            for width in range(outlinelength - sidelength, sidelength):
                for length in range(sidelength - outlinelength, sidelength):
                    image[width + sidelength * n][length] = outline[width + sidelength * n][length]
        if side4:
            for length in range(outlinelength, sidelength - outlinelength):
                for width in range(sidelength - outlinelength, sidelength):
                    image[width + sidelength * n][length] = outline[width + sidelength * n][length]
    cv2.imwrite(f"result/{str(name)}.png", image)


def main():
    t = cv2.imread('texture.png')
    o = cv2.imread('outline.png')
    while True:
        try:
            w = int(input('Outline width: '))
            animation_frames = int(input("Animation frames(if u don't know what this does enter '1'): "))
            break
        except ValueError:
            print("Please enter an integer!")
    if len(t) == len(o):
        try:
            mkdir("result")
        except FileExistsError:
            print("result folder already exists")
        with open("connected_tile.txt", "r") as f:
            lines = f.readlines()
            for i in range(47):
                c1 = bool(int(lines[i][0]))
                c2 = bool(int(lines[i][1]))
                c3 = bool(int(lines[i][2]))
                c4 = bool(int(lines[i][3]))
                s1 = bool(int(lines[i][4]))
                s2 = bool(int(lines[i][5]))
                s3 = bool(int(lines[i][6]))
                s4 = bool(int(lines[i][7]))
                draw_outline(i, c1, c2, c3, c4, s1, s2, s3, s4, animation_frames, w, t, o)
        input("Textures succesefully created, Press ENTER to leave.")
    else:
        input('Width of texture.png and outline.png does not match.\nPress ENTER to '
              'leave')


if __name__ == '__main__':
    main()

