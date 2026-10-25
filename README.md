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

dataset = scp.read_topspin("path/to/2rr")
dataset.hyper.set_quaternion(inplace=True)
```

The public quaternion components are available as
`dataset.hyper.RR`, `dataset.hyper.RI`, `dataset.hyper.IR` and
`dataset.hyper.II`. The conversion utilities are exported from
`spectrochempy_hypercomplex`.

## Development

```bash
python -m pip install -e .
python -m pip install pytest pytest-doctestplus
python -m pytest tests/ -v
```
