import matplotlib.pyplot as plt, matplotlib.animation as animation
import numpy as np, scipy.ndimage as ndi, imutils, sys

A1 = {'x1':140,
          'x2':350,
          'y1':140,
          'y2':350}

A2 = {'x1': 150,
          'x2': 250,
          'y1': 150,
          'y2': 300}

lens = [[1,2,1,2,1],
            [2,1,1,1,2],
            [1,1,1,1,1],
            [2,1,1,1,2],
            [1,2,1,2,1]]


def gray_experiment(box,state):
    f = plt.figure()
    plt.title('Fade To Black')
    graydient = []
    N = 80
    for i in range(N):
        npts = 70 * N
        for i in range(npts):
            pt = imutils.spawn_random_point(imutils.crop(box, A1, False))
            box[pt[0], pt[1]] = 1
        graydient.append([plt.imshow(ndi.convolve(box, lens), 'gray_r')])
    a = animation.ArtistAnimation(f, graydient, interval=70, blit=True, repeat_delay=900)
    plt.show()
    box1 = imutils.draw_centered_box(state, 200, False)
    f = plt.figure()
    plt.title('Fade To Black')
    graydient = []
    N = 90
    for i in range(N):
        npts = 25 * N
        for i in range(npts):
            pt = imutils.spawn_random_point(imutils.crop(box1, A1, False))
            box1[pt[0], pt[1]] = 1
        graydient.append([plt.imshow(ndi.convolve(box1, lens), 'gray_r')])
    a = animation.ArtistAnimation(f, graydient, interval=80, blit=True, repeat_delay=900)
    plt.show()


def griddy(state_2):
    box = imutils.draw_centered_box(state_2, 200, False)
    f = plt.figure()
    gridiron = []
    for i in np.arange(2, 25, 1):
        test_img = imutils.add_grid(box, i, False)
        zoom = {'x1': test_img.shape[0] / 4,
                'x2': test_img.shape[0] - test_img.shape[0] / 4,
                'y1': test_img.shape[1] / 3,
                'y2': test_img.shape[1] - test_img.shape[1] / 3}
        test_img = imutils.crop(test_img, zoom, False)
        gridiron.append([plt.imshow(test_img, 'gray_r')])
    a = animation.ArtistAnimation(f, gridiron, interval=80, blit=True, repeat_delay=900)
    plt.show()
    return test_img


def main():
    huge = [1264, 1680]
    basic = [720, 1024]
    standard = [480, 720]

    state_0 = np.zeros(standard)
    state_1 = np.zeros(basic)
    state_2 = np.zeros(huge)

    if 'test' in sys.argv:
        gray_experiment(imutils.draw_centered_box(state_1,100,False),state_1)

    if 'grid' in sys.argv:
        griddy(state_2)


if __name__ == '__main__':
    main()

