# Safe Python (Singularity)

A quick demonstration of best-practice gear development using python 3 and singularity.<br/>
When available, singularity provides a gear environment that is amenable to HPC deployments.


## Building

The gear builder does not support creating singularity images, instead we will be using the singularity build tool:

```
# Latest singularity format
sudo singularity build safe-python-singularity.sif safe-python-singularity.def

# Compatibility format for singularity versions before 3.0
sudo singularity build safe-python-singularity.simg safe-python-singularity.def
```

When building your own singularity gears, please take note of the sections below.

## Feature quirks

The following **gear manifest** features are NOT supported:

* Setting environment variables.

These should instead be set in your [definition file](https://sylabs.io/guides/3.3/user-guide/definition_files.html).<br/>
This gear's `safe-python-singularity.def` file is an example you can copy from.

By the same token, the following **singularity** features are NOT supported:

* Setting a working directory.
* Setting a run command.

These should instead be set in your [gear manifest](https://github.com/flywheel-io/gears/tree/master/spec#the-manifest).<br/>
This project's `manifest.json` file is an example you can copy from.

## Mount difficulties

Missing files? Singularity will silently discard configuration it does not like.<br/>
When ran with `--debug`, the issue becomes clearer:

```
Skipping mount, /usr/local/var/singularity/mnt/session/rootfs/flywheel/v0/config.json doesn't exist in container
Skipping mount, /usr/local/var/singularity/mnt/session/rootfs/flywheel/v0/output doesn't exist in container
```

To combat this, paths MUST exist as part of your image build step.
As per our gear spec:

* The [config file](https://github.com/flywheel-io/gears/tree/master/spec#the-input-configuration) exists at `/flywheel/v0/config.json`.
* The [output folder](https://github.com/flywheel-io/gears/tree/master/spec#the-output-folder) exists at `/flywheel/v0/output/`.
* Any [input folders](https://github.com/flywheel-io/gears/tree/master/spec#the-input-folder) exist relative to your input's name, eg `/flywheel/v0/input/dicom`.

This gear's `safe-python-singularity.def` file has commands in the `%post` step you can copy from.

## Troubleshooting

### Old singularity incompatibility after build

Even when using the older `.simg` format, you may need to produce those images with an old singularity version.<br/>
This gear built with singularity 3.3 and ran with 2.6 yielded an error:

```
Unknown image format/type: safe-python-1-singularity-3.3.simg
```

This may be related to [this singularity bug report](https://github.com/sylabs/singularity/issues/1192). The resolution was to build the gear with the older singularity version.

### Old singularity definition file change

On an older singularity, you may run into an error like this while building:

```
singularity /bin/cp: cannot create regular file '/usr/local/var/singularity/mnt/container//flywheel/v0/readme.md': No such file or directory
```

This is because the `$files` section does not create folders for you when copying files.<br/>
This gear has a `%setup` section to take care of that.

### Old singularity build error

You may run into this error:

```
singularity image-build: relocation error: /lib/x86_64-linux-gnu/libnss_files.so.2: symbol __libc_readline_unlocked version GLIBC_PRIVATE not defined in file libc.so.6 with link time reference
```

The closest I could find to discussion on this topic was [this singularity bug report](https://github.com/sylabs/singularity/issues/3917), which seems to indicate that this is an incompatibility with the host image you are trying to build on. I personally resolved this issue by switching to `ubuntu:18.04` and installing what I needed from scratch.

I have reported this problem [here](https://github.com/sylabs/singularity/issues/4203) and will update if I get a resolution.

## Example run

```
Gear invocation:
{
    "config": {
        "fast": true
    },
    "destination": {
        "id": "5d5471c0f661c40046b84194",
        "type": "session"
    },
    "inputs": {
        "api-key": {
            "base": "api-key",
            "key": "--- OMITTED ---"
        }
    }
}

We are not going fast today.

Interacting with the server...
Your name in Flywheel is Nathaniel Kofalt.

Running some commands...
Linux 4.15.0-55-generic
```

## Other versions

There are multiple versions of this gear for different purposes - most of them experimental.<br/>
Check the [branches](https://github.com/flywheel-apps/safe-python/branches) page for a list.
