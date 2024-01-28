# FLAME Standalone
Reimplementing the FLAME regressor. Code borrowed from [MICA's Flame implementation](https://github.com/Zielon/MICA/tree/8de9025ee155f208f4a4aed61ade303237f9b1db/models) and modified to work with the least dependencies possible.

## Installation
```bash
conda create -n flame python=3.10
pip install -r requirements.txt
```

## Usage
Activate the conda environment
```bash
conda activate flame
```
Run the script
```bash
python flame.py
```

## TODO
- [ ] Remove dependency chumpy
- [ ] Make it work with the latest version of Python