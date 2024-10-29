#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tomato é um módulo de automação de tarefas na linha de comando, especializado 
em formatação e edição de texto. Com o Tomato, você pode focar nos detalhes 
mais importantes do seu programa enquanto automatiza a formatação de saídas de 
texto no terminal utilizando sequências de escape ANSI.

Funcionalidades:
----------------
1. Alterar a cor do texto e o fundo:
    - Modifique facilmente a cor da saída do seu programa no terminal passando 
      o argumento `color` com o nome da cor desejada.
    - Alterar a cor de fundo passando o argumento `markup`.
    - Cores disponíveis (da tabela de cores ANSI):
        * black, red, green, yellow, blue, magenta, cyan, white
        * Versões brilhantes disponíveis adicionando o prefixo "bright_".

2. Aplicar estilos ao texto:
    - Utilize o argumento `style` para adicionar estilos como:
        * bold (negrito, código ANSI: 1)
        * underline (sublinhado, código ANSI: 4)
        * negative (inversão de cores de texto e fundo, código ANSI: 7)

3. Alinhamento do texto:
    - Use o argumento `align` para alinhar o texto no terminal:
        * center: Centraliza o texto.
        * right: Alinha o texto à direita.
        * left: Alinha o texto à esquerda.

Funcionalidade:
---------------
- A função principal `format(text, style=False, color=False, markup=False, align=False)` 
  formata a string de entrada de acordo com os argumentos fornecidos (estilo, cor, 
  fundo e alinhamento). Retorna o texto formatado utilizando códigos ANSI.
  
- Funções auxiliares:
    * `_set_style`: Mapeia o nome do estilo para o código ANSI correspondente.
    * `_set_color`: Mapeia o nome da cor para o código ANSI da cor do texto.
    * `_set_markup`: Mapeia o nome da cor para o código ANSI da cor de fundo.
    * `_set_align`: Alinha o texto com base nas dimensões do terminal.
  
Exemplo de uso:
---------------
>>> print(format("Olá, mundo!", style="bold", color="red", markup="green", align="center"))
Esse exemplo imprime "Olá, mundo!" em negrito com o texto vermelho e fundo verde, 
centralizado no terminal.

