#BIMP - Batch Image Manipulating with Python

""" 
 Author; Mark Pedersen @makerspender
 License: CC BY 2.0 https://creativecommons.org/licenses/by/2.0/
"""
#load required libraries
import PIL
import csv
import textwrap
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import os 


#create lists to store quotes and authors in
lines = [line.rstrip() for line in open('output.csv')]
authors = [author.rstrip() for author in open('input.csv')]

#start the for loop
for idx, val in enumerate(lines):
    try:
    #echo each quote and author
        print(idx, val)

    #create main quote value
        para = textwrap.wrap(val, width=40)

    #set image dimensions
        MAX_W, MAX_H = 1920, 1280

    #set image location
        imageFile = "/home/jboren/Documents/Code/Hackathon/automator/PillowAutoImage/in/{}.jpg".format(idx)

    #assign im to pillow and open the image
        im = Image.open(imageFile)#.convert('RGBA')

    #resize the image to our chosen proportions and use antialiasing
        im = im.resize((1920, 1280), Image.ANTIALIAS)

    #create new layer for adding opacity 
        poly = Image.new('RGBA', (1920,1280))
        polydraw = ImageDraw.Draw(poly)

    #fill the image with black and 165/255 opacity
        polydraw.rectangle([(0,0),(1920,1280)], fill=(0,0,0,165), outline=None)
        
    #paste in the layer on top of the image im
        im.paste(poly,mask=poly)

    #command to start merging layers
        draw = ImageDraw.Draw(im)

    #setting up fonts
        font = ImageFont.truetype("Padauk-Regular.ttf",80)
        authorfont = ImageFont.truetype("Padauk-Regular.ttf",60)
        linkfont = ImageFont.truetype("Padauk-Regular.ttf",24)

    #setting up padding and positioning for quote text
        current_h, pad = 300, 50

    #for loop breaking up each quote into lines not exceeding the width of the image dimensions	
        for line in para:
            w, h = draw.textsize(line, font=font) #
            draw.text(((MAX_W - w) / 2, current_h), line , font=font) #
            current_h += h + pad

    #setting up padding and positioning for author text
        current_h2, pad2 = 900, 80
        currentauthor = authors[idx]
        w, h = draw.textsize(currentauthor) # , font=authorfont
        draw.text(((MAX_W - w) / 2, (current_h + 100)), currentauthor, font=authorfont) # 
        current_h2 += h + pad2

    #setting up padding and positining for optional text
        current_h3, pad3 = 1200, 30
        sitelink = "TensorRandos"
        w, h = draw.textsize(sitelink) # , font=linkfont
        draw.text(((MAX_W - w) / 2, current_h3), sitelink, font=linkfont) # 
        current_h3 += h + pad3

    # #loading optional logo and converting to RGBA for transparency support
    #     logo = Image.open('kmeans_jjb.png').convert('RGBA')
    #     logo_w, logo_h = logo.size
    #     im.paste(logo, (50,1150), logo)

    #saving the image to our chosen location
        im.save("/home/jboren/Documents/Code/Hackathon/automator/InstaAutomator/post/image_{}.jpg".format(idx))
    except:
        continue