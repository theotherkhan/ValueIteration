#!/bin/bash 

if  pip3 show pandas  > /dev/null
then
    :
else
    echo "pandas installing..."
    pip3 install pandas > /dev/null
    echo "pandas installed"
fi

if  pip3 show numpy  > /dev/null
then
    :
else
    echo "numpy installing..."
    pip3 install numpy > /dev/null
    echo "numpy installed"
fi

if  pip3 show matplotlib  > /dev/null
then
    :
else
    echo "matplotlib installing..."
    python3 -mpip install matplotlib > /dev/null
    echo "matplotlib installed"
fi
python3 valueIteration.py