#!/bin/bash
usuario=$1

for i in $(cut -d: -f1 /etc/passwd)
do
    if [[ $usuario == $i ]]
    then
        echo -e "El usuario existe!\n"
        echo -e "A continuación se muestran los usuarios disponibles:\n"
        for j in $(cut -d: -f1 /etc/passwd)
        do
            echo $j
        done
        break
    fi
done
