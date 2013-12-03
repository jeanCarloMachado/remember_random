#! /bin/bash
varDate=$(date)
varMessageDef="commit automático jean - data: $varDate"
varDir=$(pwd)

echo "Efetuando pull, diretório atual: $varDir "
git pull origin master
echo "Efetuando o add . " 
git add . 
# pega a mensagem do commit do usuário
read -p "mensagem do commit default <$varMessageDef>" varMessage

if [[ ! $varMessage ]]; then
    varMessage=$varMessageDef
fi

git commit -m "$varMessage" -a
echo "fazendo o push"

#pega o branch do commit 
branch="master"
read -p "branch para comitar default: <$branch>" branch

git push origin $branch

