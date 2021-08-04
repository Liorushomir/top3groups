"""
1. calculate distance between two names
2. decide maximal distance to consider two names as the same
3. maybe get a list of words that aren't helping identification such as "inc, estates, etc."
"""

import unionfind
import numpy as np
import math

class LevinsteinDistance:

    def __init__(self):
        self.str1 = ""
        self.str2 = ""
        self.matrix = None
        self.curr_row = []
        self.next_row = []



    def __call__(self, str1, str2):
        self.str1 = "#" + self.clean_string(str1.lower())
        self.str2 = "#" + self.clean_string(str2.lower())

        """"self.curr_row = [i for i in range(len(self.str1))]
        self.next_row = [0] * len(self.str1)"""
        return self.levinstein_dist()

    def switch_curr_next(self):
        temp = self.curr_row
        self.curr_row = self.next_row
        self.next_row = temp

    def clean_string(self, str):
        #return str
        str = str.replace(',', '')
        str = str.replace('.', '')
        str = str.replace(';', '')
        str = str.replace(' ', '')
        str = str.replace('\\', '')
        str = str.replace('-', '')
        str = str.replace('_', '')
        str = str.replace('*', '')
        str = str.replace('#', '')
        str = str.replace('/', '')
        str = str.replace('>', '')
        str = str.replace('<', '')
        return str


    def levinstein_dist(self):
        cols = len(self.str1)
        rows = len(self.str2)
        self.matrix = [([0]*cols) for i in range(rows)]

        for i in range(0, cols):
            self.matrix[0][i] = i

        for i in range(0, rows):
            self.matrix[i][0] = i

        for i in range(1, rows):
            for j in range(1, cols):
                if self.str1[j] == self.str2[i]:
                    self.matrix[i][j] = self.matrix[i - 1][j - 1]
                else:
                    self.matrix[i][j] = 1 + min(self.matrix[i][j - 1], self.matrix[i - 1][j])
        #print(self.str1 + " and " + self.str2 + "and the distance is: " + str(self.matrix[-1][-1]))
        return self.matrix[-1][-1]

def get_names():
    if simple_test:
        file = open("15names.txt", "r")
    else:
        file = open("1000names.txt", "r")
    names = file.readlines()
    file.close()
    return names


def get_groups(names, dist_param):
    name_groups = unionfind.UnionFind(names)
    # dict = {}
    change = True
    lev_dist = LevinsteinDistance()
    while change:
        change = False
        for key_name in names:
            if len(key_name) <= 10:
                continue

            for name in names:
                if len(name) <= 10:
                     continue
                if not name_groups.connected(key_name, name):
                    if abs(len(key_name) - len(name)) > 1.5 * min(len(key_name),len(name)):
                        continue
                    else:
                        dist = lev_dist(key_name, name)

                    if dist <= min(dist_param, round(min(len(key_name), len(name)) / 3)):
                        name_groups.union(key_name, name)
                        change = True

    return name_groups.components()


def get_top_groups(n, names, dist_param):
    groups_by_dist = get_groups(names, dist_param)
    #print(groups_by_dist)
    groups_by_dist.sort(key=len, reverse=True)
    top_groups = [groups_by_dist[i] for i in range(min(n, len(groups_by_dist)))]
    #print(top_groups)

    return top_groups


simple_test = False

if __name__ == "__main__":
    #group_names_file = open("group_names_file.txt", "w")
    dist_param = 10
    names = get_names()
    groups = get_top_groups(3, names, dist_param)
    # group_names_file.
    for i, group in enumerate(groups):
        print("\ngroup " + str(i) + "\n")
        for name in group:
           print(name)

