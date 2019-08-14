# Safe Python

A quick demonstration of best-practice gear development using python 3.


## Building

```
$ fw gear modify

apt update && apt install -y curl && pip install -U flywheel-sdk
```

## Example run

```
$ fw gear local --fast

Gear invocation:
{
    "config": {
        "fast": true
    },
    "destination": {
        "id": "aex",
        "type": "acquisition"
    },
    "inputs": {
        "api-key": {
            "base": "api-key",
            "key": "--- OMITTED ---"
        }
    }
}

I feel the need... the need, for speed!

Interacting with the server...
Your name in Flywheel is Nathaniel Kofalt.

Running some commands...
Linux 4.15.0-55-generic
There are 559 words in example.py.

Complete!
```

## Other versions

There are multiple versions of this gear for different purposes - most of them experimental.<br/>
Check the [branches](https://github.com/flywheel-apps/safe-python/branches) page for a list.
