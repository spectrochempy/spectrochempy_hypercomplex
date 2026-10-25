# Repository extraction provenance

This repository is a candidate for independent maintenance of the existing
`spectrochempy-hypercomplex` distribution. Package publication is not enabled;
the release authority remains with the SpectroChemPy maintainers until an
explicit handover decision.

## Source mapping

- Source repository: https://github.com/spectrochempy/spectrochempy
- Source commit: `9ef571ad75dec83a94af3db3c965ab82b3ed94e8`
- Source directory: `plugins/spectrochempy-hypercomplex`
- Extracted history tip: `4fe59b00a687d6ce0c1ea118003f19e48bc99635`
- Distribution: `spectrochempy-hypercomplex`
- Import package: `spectrochempy_hypercomplex`

History was extracted with `git subtree split --prefix=plugins/spectrochempy-hypercomplex`
at the source commit. Authors and relevant directory history are retained;
commit IDs change because paths and parent histories change.

The initial candidate setup adds only standalone packaging, documentation and
CI. Quaternion algorithms and public conventions remain those of the source
plugin.

## Validation scope

Candidate CI is intended to build wheel/sdist artifacts, verify installation
without editable source paths, and test core 1.1.0, core 1.1.3 and the current
development core. It also tests core-only, NMR-only, hypercomplex-only and
combined NMR/hypercomplex environments.

The candidate contains no PyPI, Conda publication, release, Trusted Publisher
or Zenodo workflow. Real-fixture rights, release ownership and documentation
handover remain separate decisions. Scientific 2D FFT validation is not part
of repository extraction.
