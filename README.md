# BCOG200-Final-Project

I decided to change my final project because it did sound a lot like Yelp to me, too (and it felt more boring). For this project, I want to use Turtles to create a coloring book. If users don't know what to color, then they will get the option to randomize a page from my coloring book that they can work with. To make it more complex, I want to let the users be able to upload their own photo. The program will be able to make it into a 2D, lines-only picture that looks like a page out of a coloring book. From there, users will be able to color between the lines. 

a. Function 1 will ask users to upload a picture of their choice or randomize a page.
def input_image():
  - if a user inputs an image, then it will save it and use it. this function will most likely be called in the next function to.
  - else: the program will give user a random page to use.

b. Funcion 2 will go about tracing the image and finding the main shapes that will let it become all black lines that the user can color over. 
def image_trace:
  - this function will trace over the main shapes of an image and turn it into something the user can color over. i feel like this might take the most work since i would want it to look pretty similar to their real life photo, and make it black and white.

c. Function 3 will use Turtles to let the user color on the page and make it interactive. 
  - this function will take some time as it is the most user-interactive. users will be abel to pick from a color wheel and probably change between a couple different brush sizes to work and color with the page.

I will take an image as input data. this will come as an image folder found with a file pathway upload of coloring pages i choose to give the user if they do not upload their own. if they choose to input their own, I will have to figure out to let users uplad their own image. 

