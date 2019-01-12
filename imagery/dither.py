import matplotlib.pyplot as plt, scipy.ndimage as ndi
import numpy as np, imutils, sys


def view_channel(img_channels, which):
    plt.imshow(img_channels[which])
    plt.title(img_channels['label']+' '+which)
    plt.show()


def main():
    Verbose = False
    
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

        print str(color_chanels['c1'].shape)+" Image Cropped to " + str(img_slice.shape)
        imutils.render_image(img_slice,'Cropped '+color_chanels['label'], False)


if __name__ == '__main__':
    main()
