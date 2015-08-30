Python Implementation of HopcroftKarp's Algorithm
=================================================

hopcroftkarp is a library based on Hopcroft Karp's Algorithm. It takes as input a bipartite graph and produces a maximum cardinality matching as output. Since a bipartite graph might have more than one maximum matchings. It is worth noting that the algorithm can output any of the maximum matching.

Pseudo code gotten from https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm
        

        
Example
~~~~~~~

.. image:: https://raw.githubusercontent.com/sofiat-olaosebikan/hopcroftkarp/master/image/bipartite_graph.png
  
.. code::

	>>> from hopcroftkarp import HopcroftKarp
	>>> graph = {'a': {1}, 'b': {1, 2}, 'c': {1, 2}, 'd': {2, 3, 4}, 'e': {3, 4}, 'f': {4, 5, 6},
         'g': {5, 6, 7}, 'h': {8}}
	>>> HopcroftKarp(graph).maximum_matching()
		{1: 'a', 2: 'b', 3: 'e', 4: 'd', 5: 'g', 6: 'f', 8: 'h', 'a': 1, 'd': 4, 'e': 3, 'h': 8, 'b': 2, 'f': 6, 'g': 5}
		
		
		
Installation
~~~~~~~~~~~~

Simply execute

.. code::

    easy_install hopcroftkarp


or from this source distribution, run

.. code::

    python setup.py install

