# Challenge 3
## Training a Model
This module exposes ``assignment-train``.

This command allows you to train an instance of a XGBoost regression model given a dataset. This command takes only one positional argument which is the path to the dataset:
```bash
assignment-train ./diamonds.csv
```
After running this command the model will be saved as ``model.json`` and will be ready to be used by challenge 4. This command also returns the accuracy the model achieves by splitting the dataset in training (80%) and test (20%) randomly.
## API Documentation
See [challenge 3 API docs](./xtream_diamonds.challenge3.rst) to get a sense of the implementation.
