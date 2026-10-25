"""Smoke checks for the optional NMR/hypercomplex integration surface."""

from __future__ import annotations

import importlib.metadata as metadata
import inspect

import pytest

pytest.importorskip(
    "spectrochempy_nmr",
    reason="requires the optional spectrochempy-nmr distribution",
)


def test_nmr_and_hypercomplex_entry_points_are_discoverable():
    """Both official distributions expose their plugin entry points."""
    entry_points = {
        entry_point.name: entry_point.value
        for entry_point in metadata.entry_points(group="spectrochempy.plugins")
    }

    assert entry_points["nmr"] == "spectrochempy_nmr:NMRPlugin"
    assert entry_points["hypercomplex"] == (
        "spectrochempy_hypercomplex:HyperComplexPlugin"
    )


def test_nmr_uses_hypercomplex_public_helpers():
    """NMR reaches the public hypercomplex representation layer."""
    from spectrochempy_nmr.processing import hypercomplex

    source = inspect.getsource(hypercomplex)

    assert "from spectrochempy_hypercomplex import" in source
    assert "spectrochempy_hypercomplex._quaternion" not in source
