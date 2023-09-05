from PIL import Image, ImageDraw


class Point(object):
    """
    Class to Represent a single point in the image.
    Contains (x, y) co-ordinates, elevation at the point (x, y) and color of the pixel.
    """

    def __init__(self, x, y, elevation, color):
        self.x = x
        self.y = y
        self.elevation = elevation
        self.color = color

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y) + " elevation: " + \
               str(self.elevation) + " color: " + str(self.color)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.elevation == other.elevation


class Graph(object):
    """
    Class to represent the image as a Graph with each nodes being nodes.

    """

    def __init__(self, dimension, input_image, elevation_filename, output_filename):
        self.dimension = dimension
        self.image_obj = Image.open(input_image)
        self.output_filename = output_filename
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

    def change_color_of_points(self, points, stop_points):
        draw = ImageDraw.Draw(self.image_obj)
        draw.line(points, fill="red", width=1)
        for point in stop_points:
            self.image_obj.putpixel(point, (108, 36, 134))
        self.image_obj.save(self.output_filename)

    @staticmethod
    def process_elevation_file(elevation_filename):
        elevation_data = []
        with open(elevation_filename) as f:
            for line in f:
                raw_line = line.strip().split()
                elevation_values = [float(x) for x in raw_line[:-5]]
                elevation_data.append(elevation_values)

        return elevation_data
