# https://code.visualstudio.com/docs/python/python-tutorial
# https://wiki.python.org/moin/BeginnersGuide/Programmers
# https://python.land/python-tutorial
# PyTorch: https://www.youtube.com/watch?v=pcX4a5xZsIQ&t=97s


# Setup command
# python -m venv .venv

import sys

import torch

msg = "hello python"
print(msg)
print(f"Hi, Python version = {sys.version}")
print(f"Random = {torch.rand(1).item()}")
