#!/bin/bash

# Prefixo a ser adicionado
prefixo="tennis_"

# Loop para renomear os arquivos
for arquivo in *.txt; do
    novo_nome="$prefixo$arquivo"
    mv "$arquivo" "$novo_nome"
done
