# Copyright 2019 Pascal Audet
#
# This file is part of PlateCurie.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""

Configuration module to set up global variables

Variables are:

.. rubric:: Wavelet parameters

``k0``: float
    Internal Morlet wavenumber (5.336 or higher)
``p`` : float 
    Separation between adjacent wavenumbers (0.85)

.. rubric:: Bayes inference

``samples`` : int 
    Number of samples in single MCMC chain
``tunes`` : int
    Number of tuning samples
``cores`` : int
    Number of cores (i.e., parallel chains). For parallel runs, set conf.cores=1

"""

# wavelet parameters
global k0, p
k0 = 5.336
p = 0.85

# bayes parameters
global samples, tunes
samples = 200
tunes = 200
cores = 4