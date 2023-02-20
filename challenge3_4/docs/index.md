This is the documentation for challenge 3 and 4.

Challenge 1 and 2 are hosted on Colab Notebooks:
- [Challenge 1 Notebook](https://colab.research.google.com/drive/1yHl4ymnnhYKh9QwEorJ4ZNy-SYo6zCAu?usp=sharing)
- [Challenge 2 Notebook](https://colab.research.google.com/drive/1mjqtI-oCDJYSlU2jiTFXdaSPdlytIeDB?usp=sharing)

## Installation
Challenge 3 and 4 are packaged as xtream-diamonds, you only need python >= 3.8.

```bash
pip install xtream-diamonds
```

To check that everything works run

```bash
assignment-server --help
```
If you see ``command not found`` something is broken, proceed to troubleshooting.

### Troubleshooting
#### Pip Warning During Installation
Pip may yield some warnings during installation telling you that ``.local/bin`` does not belong to path.

To solve this issue add the following to .bashrc:
```bash
export PATH="$HOME/.local/bin:$PATH"
```
