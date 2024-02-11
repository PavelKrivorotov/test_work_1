#!/bin/bash

set -e;
cd main;

echo "Starting Celery client:";
celery -A main worker -l INFO
