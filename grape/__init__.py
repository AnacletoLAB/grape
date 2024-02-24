"""GRAPE main module.

For now, this is a simple wrapper of GRAPE main two sub-modules that for
software engineering porposes are kept as two separate packages.

These packages are mimed here by the two sub-directories, ensmallen and embiggen.
"""

from embiggen import *
from ensmallen import *


def import_all(module_locals):
    """Execute dynamic loading of submodules."""
    import ensmallen as _ensmallen
    import embiggen as _embiggen
    import sys as _sys
    import pkgutil as _pkgutil

    for _module in (_ensmallen, _embiggen):
        for _loader, _module_name, _is_pkg in _pkgutil.iter_modules(_module.__path__):
            if not _is_pkg:
                continue
            if _module_name.startswith(("_", "~")):
                continue
            try:
                # The reason for the try-except block is that the `find_module` method
                # was removed from the `loader` object in Python version 3.12, and we
                # need to use the `find_spec` method instead. This is not true for older
                # versions of Python, so we need to use a try-except block to handle both
                # cases.
                _loaded_module = _loader.find_module(
                    _module_name
                ).load_module(_module_name)
            except AttributeError:
                # From Python version 3.12, the `find_module` method was removed.
                # We need to use the `find_spec` method instead, but this method
                # does not immediately return a loader, which is instead an attribute
                # of the returned spec object. We need to use the `loader` attribute
                # of the returned spec object to get the loader.
                _loaded_module = _loader.find_spec(
                    _module_name
                ).loader.load_module(_module_name)
            _sys.modules[f'grape.{_module_name}'] = _loaded_module
            module_locals[_module_name] = _loaded_module


def print_version():
    from grape.__version__ import __version__ as grape_version
    import os
    import platform
    from environments_utils import is_notebook
    import pandas as pd

    data = {
        "GRAPE Version": grape_version,
        "Python version": platform.python_version(),
        "Platform": platform.platform(),
        "Threads number": os.cpu_count(),
    }

    try:
        from karateclub.version import __version__ as karate_club_version
        data["KarateClub version"] = karate_club_version
    except Exception:
        pass

    try:
        from torch import __version__ as torch_version
        data["PyTorch version"] = torch_version
    except Exception:
        pass

    try:
        from tensorflow import __version__ as tf_version
        data["TensorFlow version"] = tf_version
    except Exception:
        pass

    try:
        from pykeen import get_version as get_pykeen_version
        data["PyKEEN version"] = get_pykeen_version()
    except Exception:
        pass

    if is_notebook():
        from IPython.display import display
        display(pd.DataFrame([
            {
                "Information": information,
                "Version": version
            }
            for information, version in data.items()
        ]).set_index("Information"))
    else:
        print(data)

import_all(locals())
del import_all

# Export all non-internals.
__all__ = [
    variable_name
    for variable_name in locals().keys()
    if not variable_name.startswith(("_", "~"))
]