Metadados:
----------
Autor: Luiz R. Dererita
Versão: 0.0.3
Licença: MIT License
Status: Protótipo
"""

__author__ = "Luiz R. Dererita"
__credits__ = "Agradecimentos à comunidade de software livre."
__copyright__ = "Copyright (c) Desenvolvido por Luiz R. Dererita, 2021."
__version__ = "0.0.3"
__license__ = "MIT License"
__status__ = "Protótipo"
__maintainer__ = "Luiz R. Dererita"
__email__ = "luizdererita02@gmail.com"


import importlib
import json
import os
import re

# Diretório de plugins
PLUGIN_DIR = os.path.join(os.path.dirname(__file__), 'plugins')

plugins = {}

# Definindo constantes para os estilos e cores, para evitar erros de digitação
BOLD = "bold"
UNDERLINE = "underline"
NEGATIVE = "negative"
BLACK = "black"
RED = "red"
GREEN = "green"
YELLOW = "yellow"
BLUE = "blue"
MAGENTA = "magenta"
CYAN = "cyan"
WHITE = "white"
BRIGHT_BLACK = "bright_black"
BRIGHT_RED = "bright_red"
BRIGHT_YELLOW = "bright_yellow"
BRIGHT_BLUE = "bright_blue"
BRIGHT_MAGENTA = "bright_magenta"
BRIGHT_CYAN = "bright_cyan"
BRIGHT_WHITE = "bright_white"
CENTER = "center"
RIGHT = "right"
LEFT = "left"


def format(text: str, style: str=False, color: str=False, markup: str=False, align: str=False) -> str:
    """
    Formata o texto de entrada com base nos argumentos fornecidos: estilo, cor, 
    fundo (markup) e alinhamento. Retorna o texto formatado com códigos ANSI.

    Parâmetros:
    -----------
    text : str
        O texto a ser formatado.
    style : str, opcional
        O estilo do texto (ex.: 'bold', 'underline', 'negative'). O padrão é False.
    color : str, opcional
        A cor do texto (ex.: 'red', 'green'). O padrão é False.
    markup : str, opcional
        A cor de fundo (ex.: 'blue', 'bright_green'). O padrão é False.
    align : str, opcional
        O alinhamento do texto (ex.: 'center', 'right'). O padrão é False.

    Retorna:
    --------
    str
        O texto formatado com códigos ANSI.
    """
    # Verificando se o argumento 'text' é uma string
    if not isinstance(text, str):
        raise TypeError(f"Esperado 'text' ser uma string, mas recebeu {type(text).__name__}")
    
    # Aplicando estilo, cor e markup
    fmt = []
    if style:
    	fmt.append(_set_style(style))
    if color:
	    fmt.append(_set_color(color))
    if markup:
	    fmt.append(_set_markup(markup))
	    
    formatted_text = "\033[" + ";".join(filter(None, fmt)) + "m" + text + "\033[0m"
    
    # Aplicando alinhamento, se necessário
    return _set_align(formatted_text, align)


def _set_style(style):
    """
    Mapeia o nome do estilo fornecido para o código ANSI correspondente,
    incluindo os estilos fornecidos por plugins.
    """
    _TEXT_STYLES = {
        "bold": "1",
        "underline": "4",
        "negative": "7",
        False: False
    }

    # Integra estilos de plugins
    for plugin in plugins.values():
        if 'style' in plugin:
            _TEXT_STYLES.update(plugin['style'])

    if style and style not in _TEXT_STYLES:
        raise ValueError(f"Estilo inválido '{style}'. Estilos disponíveis: {list(_TEXT_STYLES.keys())}")
        
    return _TEXT_STYLES[style]
    
    
def _set_color(color):
    """
    Mapeia o nome da cor fornecida para o código ANSI correspondente.
    
    Parâmetros:
    -----------
    color : str
        A cor do texto (ex.: 'red', 'blue', 'bright_green').

    Retorna:
    --------
    str
        O código ANSI para a cor do texto.
    """
    _TEXT_COLORS = {
        'black':           "30",
        'red':             "31",
        'green':           "32",
        'yellow':          "33",
        'blue':            "34",
        'magenta':         "35",
        'cyan':            "36",
        'white':           "37",
        "bright_black":    "90",
        "bright_red":      "91",
        "bright_green":    "92",
        "bright_yellow":   "93",
        "bright_blue":     "94",
        "bright_magenta":  "95",
        "bright_cyan":     "96",
        "bright_white":    "97",
        False:             False
    }
    
    # Verifica se a cor fornecida é válida
    return _validate_color(color, _TEXT_COLORS, "color")
    
    
def _set_markup(color):
    """
    Mapeia o nome da cor de fundo fornecida para o código ANSI correspondente.
    
    Parâmetros:
    -----------
    color : str
        A cor de fundo (ex.: 'green', 'bright_blue').

    Retorna:
    --------
    str
        O código ANSI para a cor de fundo.
    """
    _MARKUP_COLORS = {
        "black":           "40",
        "red":             "41",
        "green":           "42",
        "yellow":          "43",
        "blue":            "44",
        "magenta":         "45",
        "cyan":            "46",
        "white":           "47",
        "bright_black":    "100",
        "bright_red":      "101",
        "bright_green":    "102",
        "bright_yellow":   "103",
        "bright_blue":     "104",
        "bright_magenta":  "105",
        "bright_cyan":     "106",
        "bright_white":    "107",
        False:             False
    }
    
    # Verifica se a cor de fundo fornecida é válida
    return _validate_color(color, _MARKUP_COLORS, "markup")


def _strip_ansi_sequences(text):
    """
    Remove temporariamente as sequências ANSI do texto para cálculos corretos de comprimento.
    
    Parâmetros:
    -----------
    text : str
        O texto que pode conter sequências ANSI.

    Retorna:
    --------
    str
        O texto sem as sequências ANSI.
    """
    ansi_escape = re.compile(r'(?:\x1B[@-_][0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)


def _set_align(text, align):
    """
    Alinha o texto com base no alinhamento fornecido e nas dimensões do terminal,
    ignorando sequências ANSI no cálculo do comprimento do texto.

    Parâmetros:
    -----------
    text : str
        O texto a ser alinhado.
    align : str
        O tipo de alinhamento (ex.: 'center', 'right', 'left').

    Retorna:
    --------
    str
        O texto alinhado de acordo com o tipo especificado ou o texto original 
        se nenhum alinhamento for fornecido.
    """
    # Se 'align' for False, apenas retorna o texto original
    if not align:
        return text

    # Obtém a largura do terminal
    width = os.get_terminal_size().columns
    
    # Remove espaços em branco
    text = text.strip()
    
    # Remove sequências ANSI para calcular o tamanho real do texto
    clean_text = _strip_ansi_sequences(text)
    text_length = len(clean_text)

    # Calcula o espaço necessário para o alinhamento
    if align == 'right':
        padding = width - text_length
        return ' ' * padding + text
    elif align == 'center':
        padding = (width - text_length) // 2
        return ' ' * padding + text
    elif align == 'left':
        return text.ljust(width)
    else:
        raise ValueError(f"Alinhamento inválido '{align}'. Alinhamentos disponíveis: ['right', 'center', 'left']")
        
    # Se o texto for maior que a largura do terminal, corta o texto
    return text[:width]  # Retorna o texto cortado, se necessário
    
    
def _validate_color(color: str, color_dict: dict, color_type: str) -> str:
    """
    Valida a cor fornecida com base na tabela de cores (color_dict) e o tipo de cor (color_type).
    
    Parâmetros:
    -----------
    color : str
        A cor fornecida pelo usuário que deve ser validada.
    color_dict : dict
        O dicionário contendo a tabela de cores disponíveis, onde as chaves são 
        os nomes das cores e os valores são os códigos ANSI correspondentes.
    color_type : str
        O tipo de cor a ser validado (ex.: 'texto' ou 'fundo'), usado para mensagens de erro mais específicas.

    Retorna:
    --------
    str
        O código ANSI correspondente à cor fornecida se for válida.

    Levanta:
    --------
    ValueError
        Se a cor fornecida não for encontrada no dicionário de cores.

    Exemplo:
    --------
    >>> _validate_color("red", _TEXT_COLORS, "texto")
    '31'

    >>> _validate_color("blue", _MARKUP_COLORS, "fundo")
    '44'

    >>> _validate_color("inexistente", _TEXT_COLORS, "texto")
    ValueError: Cor de texto inválida 'inexistente'. Cores disponíveis: ['black', 'red', 'green', ...]
    """
    # Verifica se a cor existe no dicionário fornecido
    if color and color not in color_dict:
        raise ValueError(f"Cor de {color_type} inválida '{color}'. Cores disponíveis: {list(color_dict.keys())}")
    
    # Retorna o código ANSI correspondente à cor
    return color_dict[color]
    

def load_plugins(config_file):
    """
    Carrega os plugins definidos no arquivo de configuração JSON e os registra no sistema.
    """
    # Carrega o arquivo de configuração
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    plugins = {}
    
    # Itera sobre os plugins listados na configuração
    for plugin_name in config['plugins']:
        try:
            # Importa o módulo do plugin
            module_name = f"plugins.{plugin_name}"
            module = importlib.import_module(module_name)
            
            # Verifica se o plugin tem a função 'register_plugin' para adicionar ao sistema
            if hasattr(module, 'register_plugin'):
                plugins[plugin_name] = module.register_plugin()
            else:
                print(f"O plugin {plugin_name} não possui uma função 'register_plugin'.")
        except ModuleNotFoundError:
            print(f"Plugin {plugin_name} não encontrado.")
    
    return plugins


# Exemplo de uso para carregar os plugins
plugins = load_plugins('config.json')
