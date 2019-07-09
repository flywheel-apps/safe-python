# Safe Python

A quick demonstration of best-practice gear development using python 3 and the runsc module.

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

Could not interact with server, error was:
HTTPSConnectionPool(host='docker.local.flywheel.io', port=8443): Max retries exceeded with url: /api/users/self (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7fe12385ceb8>: Failed to establish a new connection: [Errno 111] Connection refused'))

Running some commands...
Linux 4.15.0-54-generic
There are 550 words in example.py.

Complete!
```
