"""GraPE main module.

For now, this is a simple wrapper of GraPE main two sub-modules that for
software engineering porposes are kept as two separate packages.

These packages are mimed here by the two sub-directories, ensmallen and embiggen.
"""
import embiggen
import ensmallen

__all__ = [
    "embiggen",
    "ensmallen"
]
