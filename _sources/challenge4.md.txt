# Challenge 4
This module exposes two commands `assignment-server` and `assignment-price`.

## Server
`assignment-server` allows to start a server at a given address with a given model.

If you don't have a `model.json` file available go to challenge 3 and run `assignment-train` on a dataset. After generating a `model.json` you can start the server:
```bash
assignment-server --model ./model.json --address 127.0.0.1:8000
```
Please replace `./model.json` with the correct path to your model file.

## Pricing a Diamond
`assignment-price` allows to make a post request to a given server to ask the price of a given diamond.

First you need to specify a diamond as a .json file:
```json
{
    "carat": 1.1,
    "cut": "Ideal",
    "color": "H",
    "clarity": "SI2",
    "depth": 62.0,
    "table": 55.0,
    "x": 6.61,
    "y": 6.65,
    "z": 4.11
}
```

After specifying the diamond you save it (e.g. diamond.json) and send it to the server for pricing:
```bash
assignment-price --diamond ./diamond.json --address 127.0.0.1:8000
```
Path and address may be any.

## API Documentation
See [challenge 4 API docs](./xtream_diamonds.challenge4.rst) to get a sense of the implementation.

