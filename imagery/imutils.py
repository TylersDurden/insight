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


def split_channels(imgIn, show):
    name = imgIn.split('/').pop()
    imgIn = plt.imread(imgIn)
    channels = {'c1': imgIn[:, :, 0],
                'c2': imgIn[:, :, 1],
                'c3': imgIn[:, :, 2],
                'label': name}
    if show:
        f, ax = plt.subplots(1, 4, figsize=(12, 5), sharex=True, sharey=True)
        plt.title(name)
        ax[0].imshow(imgIn[:, :, 0])
        ax[0].set_title(name + ' CH1')
        ax[1].imshow(imgIn[:, :, 1])
        ax[1].set_title(name + ' CH2')
        ax[2].imshow(imgIn[:, :, 2])
        ax[2].set_title(name + ' CH3')
        ax[3].imshow(imgIn[:, :, 1], 'gray')
        ax[3].set_title(name + ' CH1 [Gray]')
        plt.show()
    return channels


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


def render_image(imat, title, color):
    if not color:
        plt.imshow(imat, 'gray')
        plt.title(title)
        plt.show()
    else:
        plt.imshow(imat)
        plt.title(title)
        plt.show()


def draw_centered_box(canvas, box_size, show):
    cx = canvas.shape[0]/2
    cy = canvas.shape[1]/2
    canvas[cx-box_size:cx+box_size,
           cy-box_size:cy+box_size] = 1
    if show:
        plt.figure()
        plt.imshow(canvas, 'gray_r')
        plt.title('Box')
        plt.show()
    return canvas


def draw_box(box_data, canvas, show):
    x1 = box_data['x1']
    x2 = box_data['x2']
    y1 = box_data['y1']
    y2 = box_data['y2']
    canvas[x1:x2,y1:y2] = 1
    if show:
        f = plt.figure()
        plt.imshow(canvas, 'gray_r')
        plt.title(' Canvas ')
        plt.show()
    return canvas


def crop(canvas, area, show):
    x1 = area['x1']
    x2 = area['x2']
    y1 = area['y1']
    y2 = area['y2']
    region = canvas[y1:y2, x1:x2]
    if show:
        f, ax = plt.subplots(1,2,sharey=False)
        ax[0].imshow(canvas, 'gray_r')
        ax[0].set_title('Original')
        ax[1].imshow(region, 'gray_r')
        ax[1].set_title('Cropped')
        plt.show()
    return region


def define_area():
    print "-----| DEFINE {x1,x2,y1,y2} |-----"
    x1 = int(input('Enter x1: '))
    x2 = int(input('Enter x2: '))
    y1 = int(input('Enter y1: '))
    y2 = int(input('Enter y2: '))
    print "----------------------------------"
    bounds = {'x1': x1,
              'x2': x2,
              'y1': y1,
              'y2': y2}
    return bounds


def scale_box(self, factor, verbose):
    """
    Take a [Shape].box primitive, and
    scale it up by the factor given.
    If verbose, show the box before and after.
    :param factor:
    :param verbose:
    :return:
    """
    # Take the small box primitive and scale it
    box = np.array(self.hardcoded_shapes['box'])
    current_box_dims = [int(np.sqrt(box.sum())),
                        int(np.sqrt(box.sum()))]
    # Define new box dimensions before white padding
    new_dims = [int(factor * current_box_dims[0]),
                int(factor * current_box_dims[0])]
    newbox = np.ones(new_dims)
    # Add the white space padding around the box
    row_padding = np.zeros((1, new_dims[0] + 2))
    col_padding = np.zeros((new_dims[1], 1))
    newbox = np.concatenate((col_padding, newbox, col_padding), 1)
    newbox = np.concatenate((row_padding, newbox, row_padding), 0)
    # If verbose, show the box
    if verbose:
        print "Box Dims: " + str(current_box_dims) + \
              "  [" + str(box.shape) + "]"
        print "New Box Dims: " + str(new_dims) + \
              "  [" + str(newbox.shape) + "]"

        f, ax = plt.subplots(1, 2)
        ax[0].imshow(box, 'gray_r')
        ax[1].imshow(newbox, 'gray_r')
        plt.show()
    return newbox


def create_square_lattice(box_sz, dims, layout, show):
    """
    Create a grid of square boxes with the given layout
    I.E [4x4] yields a grid of 4 boxes by 4 boxes.
    :param box_sz:
    :param dims:
    :param layout:
    :param show:
    :return state:
    """
    state = np.zeros(dims)
    nr = state.shape[0] / layout[0]
    nc = state.shape[1] / layout[1]

    row_size = np.arange(2 * box_sz, state.shape[0] + 2 * box_sz, nr)
    col_size = np.arange(2 * box_sz, state.shape[1] + 2 * box_sz, nc)

    for i in row_size:
        for j in col_size:
            state[i - box_sz:i + box_sz, j - box_sz:j + box_sz] = 1
    if show:
        plt.imshow(state, 'gray_r')
        plt.show()
    return state


def draw_centered_circle(canvas, radius, show):
    cx = canvas.shape[0]/2
    cy = canvas.shape[1]/2
    for x in np.arange(cx - radius, cx + radius, 1):
        for y in np.arange(cy - radius, cy + radius, 1):
            r =np.sqrt((x-cx)*(x-cx) + ((cy-y)*(cy-y)))

            if r <= radius:
                canvas[x, y] = 1
    if show:
        plt.imshow(canvas, 'gray_r')
        plt.show()
    return canvas


def add_grid(canvas, divisions, show):
    width = canvas.shape[0]
    height = canvas.shape[1]

    x_grid = np.arange(0, width, divisions)
    y_grid = np.arange(0, height, divisions)
    for x in x_grid:
        canvas[x,:] = 1
    for y in y_grid:
        canvas[:,y] = 1
    if show:
        plt.imshow(canvas, 'gray_r')
        plt.show()
    return canvas

