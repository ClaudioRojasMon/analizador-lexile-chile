"""
Analizador de Nivel Lexile para Textos en Español
Sistema adaptado al contexto educativo chileno
"""

from .analizador_lexile import AnalizadorLexileChile
from .utilidades import (
    cargar_documento,
    analizar_pdf,
    comparar_textos,
    cargar_multiples_documentos,
    guardar_resultado
)

__version__ = '1.0.0'
__author__ = 'Claudio Rojas'

__all__ = [
    'AnalizadorLexileChile',
    'cargar_documento',
    'analizar_pdf',
    'comparar_textos',
    'cargar_multiples_documentos',
    'guardar_resultado'
]
