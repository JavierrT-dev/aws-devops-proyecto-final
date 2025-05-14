#!/bin/bash
echo "Actualizando paquetes..."
sudo yum update -y

echo "Instalando git, vim, python3 y Docker..."
sudo yum install -y git vim python3 docker

echo "Iniciando Docker..."
sudo service docker start

echo "Agregando usuario actual al grupo docker..."
sudo usermod -aG docker cloudshell-user

echo "Listo. Entorno configurado."
