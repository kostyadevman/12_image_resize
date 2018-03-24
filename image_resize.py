import argparse
from PIL import Image
from os.path import basename, splitext, dirname, join


def get_argument_parser():
    usage = (' img_resize.py [-h] [ [--width WIDTH] [--height HEIGHT]' 
             '| [--scale SCALE] [--output OUTPUT] --input INPUT')
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument('--width', type=int, help='Output image width')
    parser.add_argument('--scale', type=float, help='Output image  scale')
    parser.add_argument('--height', type=int, help='Output image height')
    parser.add_argument('--output', help='Ouput image path')
    parser.add_argument('--input', required=True, help='Input image')

    return parser


def open_img(path_to_file):
    try:
        image = Image.open(path_to_file)
        return image
    except FileNotFoundError as error:
        pass
    except OSError as error:
        pass


def save_img(path_to_save, image):
    image.save(path_to_save)


def get_output_img_dir_name(path_to_input_img, output_img_size):
    input_dir = dirname(path_to_input_img)
    input_img_name = basename(path_to_input_img)
    file_name, file_extension = splitext(input_img_name)
    width, height = output_img_size

    return input_dir, '{}__{}x{}{}'.format(
        file_name,
        width,
        height,
        file_extension)


def is_ratio_match_original(original_size, size):
    admissible_error = 0.05
    orig_width, orig_height = original_size
    width, height = size
    width_ratio = orig_width / width
    height_ratio = orig_height / height
    return width_ratio - height_ratio < abs(admissible_error)


def get_output_img_size(original_size, width, height, scale):
    original_width, original_height = original_size

    if scale:
        width = round(original_width * scale)
        height = round(original_height * scale)

    if width and not height:
        height = round((width / original_width) * original_height)

    if height and not width:
        width = round((original_height / height) * original_width)
        
    if not(width and height):
        width, height = original_size

    return width, height


def resize_image(original_img,  size):
    width, height = size
    width = int(width)
    height = int(height)
    return original_img.resize((width, height))


if __name__ == '__main__':
    parser = get_argument_parser()
    args = parser.parse_args()
    scale = args.scale
    width = args.width
    height = args.height

    if scale and (width or height):
        parser.error(
            'Argument --scale not allowed with --width or --height'
        )

    input_img = open_img(args.input)

    if not input_img:
        exit('Open image error')

    input_img_size = input_img.size
    output_img_size = get_output_img_size(
        input_img_size,
        width,
        height,
        scale
    )

    if not is_ratio_match_original(input_img_size, output_img_size):
        print('Warning: ratio do not  match the original')

    output_img = resize_image(input_img, output_img_size)
    output_dir, output_img_name = get_output_img_dir_name(
        args.input,
        output_img_size
    )

    if args.output:
        output_dir = args.output
    path_to_save_output_img = join(output_dir, output_img_name)

    output_img.save(path_to_save_output_img)
    print('Image saved: {}'.format(path_to_save_output_img))
