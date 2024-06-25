#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `GParted` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `GParted` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and configurations for configuring/installing/use the `GParted` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# O `GParted` é uma aplicação de software de código aberto que fornece uma interface gráfica amigável para gerenciamento de partições de disco em sistemas Linux e outras plataformas. Com o `GParted`, os usuários podem criar, redimensionar, mover e excluir partições em unidades de disco rígido de maneira segura e eficiente. Ele oferece recursos como formatação de partições, verificação e reparo de sistemas de arquivos, bem como suporte para uma variedade de sistemas de arquivos, tornando-o uma ferramenta valiosa para administradores de sistemas e usuários que precisam gerenciar o armazenamento de seus sistemas de forma flexível e intuitiva.

# ### 1.3 Passo a passo [1]
# 
# ### 1.3.1 Atualizar o Sistema Operacional (SO)
# 
# ### 1.1 Atualizar o Sistema Operacional (SO)
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes APT. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo APT e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.5 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.6 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.7 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.8 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# #### 1.3.2 Instalação do `GPaterd` no `Linux Ubuntu`
# 
# 3. **Instale e utilize o `gparted`**: O `gparted` é uma ferramenta gráfica para gerenciamento de partições. Instale-o com: `sudo apt install gparted -y`

# ## Referências
# 
# [1] OPEN AI. ***Erro na inicialização.*** Disponível em: <https://chat.openai.com/c/86a92f6e-fb13-4be6-9b46-9ed1e8b44c9f> (texto adaptado). Acessado em: 17/10/2023 16:44.
# 
# [2] OPENAI. ***VS code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 14/11/2023 09:33.
# 
