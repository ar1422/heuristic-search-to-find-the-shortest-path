class Graph(object):
    """
    Class to represent the image as a Graph with each nodes being nodes.
    """

    def __init__(self, points_map):
        self.points_map = points_map

    def get_neighbor_points(self, point):

        eight_direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        list_of_neighbors = []

        for direction in eight_direction:
            neighbor_coordinates = (point[0] + direction[0], point[1] + direction[1])
            if neighbor_coordinates in self.points_map:
                list_of_neighbors.append(neighbor_coordinates)

        return list_of_neighbors
