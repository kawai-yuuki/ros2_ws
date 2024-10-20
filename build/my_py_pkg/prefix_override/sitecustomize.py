import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/yuukikawai-ubuntu22/ros2_ws/install/my_py_pkg'
