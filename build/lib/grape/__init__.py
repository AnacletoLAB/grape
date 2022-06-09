"""GraPE main module.

For now, this is a simple wrapper of GraPE main two sub-modules that for
software engineering porposes are kept as two separate packages.

These packages are mimed here by the two sub-directories, ensmallen and embiggen.
"""
import embiggen as _embiggen
import ensmallen as _ensmallen
from embiggen import *
from ensmallen import Graph
import sys as _sys
import pkgutil as _pkgutil

for _module in (_embiggen, _ensmallen):
    for _loader, _module_name, _is_pkg in _pkgutil.iter_modules(_module.__path__):
        if not _is_pkg:
            continue
        _sys.modules[f'grape.{_module_name}'] = _loader.find_module(
            _module_name
        ).load_module(_module_name)

# Export all non-internals.
__all__ = [
    variable_name
    for variable_name in locals().keys()
    if not variable_name.startswith("_")
]