# Tomato

**Tomato** é uma ferramenta de linha de comando desenvolvida para automação de formatação e edição de texto no terminal, utilizando sequências de escape ANSI. Com o **Tomato**, você pode facilmente personalizar a cor, o estilo e o alinhamento do texto exibido no terminal. A ferramenta também permite extensibilidade, com suporte a plugins para adicionar novos estilos.

## Funcionalidades

- **Cor do Texto e Fundo**: Personalize a cor do texto e do fundo, escolhendo entre as cores padrão ANSI e suas variações brilhantes.
- **Estilos de Texto**: Aplique estilos como **negrito**, **sublinhado** e **negativo**. Plugins podem adicionar estilos adicionais.
- **Alinhamento**: Centralize, alinhe à direita ou à esquerda o texto no terminal.
- **Suporte a Plugins**: Extenda as funcionalidades do Tomato com plugins que adicionam novos estilos e recursos.

## Estrutura do Projeto

```plaintext
tomato/
│
├── core.py           # Lógica principal do Tomato
├── plugins/          # Diretório de plugins
│   ├── __init__.py   # Permite carregar plugins dinamicamente
│   ├── italics_style.py   # Exemplo de plugin que adiciona um estilo novo
│   └── blink_anim.py   # Outro plugin de funcionalidade
├── config.json       # Arquivo de configuração com a lista de plugins
└── main.py           # Arquivo principal que usa o Tomato para teste
```

## Descrição dos Arquivos

**core.py**: Contém a função format que aplica estilos, cores e alinhamento ao texto, além de funções auxiliares para validação e aplicação dos estilos.

**plugins/**: Diretório para plugins. Cada plugin adiciona novos estilos e funcionalidades. Plugins incluídos:

**italics_style.py**: Adiciona o estilo de itálico (italics).

**blink_anim.py**: Adiciona o estilo de piscar (blink).


**config.json**: Lista de plugins a serem carregados dinamicamente pelo Tomato.

**main.py**: Programa de teste que demonstra o uso do Tomato.


## Instalação

Clone o repositório e instale as dependências (não há dependências externas no momento):

```
git clone https://github.com/LuizRaizen/tomato.git
cd tomato
python setup.py install
```

## Exemplo de Uso

from core import format

print(format("Olá, mundo!", style="bold", color="yellow", markup="red", align="center"))

Esse exemplo imprime "Olá, mundo!" no terminal com negrito, cor do texto amarelo, fundo vermelho, e alinhamento centralizado.

## Exemplo com Plugins

Para utilizar plugins, configure o arquivo config.json para incluir os plugins desejados:

```
{
    "plugins": [
        "italics_style",
        "blink_anim"
    ]
}
```

Depois, carregue os plugins com a função load_plugins e utilize o novo estilo:

```
from core import format, load_plugins
```

## Carrega os plugins configurados

```
load_plugins('config.json')
print(format("Texto em itálico e piscando!", style="italics", color="cyan", markup="black", align="right"))
```

## Licença

Este projeto está licenciado sob a MIT License.

## Autor

Desenvolvido por **Luiz R.

