import os, epics
from epicscorelibs.path import get_lib

# Works regardless of whether the below line is commented out
os.environ["PYEPICS_LIBCA"] = get_lib('ca')  

val = epics.caget("test:pv1", timeout=5.0)
if val:
    print(f"Successful, test:pv1 is {val}")
    print(epics.ca.find_libca())