#!/bin/bash
#Parámetros
host=$1
firstPort=$2
lastPort=$3
function portscan

{
for((counter=$firstPort; counter<=$lastPort; counter++))
do
    (echo > /dev/tcp/$host/$counter) > /dev/null 2>&1 && echo "$counter open"
done
}

portscan
