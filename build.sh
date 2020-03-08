#!/usr/bin/env bash
cp -r ./app/static ./app/mod_home/
python run.py build;
cd ./app/build;
python -m http.server 80;