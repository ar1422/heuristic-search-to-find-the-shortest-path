from PIL import Image, ImageDraw


def change_color_of_points(input_image, points, stop_points, output_image_filename):
    """
    Function to change the color of the points to highlight the shortest path.
    :param input_image:
    :param points:
    :param stop_points:
    :param output_image_filename:
    :return:
    """
    image_obj = Image.open(input_image)
    draw = ImageDraw.Draw(image_obj)
    draw.line(points, fill="red", width=1)
    for point in stop_points:
        image_obj.putpixel(point, (108, 36, 134))
    image_obj.save(output_image_filename)





