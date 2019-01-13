import matplotlib.pyplot as plt, scipy.ndimage as ndi
import numpy as np, imutils, sys


def view_channel(img_channels, which):
    plt.imshow(img_channels[which])
    plt.title(img_channels['label']+' '+which)
    plt.show()


def raw_featured_image(imat, nLevels, show):
    iavg = imat.mean()
    largest = imat.max()
    lowest = imat.min()
    step_size = int(float(iavg-lowest)/nLevels)
    levels = np.linspace(lowest, largest, step_size)
    if show:
        print levels
    bitmap = {}
    mapbit = {}
    ii = 0
    for lvl in levels:
        bitmap[ii] = lvl
        mapbit[lvl] = ii
        print str(ii) + " : " + str(lvl)
        ii += 1

    # Now apply mapping to image
    d_image = np.ones(imat.shape).flatten()
    dims = imat.shape
    II = 0
    for cell in imat.flatten():
        d_image[II] = get_level_from_maps(bitmap, mapbit, cell, iavg)
        II += 1
    d_image = d_image.reshape(dims)
    if show:
        print d_image.min()
        f, ax = plt.subplots(1,2, sharey=True, sharex=True)
        ax[0].imshow(imat, 'gray')
        ax[0].set_title('Original Image')
        ax[1].imshow(np.abs( d_image-imat), 'gray')
        ax[1].set_title('Discrete image')
        plt.show()
    return d_image


def get_level_from_maps(int2lvl, lvl2int, value, avg):
    bit = 0
    for ii in range(1,len(lvl2int),1):
        if int2lvl[ii] >= value >= int2lvl[ii-1]:
            bit = int2lvl[ii]
        else:
            bit = int2lvl[ii-1]
    return bit


def main():
    Verbose = True

    # If operating on an existing image, load it from arguments and process data
    if 'pic' in sys.argv:
        color_chanels = imutils.split_channels(sys.argv[2], False)
        if Verbose:
            view_channel(color_chanels, 'c3')
        if '-manual' in sys.argv:
            test_area = imutils.define_area()
        else:
            # This area will crop the astronaut from buzzhole.jpg
            test_area = {'x1':10,'x2':750,'y1':100,'y2':1100}

        img_slice = imutils.crop(canvas=color_chanels['c3'],
                                 area=test_area,
                                 show=False)

        # if verbose, show the new cropped image and it's dims
        if Verbose:
            print str(color_chanels['c1'].shape) + " Image Cropped to " + str(img_slice.shape)
            imutils.render_image(img_slice, 'Cropped ' + color_chanels['label'], False)
        # Before dithering schemes, need to smooth the space with averaged bit mappings


if __name__ == '__main__':
    main()
