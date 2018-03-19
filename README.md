# Image Resizer

Resize jpg and png images. Choose width, height to change. Besides to keep the ratio you should use scale optiosn instead width or height. Point the path of the new image or it will be save with the original one.

# Quickstart

The script requires the installed Python interpreter version 3.6.
In order to install **Pillow** library, use:

```bash
$ pip install -r requirements.txt
```

```bash
$ python image_resize.py --input /home/Boat.png --scale 0.5 --output /home/pictures/
Image saved: /home/pictures/Boat__593x342.png
```
Use **--help** to see other options:
```bash
 usage:  img_resize.py [-h] [ [--width WIDTH] [--height HEIGHT] | [--scale SCALE] [--output OUTPUT] --input INPUT

optional arguments:
  -h, --help       show this help message and exit
  --width WIDTH    Output image width
  --scale SCALE    Output image scale
  --height HEIGHT  Output image height
  --output OUTPUT  Ouput image path
  --input INPUT    Input image
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
