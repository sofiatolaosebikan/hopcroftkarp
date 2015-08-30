from setuptools import setup, find_packages

setup(name='hopcroftkarp',
      version='1.2.3',
      description='Implementation of HopcroftKarp\'s algorithm',
      long_description='{0:s}'.format(open('README.rst').read()),
      author='Sofiat Olaosebikan',
      author_email='sofiat@aims.edu.gh',
      url='https://github.com/sofiat-olaosebikan/hopcroftkarp',
      license = 'GPL',
      keywords = 'hopcroftkarp algorithm, maximum cardinality matching, bipartite graphs',
      packages=find_packages(),
      zip_safe=True,
      package_dir={'hopcroftkarp': 'hopcroftkarp'},
	  test_suite='test',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          ],
      )
      
