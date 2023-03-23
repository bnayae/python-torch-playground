# PyTorch

- [Credits](https://www.youtube.com/watch?v=pcX4a5xZsIQ&t=97s)

## SETUP

### PYENV

- [How to Install and Run Multiple Python Versions on Windows 10/11](https://www.youtube.com/watch?v=HTx18uyyHw8)
- [GitHub: PyEnv](https://github.com/pyenv-win/pyenv-win)
- [Blog](https://k0nze.dev/posts/install-pyenv-venv-vscode/)
- [VS Code](https://code.visualstudio.com/docs/python/environments)
  - Command Palette (Ctrl+Shift+P) `Python: Create Environment`

- Command line

```python
# Create a virtual environment in the terminal
python -m venv .venv
pyenv install -l
pyenv install 3.10.9
pyenv install 3.9.9
pyenv install 3.11.2
pyenv versions
pyenv shell 3.9.9
python -V
pyenv local 3.9.9
```

### Setup Local python folder

```python
pyenv install -l
```

# Tutorials

- [Requirements File](https://learnpython.com/blog/python-requirements-file/)

  ```python
  pip freeze > requirements.txt
  pip install -r requirements.txt
  # ---
  # Scan imports
  pip install pipreqs
  # ---
  # Outdated
  pip list --outdated
  pip install -U fastapi
  # ---
  # Check for missing dependency
  python -m pip check
  ```

## Media

- Sound Effect from
  - [Pixabay](https://pixabay.com/sound-effects/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=6064)
