import os
import cv2
import numpy as np

NUM_ITER = 3

def segment():
    # Move to segmentation
    os.chdir('Segmentation')

    # Run segmentation
    os.system('./script.sh')

    # Return to repository root
    os.chdir('..')

def adversarial():
    # Move to adversarial
    os.chdir('Adversarial')

    # Run adversarial Attack
    print('ColorFool attacking ResNet50')
    os.system('python -W ignore ColorFool.py --model=resnet50')

    # Return to the root
    os.chdir('..')

def colorize(img_bin: bytes) -> bytes:
    image = cv2.imdecode(np.frombuffer(img_bin, np.uint8), cv2.IMREAD_COLOR)
    cv2.imwrite('Dataset/image.png', image)

    segment()
    adversarial()

    with open('Adversarial/Results/ColorFoolImgs/adv_resnet50/image.png', 'rb') as f:
        out = f.read()
        return out

if __name__ == "__main__":
    with open('Dataset/image.png', 'rb') as fp:
        im_b = fp.read()
        colorize(im_b)
