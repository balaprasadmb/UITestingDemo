#!/bin/bash

## run it as
# source set_python_path.sh
# OR
# . set_python_path.sh
##

export PYTHONPATH=$PYTHONPATH$( find $PWD -type d |xargs|tr ' ', ':'|awk '{print ":"$1}' )

