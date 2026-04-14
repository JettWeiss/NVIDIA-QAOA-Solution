# Necessary packages
# -*- coding: utf-8 -*-
import networkx as nx
from networkx import algorithms
from networkx.algorithms import community
import cudaq
from cudaq import spin
## To install cudaq-solvers (if not already installed), uncomment and run:
## !pip install cudaq-solvers -q
## Note: cudaq-solvers requires libgfortran. If you see an ImportError, run:
## !apt-get install -y libgfortran5
import cudaq_solvers as solvers
from cudaq.qis import *
import numpy as np
import matplotlib.pyplot as plt
from typing import List
import ipywidgets as widgets
from ipywidgets import interact



# install `qutip` and `ipywidgets` in the current Python kernel. Skip this if they are already installed.
# `matplotlib` is required for all visualization tasks.
# Make sure to restart your kernel if you execute this!
# In a Jupyter notebook, go to the menu bar > Kernel > Restart Kernel.
# In VSCode, click on the Restart button in the Jupyter toolbar.

# The '\' before the '>' operator is so that the shell does not misunderstand
# the '>' qualifier for the bash pipe operation.

import sys

try:
    import matplotlib.pyplot as plt
    import qutip
    import ipywidgets as widgets

except ImportError:
    print("Tools not found, installing. Please restart your kernel after this is done.")
    !{sys.executable} -m pip install qutip\>=5 matplotlib\>=3.5
    !{sys.executable} -m pip install ipywidgets
    print("\nNew libraries have been installed. Please restart your kernel!")