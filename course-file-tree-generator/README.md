# course-file-tree-generator

Quando eu acesso um curso em arquivos/pastas gosto de criar arquivos markdown para cada pasta/modulo do curso, além de criar um README.md geral contemdpo a duraçâo dos módulos e de cada vídeo, como tambem saber os calculos de horas totais de todos os vídeios e de cada módulo/pasta.

Isso permite eu me organizar melhor e saber o quanto falta para acabr.

Acontece que fazer tudo isso manual é chato demais. É um serviço mecanico e chato de olhar arquivos e tudoo mais.

Alémd e que, dá um 'tree -f/' seja no ubuntu/windows resgata na ordem errada se o nueral nâo tiver 2 digitos,, alem de pegar arquivos que nâo são vídeos

## Objetivo

+ Varre uma pasta e subspast e registrar tempos dos vídeos, nome dos arquivos (filtra somente video) além de gerar para cada pasta, um markdown tipo

# modulo-02-,......md

e dentro estiver já separa o títlo com '#' e subtitulos com "##' além da duraçâo.