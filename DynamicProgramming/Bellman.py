import math
import cProfile
import pstats


class Bellman:
    def __init__(self, start_point, end_point, table, table_divider):
        self.start_point = Point(start_point)
        self.end_point = Point(end_point)
        self.step = int(table_divider/(end_point[1]+1))  # increment of height in range (0,4)

        self.table = table
        self.memo = {}  # memoization of previous moves
        self.path = []  # current best path
        self.minimum = math.inf  # current lowest cost

        self.bellman_recursion(self.start_point, [])
        print("\n", self.minimum, self.path, self.memo)

    def bellman_recursion(self, curr_point, result):
        curr_point.possible_moves(curr_point.point, self.end_point.point, self.step)  # generates all possible moves from curr_point
        for next_point in curr_point.combinations:  # for every point within possible points perform recursion
            key = str([curr_point.point[0], (next_point[1]-curr_point.point[1])/self.step])  # creates key for dictionary

            if key not in self.memo.keys():  # if there is no such key in memo, save it
                #  memoize for key = [sector, change_in_height] weight of that move
                self.memo[key] = self.calc_weight(curr_point, Point(next_point))

            """
            line 33-41
            Responsible for exchanging moves in result table
            """
            flag = 0
            for i in range(len(result)):
                if key[1] == result[i][1]:
                    result.pop(i)
                    result.insert(i, key)
                    flag = 1

            if flag < 1:
                result.append(key)

            #  if point's x is lower than x from end point, use recursion
            if next_point[0] < self.end_point.point[0]:
                self.bellman_recursion(Point(next_point), result)
            else:  # Otherwise save result and check if it's cost is less then current minimum.
                result = (sum([self.memo[key] for key in result]), result.copy())
                if result[0] < self.minimum:  # If it is than result is new minimum.
                    self.minimum = result[0]
                    self.path = result[1]

    def calc_weight(self, from_point, to_point):
        if to_point.point[0] in self.table.keys():  # Calculating weight/cost with use of the table
            return self.table[to_point.point[0]] * math.sqrt(1 + math.pow((from_point.point[1]/self.step - to_point.point[1]/self.step), 2))


class Point:
    def __init__(self, point_coordinates):
        self.point = point_coordinates
        self.combinations = []

    @staticmethod
    def current_sets(some_set, destination, step):
        if some_set[0] < destination[0]-1:
            y_set = [i for i in range(some_set[1], destination[1]*step + 1)]
        elif some_set[0] == destination[0]-1:
            y_set = [destination[1]*step]
        else:
            y_set = []
            print("Overfow in CurrentSets")
            exit(-100)

        return y_set

    def possible_moves(self, some_set, destination, step):
        curr_set = self.current_sets(some_set, destination, step)

        for j in curr_set:
            self.combinations.append([some_set[0]+1, j])


if __name__ == "__main__":
    feasible_number = int(input("Enter number of steps: "))
    profiler = cProfile.Profile()
    profiler.enable()
    B = Bellman([0, 0], [6, 4], {1: 4, 2: 2, 3: 1, 4: 6, 5: 5, 6: 1}, feasible_number)
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('tottime')
    stats.print_stats()
