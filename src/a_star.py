import heapq
import math
from a_star_constants import COLOR_TO_SPEED_MAP


class AStar(object):
    """
    Class for AStar algorithm and all relevant functions.
    """
    def __init__(self, graph):
        self.values = []
        self.graph = graph

    def push_to_heap(self, value, priority):
        heapq.heappush(self.values, (priority, value))

    def pop_from_heap(self):
        return heapq.heappop(self.values)[1]

    @staticmethod
    def heuristic_function(neighbor_point, end_point):
        distance = AStar.calculate_distance(neighbor_point, end_point)
        return distance / COLOR_TO_SPEED_MAP[neighbor_point.color]

    @staticmethod
    def calculate_distance(point_1, point_2):
        x_value = math.pow((point_1.x - point_2.x) * 10.29, 2)
        y_value = math.pow((point_1.y - point_2.y) * 7.55, 2)
        e_value = math.pow(point_1.elevation - point_2.elevation, 2)
        distance = math.sqrt(x_value + y_value + e_value)
        return distance

    @staticmethod
    def cost_function(current_point, neighbor_point):
        distance = AStar.calculate_distance(current_point, neighbor_point)
        return distance / COLOR_TO_SPEED_MAP[neighbor_point.color]

    def a_star_search(self, start, goal):

        self.push_to_heap(start, 0)
        path_map = {start: None}
        cost_map = {start: 0.0}
        distance_map = {start: 0.0}
        while len(self.values):

            current = self.pop_from_heap()
            if current == goal:
                break

            for next_neighbor in self.graph.get_neighbor_points(current):
                current_point_obj = self.graph.points_map[current]
                next_neighbor_obj = self.graph.points_map[next_neighbor]
                goal_obj = self.graph.points_map[goal]

                neighbor_cost = cost_map[current] + self.cost_function(current_point_obj, next_neighbor_obj)
                if next_neighbor not in cost_map or neighbor_cost < cost_map[next_neighbor]:
                    priority = neighbor_cost + self.heuristic_function(next_neighbor_obj, goal_obj)
                    self.push_to_heap(next_neighbor, priority)
                    path_map[next_neighbor] = current
                    cost_map[next_neighbor] = neighbor_cost
                    new_distance = distance_map[current] + self.calculate_distance(current_point_obj, next_neighbor_obj)
                    distance_map[next_neighbor] = new_distance

        self.values.clear()
        return path_map, distance_map
