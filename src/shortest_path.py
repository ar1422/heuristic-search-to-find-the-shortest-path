"""
Author: Arya Girisha Rao(ar1422@rit.edu)
This is a python file for the problem - https://cs.rit.edu/~jro/courses/intelSys/labs/orienteering/
"""

import sys
from a_star import AStar
from process_path_file import process_path_file

PARAMETER_ERROR_MSG = "Please provide terrain-image, elevation-file, path-file, output-image-filename parameters"
TOTAL_DISTANCE_MSG = "Total Distance from cost_map: {} m"


class ShortestPath(object):
    """
    Class for the Lab actual code - Summer Orienteering.
    """

    def __init__(self, input_graph):
        if len(sys.argv) != 5:
            raise ValueError(PARAMETER_ERROR_MSG)

        self.dimension = (395, 500)
        self.input_graph = input_graph
        self.input_filename = sys.argv[1]
        self.output_filename = sys.argv[4]
        self.points_list = process_path_file(sys.argv[3])
        self.destination_point = self.points_list[-1]

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
