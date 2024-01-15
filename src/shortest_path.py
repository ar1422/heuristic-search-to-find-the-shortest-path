"""
Author: Arya Girisha Rao(ar1422@rit.edu)
This is a python file for the problem - https://cs.rit.edu/~jro/courses/intelSys/labs/orienteering/
"""

import sys
from graph import Graph
from a_star import AStar

PARAMETER_ERROR_MSG = "Please provide terrain-image, elevation-file, path-file, output-image-filename parameters"
TOTAL_DISTANCE_MSG = "Total Distance from cost_map: {} m"


class ShortestPath(object):
    """
    Class for the Lab actual code - Summer Orienteering.
    """

    def __init__(self):
        if len(sys.argv) != 5:
            raise ValueError(PARAMETER_ERROR_MSG)

        self.dimension = (395, 500)
        self.input_graph = Graph(self.dimension, sys.argv[1], sys.argv[2], sys.argv[4])
        self.input_filename = sys.argv[1]
        self.output_filename = sys.argv[4]
        self.points_list = self.process_path_file(sys.argv[3])
        self.destination_point = None

    def process_path_file(self, path_file):
        points_list = []
        with open(path_file) as f:
            for line in f:
                x_val, y_val = line.strip().split()
                points_list.append((int(x_val), int(y_val)))

        self.destination_point = points_list[-1]
        return points_list

    @staticmethod
    def get_points_on_path(path_map, destination):
        output_list = [destination]
        temp = path_map[destination]

        while temp is not None:
            output_list.append(temp)
            temp = path_map[temp]

        return output_list[::-1]

    def run(self):
        a_star = AStar(self.input_graph)
        total_distance = 0
        output_points = []

        for i in range(len(self.points_list) - 1):
            path_map, cost_map = a_star.a_star_search(self.points_list[i], self.points_list[i + 1])
            output_points.extend(self.get_points_on_path(path_map, self.points_list[i + 1]))
            total_distance += cost_map[self.points_list[i + 1]]

        self.input_graph.change_color_of_points(output_points, self.points_list)
        print(TOTAL_DISTANCE_MSG.format(total_distance))


def main():
    so = ShortestPath()
    so.run()


if __name__ == '__main__':
    main()
