# Copyright (c) 2015, Sofiat Olaosebikan. All Rights Reserved

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from copy import deepcopy

class HopcroftKarp(object):
    def __init__(self, graph):
        """
        :param graph: an unweighted bipartite graph represented as a dictionary.
        Vertices in the left and right vertex set must have different labelling
        :return: a maximum matching of the given graph represented as a dictionary.
        """
        self._matching = {}
        self._dfs_paths = []
        self._dfs_parent = {}
        
        self._graph = deepcopy(graph)
        self._left = set(self._graph.keys())
        self._right = set()

        for value in self._graph.values():
            self._right.update(value)
        for vertex in self._left:
            for neighbour in self._graph[vertex]:
                if neighbour not in self._graph:
                    self._graph[neighbour] = set()
                    self._graph[neighbour].add(vertex)
                else:
                    self._graph[neighbour].add(vertex)

        

    def __bfs(self):
        layers = []
        layer = set()
        for vertex in self._left:  # for each free vertex in the left vertex set
            if vertex not in self._matching:  # confirms that the vertex is free
                layer.add(vertex)
        layers.append(layer)
        visited = set()  # to keep track of the visited vertices
        while True:
            # we take the most recent layer in the partitioning on every repeat
            layer = layers[-1]
            new_layer = set()  # new list for subsequent layers
            for vertex in layer:
                if vertex in self._left:  # if true, we traverse unmatched edges to vertices in right
                    visited.add(vertex)
                    for neighbour in self._graph[vertex]:
                        # check if the neighbour is not already visited
                        # check if vertex is matched or the edge between neighbour and vertex is not matched
                        if neighbour not in visited and (vertex not in self._matching or neighbour != self._matching[vertex]):
                            new_layer.add(neighbour)
                else:  # we traverse matched edges to vertices in left
                    visited.add(vertex)  # we don't want to traverse the vertex again
                    for neighbour in self._graph[vertex]:
                        # check if the neighbour is not already visited
                        # check if vertex is in the matching and if the edge between vertex and neighbour is matched
                        if neighbour not in visited and (vertex in self._matching and neighbour == self._matching[vertex]):
                            new_layer.add(neighbour)
            layers.append(new_layer)  # we add the new layer to the set of layers
            # if new_layer is empty, we have to break the BFS while loop....
            if len(new_layer) == 0:
                return layers   # break
            # else, we terminate search at the first layer k where one or more free vertices in V are reached
            if any(vertex in self._right and vertex not in self._matching for vertex in new_layer):
                return layers  # break
                # break

    # --------------------------------------------------------------------------------------------------------------
    # if we are able to collate these free vertices, we run DFS recursively on each of them
    # this algorithm finds a maximal set of vertex disjoint augmenting paths of length k (shortest path),
    # stores them in P and increments M...
    # --------------------------------------------------------------------------------------------------------------
    def __dfs(self, v, index, layers):
        """
        we recursively run dfs on each vertices in free_vertex,

        :param v: vertices in free_vertex
        :return: True if P is not empty (i.e., the maximal set of vertex-disjoint alternating path of length k)
        and false otherwise.
        """
        if index == 0:
            path = [v]
            while self._dfs_parent[v] != v:
                path.append(self._dfs_parent[v])
                v = self._dfs_parent[v]
            self._dfs_paths.append(path)
            return True
        for neighbour in self._graph[v]:  # check the neighbours of vertex
            if neighbour in layers[index - 1]:
                # if neighbour is in left, we are traversing unmatched edges..
                if neighbour in self._dfs_parent:
                    continue
                if (neighbour in self._left and (v not in self._matching or neighbour != self._matching[v])) or \
                        (neighbour in self._right and (v in self._matching and neighbour == self._matching[v])):
                    self._dfs_parent[neighbour] = v
                    if self.__dfs(neighbour, index-1, layers):
                        return True
        return False

    def maximum_matching(self, keys_only=False):
        while True:
            layers = self.__bfs()
            # we break out of the whole while loop if the most recent layer added to layers is empty
            # since if there are no vertices in the recent layer, then there is no way augmenting paths can be found
            if len(layers[-1]) == 0:
                break
            free_vertex = set([vertex for vertex in layers[-1] if vertex not in self._matching])

            # the maximal set of vertex-disjoint augmenting path and parent dictionary
            # has to be cleared each time the while loop runs
            # self._dfs_paths.clear() - .clear() and .copy() attribute works for python 3.3 and above
            del self._dfs_paths[:]
            self._dfs_parent.clear()

            for vertex in free_vertex:  # O(m) - every vertex considered once, each edge considered once
                # this creates a loop of the vertex to itself in the parent dictionary,
                self._dfs_parent[vertex] = vertex
                self.__dfs(vertex, len(layers)-1, layers)

            # if the set of paths is empty, nothing to add to the matching...break
            if len(self._dfs_paths) == 0:
                break

            # if not, we swap the matched and unmatched edges in the paths formed and add them to the existing matching.
            # the paths are augmenting implies the first and start vertices are free. Edges 1, 3, 5, .. are thus matched
            for path in self._dfs_paths:
                for i in range(len(path)):
                    if i % 2 == 0:
                        self._matching[path[i]] = path[i+1]
                        self._matching[path[i+1]] = path[i]
        if keys_only:
            self._matching = {k:v for k,v in self._matching.items() if k in self._left}
        return self._matching