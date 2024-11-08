from __future__ import annotations

import importlib.metadata

import snakemake_invoke as m


def test_version():
    assert importlib.metadata.version("snakemake_invoke") == m.__version__
