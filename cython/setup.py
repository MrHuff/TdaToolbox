from distutils.core import setup, Extension
from Cython.Build import cythonize

"""This file is part of the Gudhi Library. The Gudhi library
   (Geometric Understanding in Higher Dimensions) is a generic C++
   library for computational topology.

   Author(s):       Vincent Rouvreau

   Copyright (C) 2016  Inria

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "GUDHI Editorial Board"
__copyright__ = "Copyright (C) 2016  Inria"
__license__ = "GPL v3"

gudhi = Extension(
    "gudhi",
    sources = ['/homes/rhu/Documents/phd_projects/TdaToolbox/2018-09-04-14-25-00_GUDHI_2.3.0/build/cython/gudhi.pyx',],
    language = 'c++',
    extra_compile_args=['-DBOOST_RESULT_OF_USE_DECLTYPE', '-DBOOST_ALL_NO_LIB', '-DBOOST_SYSTEM_NO_DEPRECATED', '-std=c++11', '-frounding-math', ],
    extra_link_args=[],
    libraries=[],
    library_dirs=[],
    include_dirs = ['/usr/include', '/usr/include', '/usr/include', '/homes/rhu/Documents/phd_projects/TdaToolbox/2018-09-04-14-25-00_GUDHI_2.3.0/include', '/homes/rhu/Documents/phd_projects/TdaToolbox/2018-09-04-14-25-00_GUDHI_2.3.0/cython/include', ],
    runtime_library_dirs=[],
)

setup(
    name = 'gudhi',
    author='GUDHI Editorial Board',
    author_email='gudhi-contact@lists.gforge.inria.fr',
    version='2.3.0',
    url='http://gudhi.gforge.inria.fr/',
    ext_modules = cythonize(gudhi),
    install_requires = ["cython",],
)
