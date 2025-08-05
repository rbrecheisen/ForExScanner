@echo off

setlocal

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

del poetry.lock

poetry config virtualenvs.create false --local

@REM poetry cache clear pypi --all
@REM poetry update
poetry install

endlocal