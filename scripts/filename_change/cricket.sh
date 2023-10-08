#!/bin/bash

# Prefixo a ser adicionado
prefixo="cricket_"

# Loop para renomear os arquivos
for arquivo in *.txt; do
    novo_nome="$prefixo$arquivo"
    mv "$arquivo" "$novo_nome"
done
