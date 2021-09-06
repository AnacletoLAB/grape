"""GraPE main module.

For now, this is a simple wrapper of GraPE main two sub-modules that for
software engineering porposes are kept as two separate packages.
"""
import ensmallen
import embiggen

__all__ = [
    "ensmallen",
    "embiggen"
]