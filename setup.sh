#bin/bash

pkg update && pkg upgrade
pkg install python3
pip install colorama

echo 'Done'
