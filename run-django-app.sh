#!/bin/bash

set -e;
cd main;

echo -e "Run migrations:\n";
python manage.py migrate;

echo -e "\nRun app:\n"
python manage.py runserver $host:$port
