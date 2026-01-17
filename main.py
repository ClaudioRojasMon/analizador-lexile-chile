"""
Script principal para análisis de nivel Lexile
Herramienta de línea de comandos para analizar textos en español
"""

import sys
import os
import argparse

# Agregar src al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from analizador_lexile import AnalizadorLexileChile
from utilidades import cargar_documento, analizar_pdf, comparar_textos, guardar_resultado


def main():
    """Función principal del programa."""
    
    parser = argparse.ArgumentParser(
        description='Analizador de Nivel Lexile para textos en español',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  # Analizar un archivo de texto
  python main.py --file mi_texto.txt
  
  # Analizar un PDF
  python main.py --file documento.pdf
  
  # Comparar múltiples textos
  python main.py --comparar texto1.txt texto2.pdf texto3.txt
  
  # Guardar resultado en archivo
  python main.py --file texto.txt --output resultado.txt
        """
    )
    
    parser.add_argument(
        '--file',
        '-f',
        type=str,
        help='Archivo de texto o PDF a analizar'
    )
    
    parser.add_argument(
        '--texto',
        '-t',
        type=str,
        help='Texto directo a analizar (entre comillas)'
    )
    
    parser.add_argument(
        '--comparar',
        '-c',
        nargs='+',
        help='Lista de archivos a comparar'
    )
    
    parser.add_argument(
        '--output',
        '-o',
        type=str,
        help='Archivo donde guardar el resultado'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='Analizador Lexile Chile v1.0.0'
    )
    
    args = parser.parse_args()
    
    # Validar argumentos
    if not args.file and not args.texto and not args.comparar:
        parser.print_help()
        return
    
    # Inicializar analizador
    print("\n🚀 Analizador de Nivel Lexile - Chile")
    print("=" * 70)
    print()
    
    try:
        analizador = AnalizadorLexileChile()
    except Exception as e:
        print(f"❌ Error al inicializar: {e}")
        return
    
    # Modo comparación
    if args.comparar:
        print(f"\n📊 Modo Comparación: {len(args.comparar)} archivos")
        print("=" * 70)
        
        documentos = {}
        for archivo in args.comparar:
            try:
                nombre = os.path.basename(archivo)
                texto = cargar_documento(archivo)
                documentos[nombre] = texto
            except Exception as e:
                print(f"❌ Error al cargar {archivo}: {e}")
        
        if documentos:
            comparar_textos(documentos, analizador)
        return
    
    # Modo análisis individual
    if args.file:
        try:
            if args.file.lower().endswith('.pdf'):
                resultado = analizar_pdf(args.file, analizador)
            else:
                texto = cargar_documento(args.file)
                print(f"\n📄 Analizando: {os.path.basename(args.file)}")
                print("=" * 70)
                resultado = analizador.analizar(texto)
                analizador.imprimir_resultado(resultado)
        except Exception as e:
            print(f"❌ Error: {e}")
            return
    
    elif args.texto:
        print(f"\n📝 Analizando texto proporcionado")
        print("=" * 70)
        resultado = analizador.analizar(args.texto)
        analizador.imprimir_resultado(resultado)
    
    # Guardar resultado si se especificó
    if args.output and 'resultado' in locals() and resultado:
        try:
            guardar_resultado(resultado, args.output)
        except Exception as e:
            print(f"❌ Error al guardar: {e}")
    
    print("\n✅ Análisis completado\n")


if __name__ == '__main__':
    main()
