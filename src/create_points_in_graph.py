from PIL import Image
from point import Point


def create_list_of_points(dimension, input_image_filename, elevation_data):
    """
    Function to create tht list of points from the input image filename
    :param dimension:
    :param input_image_filename:
    :param elevation_data:
    :return:
    """

    image_obj = Image.open(input_image_filename)
    points_list_map = {}
    for i in range(dimension[0]):
        for j in range(dimension[1]):
            points_list_map[(i, j)] = Point(i, j, elevation_data[j][i], image_obj.getpixel((i, j))[:3])

    return points_list_map
