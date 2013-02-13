import os
import sys
import inspect

for subfolder in ["../../sdk", "../../sdk/gen-py"]:
  abs_path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0], subfolder)))
  sys.path.append(abs_path)

from mask import Mask
