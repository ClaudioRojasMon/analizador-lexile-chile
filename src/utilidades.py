"""
Utilidades para el Analizador Lexile
Funciones auxiliares para cargar y procesar documentos
"""

import PyPDF2
import pdfplumber
import os


def cargar_documento(ruta):
    """
    Carga cualquier documento automáticamente (PDF o TXT).
    
    Detecta automáticamente el tipo de archivo y utiliza el método
    apropiado para extraer el texto.
    
    Args:
        ruta (str): Ruta al archivo (PDF, TXT, MD, etc.)
        
    Returns:
        str: Texto extraído del documento
        
    Raises:
        FileNotFoundError: Si el archivo no existe
        Exception: Si hay un error al procesar el archivo
    """
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"El archivo no existe: {ruta}")
    
    # Detectar extensión
    if ruta.lower().endswith('.pdf'):
        return _extraer_texto_pdf(ruta)
    else:
        return _leer_texto(ruta)


def _extraer_texto_pdf(ruta):
    """
    Extrae texto de un archivo PDF.
    
    Intenta primero con pdfplumber (más preciso), y si falla,
    usa PyPDF2 como respaldo.
    
    Args:
        ruta (str): Ruta al archivo PDF
        
    Returns:
        str: Texto extraído del PDF
    """
    texto = ""
    
    # Intentar con pdfplumber primero
    try:
        with pdfplumber.open(ruta) as pdf:
            for pagina in pdf.pages:
                texto_pagina = pagina.extract_text()
                if texto_pagina:
                    texto += texto_pagina + "\n"
        
        if texto.strip():
            return texto
    except Exception as e:
        print(f"⚠️  pdfplumber falló: {e}")
        print("   Intentando con PyPDF2...")
    
    # Respaldo con PyPDF2
    try:
        with open(ruta, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for pagina in pdf_reader.pages:
                texto_pagina = pagina.extract_text()
                if texto_pagina:
                    texto += texto_pagina + "\n"
        
        return texto
    except Exception as e:
        raise Exception(f"Error al leer PDF: {e}")


def _leer_texto(ruta):
    """
    Lee un archivo de texto plano.
    
    Args:
        ruta (str): Ruta al archivo de texto
        
    Returns:
        str: Contenido del archivo
    """
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        # Intentar con latin-1 si UTF-8 falla
        with open(ruta, 'r', encoding='latin-1') as f:
            return f.read()


def analizar_pdf(ruta_pdf, analizador):
    """
    Analiza un archivo PDF completo.
    
    Extrae el texto del PDF y lo analiza con el analizador Lexile.
    Muestra un preview del texto extraído antes del análisis.
    
    Args:
        ruta_pdf (str): Ruta al archivo PDF
        analizador: Instancia de AnalizadorLexileChile
        
    Returns:
        dict: Resultados del análisis o None si hay error
    """
    print(f"\n📄 Cargando PDF: {os.path.basename(ruta_pdf)}")
    print("=" * 70)
    
    try:
        texto_completo = _extraer_texto_pdf(ruta_pdf)
    except Exception as e:
        print(f"❌ Error al extraer texto del PDF: {e}")
        print("\n💡 Posibles soluciones:")
        print("   1. Asegúrate de que el PDF no esté protegido")
        print("   2. Verifica que el PDF contenga texto (no solo imágenes)")
        print("   3. Intenta convertir el PDF a .txt primero")
        return None
    
    if not texto_completo.strip():
        print("❌ El PDF no contiene texto extraíble")
        print("💡 Este PDF puede contener solo imágenes escaneadas")
        print("   Necesitarías OCR para extraer el texto")
        return None
    
    # Mostrar preview
    print(f"\n📝 Preview del texto extraído:")
    print("-" * 70)
    preview = texto_completo[:500] + "..." if len(texto_completo) > 500 else texto_completo
    print(preview)
    print("-" * 70)
    print(f"\n   Total de caracteres: {len(texto_completo)}")
    
    # Analizar con Lexile
    print("\n🔍 ANALIZANDO NIVEL LEXILE...")
    print("=" * 70)
    
    resultado = analizador.analizar(texto_completo)
    analizador.imprimir_resultado(resultado)
    
    return resultado


def comparar_textos(textos_dict, analizador):
    """
    Compara múltiples textos y muestra una tabla comparativa.
    
    Args:
        textos_dict (dict): Diccionario {"nombre": "texto"}
        analizador: Instancia de AnalizadorLexileChile
        
    Returns:
        list: Lista de resultados ordenados por nivel Lexile
    """
    print("=" * 70)
    print("COMPARACIÓN DE MÚLTIPLES TEXTOS")
    print("=" * 70)
    print()
    
    resultados = []
    
    for nombre, texto in textos_dict.items():
        resultado = analizador.analizar(texto)
        if 'error' not in resultado:
            resultados.append({
                'nombre': nombre,
                'lexile': resultado['lexile'],
                'grado': resultado['grado'],
                'palabras': resultado['estadisticas']['palabras'],
                'oraciones': resultado['estadisticas']['oraciones']
            })
    
    # Imprimir tabla comparativa
    print(f"{'Nombre':<30} {'Lexile':>8} {'Grado':<25} {'Palabras':>8}")
    print("-" * 70)
    
    for r in sorted(resultados, key=lambda x: x['lexile']):
        print(f"{r['nombre']:<30} {r['lexile']:>6}L  {r['grado']:<25} {r['palabras']:>8}")
    
    print()
    return resultados


def cargar_multiples_documentos(rutas_dict):
    """
    Carga múltiples documentos de una vez.
    
    Args:
        rutas_dict (dict): Diccionario {"nombre": "ruta/al/archivo"}
        
    Returns:
        dict: Diccionario {"nombre": "texto_extraído"}
    """
    documentos = {}
    
    for nombre, ruta in rutas_dict.items():
        try:
            documentos[nombre] = cargar_documento(ruta)
            print(f"✓ Cargado: {nombre}")
        except Exception as e:
            print(f"❌ Error al cargar {nombre}: {e}")
    
    return documentos


def guardar_resultado(resultado, ruta_salida):
    """
    Guarda el resultado del análisis en un archivo de texto.
    
    Args:
        resultado (dict): Resultado del análisis
        ruta_salida (str): Ruta donde guardar el archivo
    """
    with open(ruta_salida, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("   ANÁLISIS DE NIVEL LEXILE\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"📊 Nivel Lexile: {resultado['lexile']}L\n")
        f.write(f"   Rango: {resultado['rango']}\n\n")
        f.write(f"🎓 Nivel Educativo: {resultado['grado']}\n")
        f.write(f"   Clasificación: {resultado['nivel']}\n")
        f.write(f"   Edad recomendada: {resultado['edad']}\n\n")
        f.write(f"✓ Confianza del análisis: {resultado['confianza']}\n\n")
        f.write("📈 Estadísticas del texto:\n")
        for key, value in resultado['estadisticas'].items():
            f.write(f"   • {key.replace('_', ' ').title()}: {value}\n")
    
    print(f"\n✓ Resultado guardado en: {ruta_salida}")
