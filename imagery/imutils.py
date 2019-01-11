import matplotlib.pyplot as plt, matplotlib.animation as animation
import numpy as np


def load_image(path2pic, verbose):
    """

    :param path2pic:
    :param verbose:
    :return:
    """
    img = plt.imread(path2pic)
    if verbose:
        print "Found "+path2pic
        print 'Shape: ' + str(img.shape)
    return img


def render_bw(matrices, frame_rate):
    """
    Render the given matrices one by one,
    at the designated frame rate, using the
    matplotlib animation library.
    [IN BLACK AND WHITE]
    :param matrices:
    :param frame_rate:
    :return:
    """
    film = []
    f = plt.figure()
    for frame in matrices:
        film.append([plt.imshow(frame, 'gray_r')])
    a = animation.ArtistAnimation(f, film, interval=frame_rate, blit=True, repeat_delay=900)
    plt.show()


def render_color(matrices, frame_rate):
    """
    Render the given matrices one by one,
    at the designated frame rate, using the
    matplotlib animation library.
    [IN COLOR]
    :param matrices:
    :param frame_rate:
    :return:
    """
    film = []
    f= plt.figure()
    for frame in matrices:
        film.append([plt.imshow(frame)])
    a = animation.ArtistAnimation(f, film, interval=frame_rate, blit=True, repeat_delay=900)
    plt.show()


def ind2sub(index,dims):
    """
    Given an index and array dimensions,
    convert an index to [x,y] subscript pair.
    :param index:
    :param dims:
    :return tuple - subscripts :
    """
    subs = []
    ii = 0
    for y in range(dims[1]):
        for x in range(dims[0]):
            if index == ii:
                subs = [x,y]
            ii +=1
    return subs


def sub2ind(subs, dims):
    """
    Given a 2D Array's subscripts, return it's
    flattened index
    :param subs:
    :param dims:
    :return:
    """
    ii = 0
    indice = 0
    for y in range(dims[1]):
        for x in range(dims[0]):
            if subs[0] == x and subs[1] == y:
                indice = ii
            ii += 1
    return indice


def spawn_random_point(state):
    # Initialize a random position
    x = np.random.randint(0, state.shape[0], 1, dtype=int)
    y = np.random.randint(0, state.shape[1], 1, dtype=int)
    return [x, y]


def render_image(imat, title):
    f = plt.figure()
    plt.imshow(imat, 'gray_r')
    plt.title(title)
    plt.show()

