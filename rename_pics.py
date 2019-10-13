import os
# Function to rename multiple files 
 
i = 0
   
for filename in os.listdir("in"): 
    dst = str(i) + ".jpg"
    src ='in/'+ filename 
    dst ='in/'+ dst 
        
    # rename() function will 
    # rename all the files 
    os.rename(src, dst) 
    i += 1