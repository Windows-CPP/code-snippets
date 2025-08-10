# multithreading
"""
For when several threads are neccessary to rapidly process data.
Design to be adaptable (with vars) to different data processing tasks- Either automate based on data
type, size, etc. OR allow user to specify processing parameters.
"""


# ---------------------------------------- #
# HARDWARE ACCELERATION
"""
A series of snippets relating to the anbling of hardware acceleration for datatype-specific processing.
This includes specific snippets for the activation / optimization of data processing using hardware acceleration for
1) OpenCV for computer vision (OpenCV),
2) NumPy & SciPy mathematical functions, 
3) PyTorch & TensorFlow machine learning operations, 
4) a direct interface for generic GPU hardware units (For non-CUDA hardware) (OpenCL), 
5) and an extra snippet for GPUs with CUDA support (CUDA-Python & VPF)
"""

# OPENCV HARDWARE ACCELERATION -{ OPENCV
## look into this- occasionally may require custom builds of OpenCV to enable hardware acceleration

# NUMPY / SCIPY HARDWARE ACCELERATION -{ CUPY 


# PYTORCH HARDWARE ACCELERATION


# TENSORFLOW HARDWARE ACCELERATION


# OPENCL HOMOGENEOUS ACCELERATED COMPUTING


# CUDA-BASED HARDWARE ACCELERATION