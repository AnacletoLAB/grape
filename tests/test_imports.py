"""Test to verify whether the imports work."""

def test_import_from_submodules():
    from grape import Graph
    from grape.embedders import SPINE
    from grape.datasets.string import HomoSapiens