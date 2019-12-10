#!/usr/bin/env bash

rsync -avzi export_pads.py config.py.example README.md requirements.txt nodejs@k_nodejs:daily_pad_backup/script/
