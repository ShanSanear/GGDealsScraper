#!/bin/bash

export PYTHONPATH=$(eval pwd):$PYTHONPATH
~/.local/bin/poetry install
~/.local/bin/poetry run python app/main.py