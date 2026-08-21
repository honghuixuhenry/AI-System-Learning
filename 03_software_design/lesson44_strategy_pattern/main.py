class Navigation:
    def plan(self, start, goal):
        pass

class AStarNavigation(Navigation):
    def plan(self, start, goal):
        return "A* Path"

class RRTNavigation(Navigation):
    def plan(self, start, goal):
        return "RRT Path"

class RLNavigation(Navigation):
    def plan(self, start, goal):
        return "RL Path"

class Planner:
    def __init__(self, navigation):
        self.navigation = navigation
    def run(self):
        return self.navigation.plan("A", "B")

planner = Planner(AStarNavigation())
print(planner.run())

class SortStrategy:
    def sort(self, array):
        pass
class BubbleSort(SortStrategy):
    def sort(self, array):
        return "BubbleSort Outcomes"
class QuickSort(SortStrategy):
    def sort(self, array):
        return "QuickSort Outcomes"
    
class Sorter:
    def __init__(self, sorter):
        self.sorter = sorter
    def run(self):
        return self.sorter.sort([1,2,3])
sorter = Sorter(BubbleSort())
print(sorter.run())