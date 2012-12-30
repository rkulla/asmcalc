#!/bin/bash
# This script will run all the tests in the test/ directory.
# Usage: Make sure this file is in the root of the project,
#        cd to the root of the project and run as:
#        $ chmod u+x runtests.bash
#        $ ./runtests.bash

export PYTHONPATH=$PYTHONPATH:.
python test/test_*
