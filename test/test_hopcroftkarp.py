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


import unittest
from HopcroftKarp import HopcroftKarp

class Tester(unittest.TestCase):
    def test_mainExample(self):
        graph = {'a': {1, 3}, 'c': {1, 3}, 'd': {3, 6}, 'h': {8}}
        hk = HopcroftKarp(graph)
        max_matching = hk.maximum_matching()
        self.assertTrue(max_matching == {1: 'a', 'a': 1, 3: 'c', 'c': 3, 6: 'd', 'd': 6, 8: 'h', 'h': 8} or
                        max_matching == {3: 'a', 'a': 3, 1: 'c', 'c': 1, 6: 'd', 'd': 6, 8: 'h', 'h': 8}, 
                        'maximum matching is incorrect')

    def test_keys_only(self):
        graph = {'a': {1, 3}, 'c': {1, 3}, 'd': {3, 6}, 'h': {8}}
        hk = HopcroftKarp(graph)
        max_matching = hk.maximum_matching(keys_only=True)
        self.assertTrue(max_matching == {'a': 1, 'c': 3, 'd': 6, 'h': 8} or
                        max_matching == {'a': 3, 'c': 1, 'd': 6, 'h': 8}, 
                        'maximum matching is incorrect')
