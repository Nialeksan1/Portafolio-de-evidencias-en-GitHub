#!/bin/bash

# Se declaran variables globales con codigos de escape ANSI para el color
GREEN='\033[0;32m'
NC='\033[0m'

function spin()
{
    printf "\b${sp:sc++:1}"
    ((sc==${#sp})) && sc=0
}

function endspin()
{
    printf "\r%s\n" "$@"
}

# Función para hacer ping y verificar puertos 22-80
function ping_ipurl()
{
    echo -e "\n"
    # Se le da un segundo de ejecución para hacer ping a la ip/url
    # Todo resultado se envía a /dev/null
    timeout 1 ping -c 1 $1 > /dev/null

    # Si lo anterior resultó exitoso, realizará el escaneo
    if [[ $? == 0 ]]; then
        echo "Node with ip or url $i is up"
        for(( j=22;j<=80;j++ ))
        do
            # Un segundo para hacer la conexion a la ip/url con puerto $j
            # Si hay conexión, imprime en verde y con tab, sino, imprime closed
            timeout 1 bash -c "echo 2>/dev/null >/dev/tcp/$1/$j" &&
            echo -e "-> \t ${GREEN}port $j is open${NC}" ||
            echo -e "port $j is closed"
        done
    else
        # Imprimirá que está caido o no se reconoce y saldrá de la función
        echo "Node with ip or url $i is down or unknown"
        return
    fi
}

function OS()
{
    # Mediante condicionales anidadas verifica el tipo de comando para el SO
    if [ type -t wevtutil &> /dev/null ]; then
        OS=MSwin
    elif [ type -t scutil &> /dev/null ]; then
        OS=macOS
    else
        OS=Linux
    fi
    echo -e "\n El sistema operativo es $OS"
}

function main()
{
    # En laboratorio4.txt la fecha y el SO utilizado
    date
    OS

    # Le el contenido recibido como arreglo
    readarray ips

    # Por cada elemento en el arreglo, se ejecuta la función ping_ipurl
    # EL resultado se ingresa al archivo
    for i in "${ips[@]}"
    do
        ping_ipurl $i
    done 2>/dev/null
}

echo "Esto tardará unos minutos, pero descuida, toda la información esta siendo copiada a laboratorio4.txt"
main >> laboratorio4.txt
# Al terminar imprimer en $1 un mensaje de finalización
echo Finish
