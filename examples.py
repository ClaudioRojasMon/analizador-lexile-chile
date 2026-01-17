"""
Ejemplos de Uso del Analizador Lexile Chile
Casos de uso comunes y prácticos
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from analizador_lexile import AnalizadorLexileChile
from utilidades import cargar_documento, comparar_textos, guardar_resultado


def ejemplo_1_texto_simple():
    """Ejemplo 1: Analizar un texto simple."""
    print("\n" + "="*70)
    print("EJEMPLO 1: Analizar un texto simple")
    print("="*70 + "\n")
    
    analizador = AnalizadorLexileChile()
    
    texto = """
    El perro corre por el parque. El gato salta sobre la cerca.
    Son amigos y juegan juntos todos los días.
    """
    
    resultado = analizador.analizar(texto)
    analizador.imprimir_resultado(resultado)


def ejemplo_2_texto_complejo():
    """Ejemplo 2: Analizar un texto más complejo."""
    print("\n" + "="*70)
    print("EJEMPLO 2: Analizar un texto complejo")
    print("="*70 + "\n")
    
    analizador = AnalizadorLexileChile()
    
    texto = """
    La fotosíntesis es un proceso bioquímico fundamental mediante el cual
    las plantas, algas y algunas bacterias convierten la energía lumínica
    en energía química. Este mecanismo esencial permite la síntesis de
    compuestos orgánicos a partir de dióxido de carbono y agua, liberando
    oxígeno como subproducto. La clorofila, pigmento característico de los
    cloroplastos, absorbe principalmente la luz en los espectros azul y rojo,
    reflejando el verde que percibimos visualmente.
    """
    
    resultado = analizador.analizar(texto)
    analizador.imprimir_resultado(resultado)


def ejemplo_3_desde_archivo():
    """Ejemplo 3: Analizar un archivo de texto."""
    print("\n" + "="*70)
    print("EJEMPLO 3: Analizar desde archivo")
    print("="*70 + "\n")
    
    analizador = AnalizadorLexileChile()
    
    # Crear un archivo de ejemplo
    ruta_ejemplo = "data/ejemplo.txt"
    os.makedirs("data", exist_ok=True)
    
    with open(ruta_ejemplo, 'w', encoding='utf-8') as f:
        f.write("""
        El sistema educativo chileno se divide en varios niveles.
        La educación básica comprende desde primero a octavo básico.
        Luego viene la educación media, que va desde primero a cuarto medio.
        Finalmente, está la educación superior universitaria.
        """)
    
    print(f"Archivo creado: {ruta_ejemplo}")
    
    try:
        texto = cargar_documento(ruta_ejemplo)
        resultado = analizador.analizar(texto)
        analizador.imprimir_resultado(resultado)
    except Exception as e:
        print(f"Error: {e}")


def ejemplo_4_comparar_textos():
    """Ejemplo 4: Comparar múltiples textos."""
    print("\n" + "="*70)
    print("EJEMPLO 4: Comparar múltiples textos")
    print("="*70 + "\n")
    
    analizador = AnalizadorLexileChile()
    
    textos = {
        "Texto Infantil": "El gato come. El perro juega. Son amigos.",
        
        "Texto Escolar": """
        Los animales vertebrados se clasifican en cinco grupos principales.
        Los mamíferos, aves, reptiles, anfibios y peces tienen características
        únicas que los distinguen entre sí.
        """,
        
        "Texto Académico": """
        La teoría de la relatividad especial, propuesta por Albert Einstein en 1905,
        revolucionó nuestra comprensión del espacio y el tiempo. Esta teoría establece
        que las leyes de la física son idénticas en todos los sistemas de referencia
        inerciales, y que la velocidad de la luz en el vacío es constante e independiente
        del movimiento de la fuente emisora o del observador.
        """
    }
    
    resultados = comparar_textos(textos, analizador)
    
    print("\n📊 Análisis detallado de cada texto:")
    for nombre, texto in textos.items():
        print(f"\n--- {nombre} ---")
        resultado = analizador.analizar(texto)
        print(f"Lexile: {resultado['lexile']}L")
        print(f"Nivel: {resultado['grado']}")


def ejemplo_5_guardar_resultado():
    """Ejemplo 5: Guardar resultado en archivo."""
    print("\n" + "="*70)
    print("EJEMPLO 5: Guardar resultado en archivo")
    print("="*70 + "\n")
    
    analizador = AnalizadorLexileChile()
    
    texto = """
    La inteligencia artificial es un campo de la informática que busca
    crear sistemas capaces de realizar tareas que normalmente requieren
    inteligencia humana. Estos sistemas pueden aprender, razonar y
    tomar decisiones basadas en datos.
    """
    
    resultado = analizador.analizar(texto)
    analizador.imprimir_resultado(resultado)
    
    # Guardar resultado
    os.makedirs("outputs", exist_ok=True)
    ruta_salida = "outputs/resultado_ejemplo.txt"
    guardar_resultado(resultado, ruta_salida)


def menu_ejemplos():
    """Menú interactivo de ejemplos."""
    while True:
        print("\n" + "="*70)
        print("   EJEMPLOS DEL ANALIZADOR LEXILE CHILE")
        print("="*70)
        print("\nSelecciona un ejemplo:")
        print("  1. Texto simple (nivel básico)")
        print("  2. Texto complejo (nivel avanzado)")
        print("  3. Analizar desde archivo")
        print("  4. Comparar múltiples textos")
        print("  5. Guardar resultado en archivo")
        print("  6. Ejecutar todos los ejemplos")
        print("  0. Salir")
        print()
        
        opcion = input("Opción: ").strip()
        
        if opcion == '1':
            ejemplo_1_texto_simple()
        elif opcion == '2':
            ejemplo_2_texto_complejo()
        elif opcion == '3':
            ejemplo_3_desde_archivo()
        elif opcion == '4':
            ejemplo_4_comparar_textos()
        elif opcion == '5':
            ejemplo_5_guardar_resultado()
        elif opcion == '6':
            ejemplo_1_texto_simple()
            ejemplo_2_texto_complejo()
            ejemplo_3_desde_archivo()
            ejemplo_4_comparar_textos()
            ejemplo_5_guardar_resultado()
            print("\n✅ Todos los ejemplos ejecutados\n")
            break
        elif opcion == '0':
            print("\n👋 ¡Hasta luego!\n")
            break
        else:
            print("\n❌ Opción inválida. Intenta de nuevo.")
        
        input("\nPresiona Enter para continuar...")


if __name__ == '__main__':
    menu_ejemplos()
