#!/bin/bash

export PYTHONPATH=.

python3 integration_tests/"$1".py
