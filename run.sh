#!/bin/bash 

if  pip3 show pandas  > /dev/null
then
    :
else
    echo "pandas installing..."
    pip3 install pandas > /dev/null
    echo "pandas installed"
fi
python3 valueIteration.py