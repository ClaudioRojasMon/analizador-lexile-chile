"""
Analizador de Nivel Lexile para Textos en Español
Adaptado al sistema educativo chileno

Este módulo proporciona funcionalidad para analizar textos en español
y determinar su nivel de complejidad lectora (Lexile).
"""

import re
import numpy as np
from collections import Counter
import math
import spacy


class AnalizadorLexileChile:
    """
    Analizador de nivel Lexile adaptado para el sistema educativo chileno.
    
    Permite evaluar la complejidad de textos en español y clasificarlos
    según los niveles educativos de Chile (Básica, Media, Universidad).
    
    Attributes:
        nlp: Modelo de procesamiento de lenguaje natural de spaCy
        frecuencias: Diccionario de frecuencias de palabras comunes
    """
    
    def __init__(self):
        """Inicializa el analizador cargando el modelo de spaCy."""
        print("Inicializando analizador para sistema educativo chileno...")
        try:
            self.nlp = spacy.load("es_core_news_sm")
            print("✓ Modelo cargado correctamente\n")
        except:
            print("❌ Error: Modelo de spaCy no encontrado")
            print("Ejecuta: python -m spacy download es_core_news_sm")
            raise
        
        self.frecuencias = self._cargar_frecuencias_expandidas()
        print(f"✓ Diccionario con {len(self.frecuencias)} palabras comunes")
        print("✓ Sistema educativo: Chile 🇨🇱\n")
    
    def analizar(self, texto: str) -> dict:
        """
        Analiza un texto y retorna su nivel Lexile.
        
        Args:
            texto: Texto a analizar (string)
            
        Returns:
            dict: Diccionario con los resultados del análisis:
                - lexile: Nivel Lexile estimado
                - rango: Rango del nivel Lexile
                - grado: Nivel educativo chileno
                - nivel: Descripción del nivel
                - edad: Rango de edad recomendado
                - confianza: Nivel de confianza del análisis
                - estadisticas: Métricas detalladas del texto
        """
        texto = texto.strip()
        if not texto:
            return {'error': 'Texto vacío'}
        
        doc = self.nlp(texto)
        oraciones = list(doc.sents)
        
        if not oraciones:
            return {'error': 'No se detectaron oraciones'}
        
        palabras = [t for t in doc if not t.is_punct and not t.is_space]
        num_palabras = len(palabras)
        
        if num_palabras == 0:
            return {'error': 'No se detectaron palabras'}
        
        # Calcular métricas
        longitudes_oraciones = []
        for sent in oraciones:
            palabras_sent = [t for t in sent if not t.is_punct and not t.is_space]
            longitudes_oraciones.append(len(palabras_sent))
        
        long_promedio = np.mean(longitudes_oraciones)
        long_desv = np.std(longitudes_oraciones)
        
        # Frecuencia de palabras
        palabras_raras = 0
        rankings = []
        
        for palabra in palabras:
            lemma = palabra.lemma_.lower()
            if lemma in self.frecuencias:
                rankings.append(self.frecuencias[lemma])
            elif palabra.text.lower() in self.frecuencias:
                rankings.append(self.frecuencias[palabra.text.lower()])
            else:
                rankings.append(2000)
                palabras_raras += 1
        
        freq_promedio = np.mean(rankings) if rankings else 1000
        percentil_raras = (palabras_raras / num_palabras) * 100
        
        # Análisis de sílabas
        total_silabas = sum(self._contar_silabas(p.text) for p in palabras)
        silabas_promedio = total_silabas / num_palabras if num_palabras > 0 else 0
        
        # Palabras complejas
        palabras_complejas = sum(1 for p in palabras if self._es_compleja(p.text))
        ratio_complejas = palabras_complejas / num_palabras if num_palabras > 0 else 0
        
        # Diversidad léxica
        palabras_unicas = len(set(p.lemma_.lower() for p in palabras))
        diversidad = palabras_unicas / num_palabras if num_palabras > 0 else 0
        
        # Calcular Lexile
        lexile = self._calcular_lexile(
            long_promedio, long_desv, freq_promedio,
            silabas_promedio, ratio_complejas, percentil_raras
        )
        
        # Clasificar según sistema educativo chileno
        clasificacion = self._clasificar_nivel_chile(lexile)
        
        # Calcular confianza
        confianza = self._calcular_confianza(num_palabras, len(oraciones))
        
        return {
            'lexile': round(lexile),
            'rango': f"{round(lexile-50)}L - {round(lexile+50)}L",
            'grado': clasificacion['grado'],
            'nivel': clasificacion['nivel'],
            'edad': clasificacion['edad'],
            'confianza': confianza,
            'estadisticas': {
                'palabras': num_palabras,
                'oraciones': len(oraciones),
                'palabras_por_oracion': round(long_promedio, 1),
                'silabas_por_palabra': round(silabas_promedio, 2),
                'palabras_raras_pct': round(percentil_raras, 1),
                'palabras_complejas_pct': round(ratio_complejas * 100, 1),
                'diversidad_lexica': round(diversidad, 3)
            }
        }
    
    def _calcular_lexile(self, long_prom, long_desv, freq_prom, 
                        sil_prom, ratio_complejas, pct_raras):
        """Calcula el nivel Lexile basado en múltiples métricas."""
        base = 100
        
        # Componente de longitud de oración
        if long_prom <= 5:
            comp_longitud = 0
        elif long_prom <= 10:
            comp_longitud = (long_prom - 5) * 80
        elif long_prom <= 20:
            comp_longitud = 400 + (long_prom - 10) * 50
        else:
            comp_longitud = 900 + (long_prom - 20) * 30
        
        # Componente de frecuencia
        comp_frecuencia = max(0, (freq_prom - 1.5) * 200)
        
        # Componente de palabras raras
        if long_prom > 8:
            comp_raras = pct_raras * 2
        else:
            comp_raras = pct_raras * 0.5
        
        # Componente de sílabas
        comp_silabas = max(0, (sil_prom - 1.8) * 150)
        
        # Componente de palabras complejas
        comp_complejas = ratio_complejas * 100
        
        # Componente de variabilidad
        comp_variabilidad = long_desv * 8
        
        lexile = (base + comp_longitud + comp_frecuencia + comp_raras + 
                 comp_silabas + comp_complejas + comp_variabilidad)
        
        return max(50, min(1600, lexile))
    
    def _clasificar_nivel_chile(self, lexile):
        """
        Clasifica el texto según el sistema educativo chileno.
        
        Args:
            lexile: Nivel Lexile calculado
            
        Returns:
            dict: Información de la clasificación
        """
        if lexile < 300:
            return {
                'grado': '1º-2º Básico',
                'nivel': 'Inicial',
                'edad': '6-7 años'
            }
        elif lexile < 500:
            return {
                'grado': '3º-4º Básico',
                'nivel': 'Elemental',
                'edad': '8-9 años'
            }
        elif lexile < 700:
            return {
                'grado': '5º-6º Básico',
                'nivel': 'Intermedio',
                'edad': '10-11 años'
            }
        elif lexile < 900:
            return {
                'grado': '7º-8º Básico',
                'nivel': 'Avanzado Básico',
                'edad': '12-13 años'
            }
        elif lexile < 1050:
            return {
                'grado': '1º-2º Medio',
                'nivel': 'Media Inicial',
                'edad': '14-15 años'
            }
        elif lexile < 1200:
            return {
                'grado': '3º-4º Medio',
                'nivel': 'Media Avanzada',
                'edad': '16-17 años'
            }
        else:
            return {
                'grado': 'Universidad/Profesional',
                'nivel': 'Superior',
                'edad': '18+ años'
            }
    
    def _calcular_confianza(self, num_palabras, num_oraciones):
        """Calcula el nivel de confianza del análisis."""
        if num_palabras >= 500 and num_oraciones >= 20:
            return "Alta"
        elif num_palabras >= 200 and num_oraciones >= 10:
            return "Media"
        else:
            return "Baja"
    
    def _contar_silabas(self, palabra):
        """Cuenta las sílabas de una palabra en español."""
        palabra = palabra.lower()
        vocales = 'aeiouáéíóúü'
        silabas = 0
        anterior_vocal = False
        
        for char in palabra:
            es_vocal = char in vocales
            if es_vocal and not anterior_vocal:
                silabas += 1
            anterior_vocal = es_vocal
        
        return max(1, silabas)
    
    def _es_compleja(self, palabra):
        """Determina si una palabra es compleja (3+ sílabas)."""
        return self._contar_silabas(palabra) >= 3
    
    def _cargar_frecuencias_expandidas(self):
        """Carga diccionario expandido de frecuencias de palabras comunes."""
        # Diccionario básico de palabras más frecuentes en español
        palabras_base = {
            'el': 1, 'la': 2, 'de': 3, 'que': 4, 'y': 5,
            'a': 6, 'en': 7, 'un': 8, 'ser': 9, 'se': 10,
            'no': 11, 'haber': 12, 'por': 13, 'con': 14, 'su': 15,
            'para': 16, 'como': 17, 'estar': 18, 'tener': 19, 'le': 20,
        }
        
        # Palabras adicionales comunes
        palabras_adicionales = {
            'todo': 21, 'pero': 22, 'más': 23, 'hacer': 24, 'o': 25,
            'poder': 26, 'decir': 27, 'este': 28, 'ir': 29, 'otro': 30,
            'ese': 31, 'si': 32, 'me': 33, 'ya': 34, 'ver': 35,
            'porque': 36, 'dar': 37, 'cuando': 38, 'él': 39, 'muy': 40,
            'sin': 41, 'vez': 42, 'mucho': 43, 'saber': 44, 'qué': 45,
            'sobre': 46, 'mi': 47, 'alguno': 48, 'mismo': 49, 'yo': 50,
        }
        
        # Combinar diccionarios
        frecuencias = {**palabras_base, **palabras_adicionales}
        
        return frecuencias
    
    def imprimir_resultado(self, resultado):
        """
        Imprime el resultado del análisis de forma legible.
        
        Args:
            resultado: Diccionario con los resultados del análisis
        """
        if 'error' in resultado:
            print(f"❌ Error: {resultado['error']}")
            return
        
        print("=" * 70)
        print("   ANÁLISIS DE NIVEL LEXILE")
        print("=" * 70)
        print()
        print(f"📊 Nivel Lexile: {resultado['lexile']}L")
        print(f"   Rango: {resultado['rango']}")
        print()
        print(f"🎓 Nivel Educativo: {resultado['grado']}")
        print(f"   Clasificación: {resultado['nivel']}")
        print(f"   Edad recomendada: {resultado['edad']}")
        print()
        print(f"✓ Confianza del análisis: {resultado['confianza']}")
        print()
        print("📈 Estadísticas del texto:")
        print(f"   • Palabras totales: {resultado['estadisticas']['palabras']}")
        print(f"   • Oraciones: {resultado['estadisticas']['oraciones']}")
        print(f"   • Palabras por oración: {resultado['estadisticas']['palabras_por_oracion']}")
        print(f"   • Sílabas por palabra: {resultado['estadisticas']['silabas_por_palabra']}")
        print(f"   • Palabras raras: {resultado['estadisticas']['palabras_raras_pct']}%")
        print(f"   • Palabras complejas: {resultado['estadisticas']['palabras_complejas_pct']}%")
        print(f"   • Diversidad léxica: {resultado['estadisticas']['diversidad_lexica']}")
        print()
        print("=" * 70)
