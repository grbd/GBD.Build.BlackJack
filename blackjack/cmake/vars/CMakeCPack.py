﻿from .types.CMakeVariable import CMakeVariable
from .types.VariableCollection import VariableCollection

class CMakeCPack(VariableCollection):
    """CMake CPack related variables"""

    CPACK_ABSOLUTE_DESTINATION_FILES = ()
    CPACK_COMPONENT_INCLUDE_TOPLEVEL_DIRECTORY = ()
    CPACK_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION = ()
    CPACK_INCLUDE_TOPLEVEL_DIRECTORY = ()
    CPACK_INSTALL_SCRIPT = ()
    CPACK_PACKAGING_INSTALL_PREFIX = ()
    CPACK_SET_DESTDIR = ()
    CPACK_WARN_ON_ABSOLUTE_INSTALL_DESTINATION = ()
