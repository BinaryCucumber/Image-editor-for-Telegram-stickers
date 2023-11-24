from PIL import Image
import os
import glob


path = "C://Users/Vsevolod/Menu/Desktop/NoEditedStikers/*.*"
path2 = "C://Users/Vsevolod/Menu/Desktop/Edited for STIKERS/"

for file in glob.glob(path):
      print(file)
      filename = os.path.basename(file)
      image = Image.open(file)
      resized_image = image.resize((512, 512))
      if ".jpg" in filename:
            filename = filename.removesuffix('.jpg')
      resized_image.save(path2 + filename + '.png')
      print("File " + filename +" is edited")
