import scipy.ndimage as ndi, numpy as np, sys, imutils


def draw_centered_box(canvas, box_sz, show):
    center_x = int(canvas.shape[0]/2)
    center_y = int(canvas.shape[1]/2)
    canvas[center_x-box_sz:center_y+box_sz,
           center_y-box_sz:center_y+box_sz] = 1
    if show:
        imutils.render_image(canvas, 'Box')
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
        imutils.render_image(canvas, 'Grid')
    return canvas


def draw_centered_circle(canvas, radius, show):
    cx = canvas.shape[0]/2
    cy = canvas.shape[1]/2
    for x in np.arange(cx - radius, cx + radius, 1):
        for y in np.arange(cy - radius, cy + radius, 1):
            r =np.sqrt((x-cx)*(x-cx) + ((cy-y)*(cy-y)))

            if r <= radius:
                canvas[x, y] = 1
    if show:
        imutils.render_image(canvas, 'circle')
    return canvas


def main():
    width = 250
    height = 250
    if '-manual' in sys.argv:
        width = int(input('Enter width: '))
        height = int(input('Enter height: '))
    # Now create the canvas, either with user provided
    # dims, or the default ones
    canvas = np.zeros((width, height))

    box = draw_centered_box(canvas, 10, False)

    boxNgrid = add_grid(box, 10, False)

    f0 = [[1,1,1],[1,1,1],[1,1,1]]
    f1 = [[1,1,1],[1,0,1],[1,1,1]]

    imutils.render_image(ndi.convolve(boxNgrid,f0),'Grid Conv.')

    draw_centered_circle(box,30, True)


if __name__ == '__main__':
    main()

