import matplotlib.pyplot as plt, matplotlib.animation as animation
import numpy as np, imutils, sys, os


def create_alphabet_scrapbook():
    letters = imutils.pwd() + '/Letters.png'
    alphas = imutils.load_image(letters, True)
    dims = alphas.shape

    A = alphas[2:20, 5:20, 1]
    B = alphas[2:20, 32:47, 1]
    C = alphas[2:20, 60:75, 1]
    D = alphas[2:20, 85:100, 1]
    E = alphas[2:20, 110:127, 1]
    F = alphas[2:20, 138:153, 1]
    G = alphas[2:20, 163:178, 1]
    H = alphas[2:20, 187:205, 1]
    I = alphas[2:20, 216:230, 1]
    J = alphas[2:20, 240:257, 1]
    K = alphas[2:20, 266:282, 1]
    L = alphas[2:20, 292:305, 1]
    M = alphas[2:20, 319:335, 1]

    N = alphas[27:50, 6:25, 1]
    O = alphas[27:50, 32:48, 1]
    P = alphas[27:50, 58:74, 1]
    Q = alphas[27:50, 86:100, 1]
    R = alphas[27:50, 111:127, 1]
    S = alphas[27:50, 136:151, 1]
    T = alphas[27:50, 166:179, 1]
    U = alphas[27:50, 189:205, 1]
    V = alphas[27:50, 216:232, 1]
    W = alphas[27:50, 241:257, 1]
    X = alphas[27:50, 267:283, 1]
    Y = alphas[27:50, 294:310, 1]
    Z = alphas[27:50, 319:335, 1]
    SP = np.zeros(Z.shape)
    LETTERS = {'A': A, 'B': B, 'C': C, 'D': D,
               'E': E, 'F': F, 'G': G, 'H': H,
               'I': I, 'J': J, 'K': K, 'L': L,
               'M': N, 'O': O, 'P': P, 'Q': Q,
               'R': R, 'S': S, 'T': T, 'U': U,
               'V': V, 'W': W, 'X': X, 'Y': Y,
               'Z': Z,
               ' ': SP}
    return LETTERS


def spell_word(word, Letters, show):
    padding = 10
    f = plt.figure()
    sample = []
    sizes = []
    dx = 0
    dy = 0
    for element in list(word):
        if str(element).upper() in Letters.keys():
            try:
                alpha = Letters[str(element).upper()]
                # sample.append([plt.imshow(alpha, 'gray_r')])
                sizes.append(alpha)
                dx += alpha.shape[0]
                dy += alpha.shape[1]
                print alpha.shape
            except KeyError:
                print "Unknown Character "+str(element).upper()+" !"
    x = 1
    y = 1
    word = np.zeros((50, dy + padding))
    print "* Creating Word with shape " + str(word.shape)
    for frame in sizes:
        dX = np.array(frame.shape[0])
        dY = np.array(frame.shape[1])
        try:
            word[padding+x: x + dX+padding, y: y + dY] = np.array(frame)
            sample.append([plt.imshow(word, 'gray_r')])
        except ValueError:
            pass
        # x += dX
        y += dY
    if show:
        a = animation.ArtistAnimation(f,sample,interval=500,blit=True,repeat_delay=900)
        plt.imshow(word,'gray')
        plt.show()
    return sample


def main():
    Letters = create_alphabet_scrapbook()

    if 'example' in sys.argv:
        word = spell_word('Hello World', Letters, True)

    if 'input' in sys.argv:
        word = spell_word(str(input('Enter Some Text: ')), Letters, True)


if __name__ == '__main__':
    main()
