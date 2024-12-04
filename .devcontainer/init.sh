#!/bin/bash

set -xe

git config --global --add safe.directory /workspace

pip install -r requirements.txt