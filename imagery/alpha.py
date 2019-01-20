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
    J = alphas[3:20, 240:257, 1]
    K = alphas[2:20, 266:282, 1]
    L = alphas[5:19, 292:306, 1]
    M = alphas[2:20, 319:335, 1]

    N = alphas[27:48, 6:24, 1]
    O = alphas[28:48, 35:47, 1]
    P = alphas[28:49, 58:72, 1]
    Q = alphas[28:50, 86:100, 1]
    R = alphas[27:47, 111:127, 1]
    S = alphas[27:47, 136:151, 1]
    T = alphas[27:47, 166:177, 1]
    U = alphas[27:47, 189:205, 1]
    V = alphas[27:47, 216:232, 1]
    W = alphas[27:47, 241:257, 1]
    X = alphas[27:47, 267:283, 1]
    Y = alphas[27:47, 294:310, 1]
    Z = alphas[27:47, 319:335, 1]
    SP = np.zeros(Z.shape)
    LETTERS = {'A': A, 'B': B, 'C': C, 'D': D,
               'E': E, 'F': F, 'G': G, 'H': H,
               'I': I, 'J': J, 'K': K, 'L': L,
               'M': M, 'N': N, 'O': O, 'P': P,
               'Q': Q, 'R': R, 'S': S, 'T': T,
               'U': U, 'V': V, 'W': W, 'X': X,
               'Y': Y, 'Z': Z,
               ' ': SP}
    return LETTERS


def spell_word(word, Letters, show):
    letter_data = {}
    padding = 10
    f = plt.figure()
    sample = []
    image = []
    sizes = []
    dx = 0
    dy = 0
    letter_data['word'] = word
    letter_data['shapes'] = []
    letter_data['cm_pos'] = []  # Center Of Mass Position for letter image
    line_breaks = False



    if len(list(word)) > 45:
        line_breaks = True
        print str(len(list(word))) + " Characters in Word"
        print "Adding line breaks"
    for element in list(word):
        if str(element).upper() in Letters.keys():
            try:
                alpha = Letters[str(element).upper()]
                sizes.append(alpha)
                dx += alpha.shape[0]
                dy += alpha.shape[1]
            except KeyError:
                print "Unknown Character "+str(element).upper()+" !"
    x = 1
    y = 1
    i = 0
    ii = 0
    breaker = False
    Word = np.zeros((100, dy + padding))
    print "* Creating Word with shape " + str(Word.shape)
    for frame in sizes:
        dX = np.array(frame.shape[0])
        dY = np.array(frame.shape[1])
        i += 1
        ii += 1
        try:
            Word[padding+x: x + dX+padding, y: y + dY] = np.array(frame)
            letter_data['shapes'].append(np.array(frame).shape)
            letter_data['cm_pos'].append(np.array([padding+x,x + dX+padding, y, y + dY]))
            # print str(np.array(frame).shape)+': '+\
            #       str(np.array(frame).shape[0]*np.array(frame).shape[1])
            sample.append([plt.imshow(Word, 'gray_r')])
            image.append(Word)
        except ValueError:
            pass
        if line_breaks and i > 40:
            breaker = True
        if line_breaks and i > 40 and list(word).pop(ii) == ' ' and breaker:
            i = 0
            padding += 20
            y = 1
            breaker = False
        y += dY

    if show:
        a = animation.ArtistAnimation(f,sample,interval=500,blit=True,repeat_delay=900)
        plt.imshow(word,'gray_r')
        plt.show()
    return image, letter_data


def text_alignment(frame, letter_data):
    print frame.shape


def dump_letter_data(letter_data, words):
    print "LETTER | SHAPE : {y1, y2, x1, x2} "
    i = 0
    for element in letter_data['shapes']:
        print str(list(words).pop(i)) + ' ' + str(element) + " : " +\
              str(letter_data['cm_pos'][i])
        i += 1


def main():
    Letters = create_alphabet_scrapbook()
    test_phrase = '   The quick brown fox jumps over the lazy dog '
    long_phrase = test_phrase+'But then the fox eats the dog Nat Geo style real quick'
    if 'example' in sys.argv:
        word, letter_info = spell_word(long_phrase, Letters, False)
        stamped_word = word.pop()
        plt.figure(figsize=(14,2))
        plt.imshow(stamped_word, 'gray')
        plt.title('Un-Aligned Word')
        plt.show()
        dump_letter_data(letter_info, test_phrase)

    if 'input' in sys.argv:
        word, letter_info = spell_word(imutils.list2str(sys.argv[2:]), Letters, True)
        stamped_word = word.pop()
        plt.imshow(stamped_word, 'gray')
        plt.title('Un-Aligned Word')
        plt.show()


if __name__ == '__main__':
    main()
