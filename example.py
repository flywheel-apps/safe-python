#!/usr/bin/env python

# Note:
# The above shebang, and setting the file's executable bit, allows the manifest's "command" key to be "./example.py".
# This is ideal as it removes any further bash processing of the gear command.

import json

invocation = json.loads(open('config.json').read())

# Note:
# The above load command robustly parses the /flywheel/v0/config.json file.
# This is ideal as it prevents any hand-parsing of the JSON syntax in bash or similar.

import copy

safe_invocation = copy.deepcopy(invocation)
safe_invocation["inputs"]["api-key"]["key"] = "--- OMITTED ---"

print("Gear invocation:")
print(json.dumps(safe_invocation, indent=4, sort_keys=True))
print()

# Note:
# The above demonstrates how to print the gear's invocation.
# Because there is an API key input provided to this gear, deep-copy is used blank the key out.
# This is ideal as it prevents another user from reading the gear logs and gaining (temporary) credentials.

if invocation["config"]["fast"]:
	print("I feel the need... the need, for speed!")
else:
	print("We are not going fast today.")
print()

# Note:
# The above conditional demonstrates checking a gear configuration setting.
# This is ideal because it allows robust, typed config options to be loaded from the JSON file.

import flywheel
import sys

fw = flywheel.Client(invocation["inputs"]["api-key"]["key"])

def interact_with_server():
	print("Interacting with the server...")
	user = fw.get_current_user()
	print('Your name in Flywheel is', user.firstname, user.lastname + '.')

try:
	interact_with_server()
except Exception as e:
	# Expected, runsc does not respect networking settings
	print("Could not interact with server, error was:")
	print(e,                                          )
print()

# Note:
# The above demonstrates how to best interact with remote services, such as the flywheel API.
# After creating a flywheel.Client object, it is best to define a function that performs your operation.
# When calling functions that interact with remote services, wrap them in a try/catch as shown.
# With this try/catch, a failure produces 2 lines of output. Without it, a failure produces 70 lines.
# This is ideal because it provides far more readable logs to the user.

import subprocess

def interact_with_system():
	print("Running some commands...")
	sys.stdout.flush()
	sys.stderr.flush()

	# Note:
	# Flushing print buffers is important before running any system command.
	# Otherwise, important log statements may not appear until after the command returns.
	# This is ideal because some gears can fork off commands that take hours or days to complete.

	subprocess.run(["uname", "-sr"], check=True)

	# Expected, runsc does not respect networking settings
	# subprocess.run(["curl", "-sI", "google.com"], check=True)

	result = subprocess.run(["wc", "-w", "example.py"], capture_output=True, check=True)

	word_count = result.stdout.decode("utf-8").split(' ')[0]
	print("There are", word_count, "words in example.py.")

try:
	interact_with_system()
except Exception as e:
	print("Could not interact with system, error was:", file=sys.stderr)
	print(e,                                            file=sys.stderr)
print()

# Note: The above demonstrates how to best run system commands.
# The subprocess.run is ideal for requiring an explicit command array.
# The "check" parameter is strongly recommended as it raises an exception on non-zero return codes.
# The "shell" paramter is not recommended; instead, use the subprocess module as documented here:
# https://docs.python.org/3/library/subprocess.html#replacing-older-functions-with-the-subprocess-module
# As before, a function is declared and wrapped in a try/catch.
# This is ideal because it minimizes opportunities to run unintended commands.

print("Complete!")

# Note:
# In either of the above try/catches, it may be desirable to add "exit(1)" to the "except Exception" stanzas.
# This depends on if you want the gear to fail or continue as success when a function fails.
# This is ideal because it allows you to tightly control if a gear is marked as red or green.
