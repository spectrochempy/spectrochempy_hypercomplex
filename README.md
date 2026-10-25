# spectrochempy-hypercomplex

Hypercomplex / quaternion support plugin for SpectroChemPy.

Provides quaternion-based dataset operations, quaternion-aware processing
handlers, and utilities that can be reused by NMR and other SpectroChemPy
plugins. The plugin does not depend on the NMR plugin.

## Installation

```bash
python -m pip install spectrochempy-hypercomplex
```

For NMR workflows:

```bash
python -m pip install "spectrochempy[nmr]" spectrochempy-hypercomplex
```

## Usage

```python
import spectrochempy as scp

# Hypercomplex support is independent of the NMR plugin.
dataset = scp.NDDataset([1.0, 2.0, 3.0, 4.0])
dataset.hyper.set_quaternion(inplace=True)
```

The public quaternion components are available as
`dataset.hyper.RR`, `dataset.hyper.RI`, `dataset.hyper.IR` and
`dataset.hyper.II`. The conversion utilities are exported from
`spectrochempy_hypercomplex`.

For NMR data, install `spectrochempy-nmr` as shown above and use its public
reader before applying the hypercomplex representation.

## Development

```bash
python -m pip install -e .
python -m pip install pytest pytest-doctestplus
python -m pytest tests/ -v
```
