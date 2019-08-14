# Safe Python (Runsc)

A quick demonstration of best-practice gear development using python 3 and runsc.<br/>
This module, when available, provides a security boundary beyond what is traditional for the containerization ecosystem.

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
Could not interact with server, error was:
HTTPSConnectionPool(host='<hostname>', port=8443): Max retries exceeded with url: /api/users/self (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7fcaa73a8e50>: Failed to establish a new connection: [Errno 111] Connection refused'))

Running some commands...
Linux 4.15.0-55-generic
There are 559 words in example.py.

Complete!
```

Note that the server interaction does not succeed, as networking is not currently supported with our runsc module.

## Other versions

There are multiple versions of this gear for different purposes - most of them experimental.<br/>
Check the [branches](https://github.com/flywheel-apps/safe-python/branches) page for a list.
