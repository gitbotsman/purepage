# 方便设断点
try:
    import ipdb as pdb
except:
    import pdb
__builtins__["debug"] = pdb.set_trace
