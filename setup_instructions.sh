#!/bin/bash

# Setup instructionsn

# create virtual environment
python3 -m venv .venv

# activate virtual environment
source ".venv/bin/activate"

# set python path
export PYTHONPATH=..

# upgrade pip installer
pip install --upgrade pip

# python project configuration (pyproject.toml)
pip install -e .


