#!/bin/sh

if test -d replace
then
    :
else
    mkdir replace
fi

for tf in *.txt
do
    #echo $tf
    cp $tf replace/$tf
    cd replace
    sed "s/$1/$2/g" ../$tf > $tf
    cd ..
done
#sed "s/$1/$2/g" 
