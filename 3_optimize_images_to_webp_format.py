from PIL import Image
import os

maxWidth = 1920
optimizedPrefix = ''
OptimizationLevel = 90

imageOptimizeDirectory = os.path.join(os.getcwd(),'game','images')
filelist = os.listdir(imageOptimizeDirectory)
for file in filelist:
    if file.endswith(('jpg', 'png' )):
        print("optimizing image: "+ file)
        img = Image.open(os.path.join(imageOptimizeDirectory,file))
        img.save(os.path.join(imageOptimizeDirectory,optimizedPrefix+file.replace('.png','.webp').replace('.jpg','.webp').replace('_d.','.').replace('_c1','')),
                optimize=True,
                quality=int(OptimizationLevel),
                format = 'WEBP'
                )
        os.remove(os.path.join(imageOptimizeDirectory,file))
print('All images optimized!') 