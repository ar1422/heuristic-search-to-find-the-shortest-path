from PIL import Image
from point import Point


class Graph(object):
    """
    Class to represent the image as a Graph with each nodes being nodes.
    """

    def __init__(self, dimension, input_image, elevation_filename):
        self.dimension = dimension
        self.image_obj = Image.open(input_image)
        self.points_map = self._add_all_points(elevation_filename)

    def _add_all_points(self, elevation_filename):

        elevation_data = self.process_elevation_file(elevation_filename)
        points_list_map = {}

        for i in range(self.dimension[0]):
            for j in range(self.dimension[1]):
                points_list_map[(i, j)] = Point(i, j, elevation_data[j][i], self.image_obj.getpixel((i, j))[:3])

        return points_list_map

    def get_neighbor_points(self, point):

        eight_direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        list_of_neighbors = []

        for direction in eight_direction:
            neighbor_coordinates = (point[0] + direction[0], point[1] + direction[1])
            if neighbor_coordinates in self.points_map:
                list_of_neighbors.append(neighbor_coordinates)

        return list_of_neighbors
