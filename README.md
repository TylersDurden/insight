# [I]mages
I do a lot of programming playing with image processing, and creating algorithmic art
or doing visually based simulations (RandomWalks, Automata, etc.). To facilitate the
process of creating these programs I'm creating the ``imutils.py`` library of image
related functions I frequently use. This should be useful, and helpful for developing
more robust and logical image related projects on a larger scale. 

## Alpha *{Low_Quality Text Rendering}*
![text](https://raw.githubusercontent.com/TylersDurden/insight/master/TextRendering.png)

Pretty Crude, but takes text with any characters (A-Z) and
renders an image of the equivalent text. It also adds a newline
if there's enough words in the text input. 

![long words](https://raw.githubusercontent.com/TylersDurden/insight/master/TypeFace.png)

## imutils
This library of useful image related functions covers quite a lot of utilities that
makes later programming much more concise. Here's an overview of what imutils holds:
 ________________________
 * draw_centered_box
  
  ``
  Given (state, boxsize, show) a box is rendered in center of
  the given state in the center with a width and height of 2X
  boxsize. If show == true, the image is rendered. ``
-------------------------
 * draw_grid
 
 `
 Overlay a grid of a given density on a state. 
 Passing true for the show flag will let you preview the 
 new state before returning it.
 `         
------------------------
 * crop
 
 ``
 Crop and image to the given {x1,y1,x2,y2} window. 
 ``
------------------------
 * rendering

 ``
Passing in an image matrix, a label, and an isColor flag, 
and image is rendered/plotted and given a generic label. 
 `
------------------------
 * ind2sub/sub2ind

 ``
Given the Folowwing Matrix: 
A = [[1,0,2,3],
     [0,3,1,2],
     [0,0,2,0],
     [1,2,0,1]]
 ind2sub(3,A) = 2
 sub2ind(3,A) = [2,0]
 ``
 ------------------------
 * split_color_channels

 ``
Given the input matrix of an image, return a mapping
of all three [R, G, B] color channels.  
 ``
------------------------
___________________________
