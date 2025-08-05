#!/bin/bash

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

rm poetry.lock

poetry config virtualenvs.create false --local

poetry cache clear pypi --all
poetry update
poetry install