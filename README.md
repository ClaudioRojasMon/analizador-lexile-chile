![Analitica](Logo.png)

# 📚 Analizador de Nivel Lexile - Chile

Sistema de análisis de complejidad lectora para textos en español, adaptado al contexto educativo chileno.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![spaCy](https://img.shields.io/badge/spaCy-NLP-green.svg)](https://spacy.io/)

## 📋 Tabla de Contenidos

- [¿Qué es el Nivel Lexile?](#-qué-es-el-nivel-lexile)
- [Motivación del Proyecto](#-motivación-del-proyecto)
- [Características](#-características)
- [Instalación](#-instalación)
- [Uso Rápido](#-uso-rápido)
- [Ejemplos](#-ejemplos)
- [Documentación](#-documentación)
- [Créditos](#-créditos)
- [Licencia](#-licencia)

## 📖 ¿Qué es el Nivel Lexile?

El **Nivel Lexile** es una medida estandarizada de complejidad lectora que ayuda a emparejar lectores con textos apropiados para su nivel de comprensión. Desarrollada por MetaMetrics, esta escala se utiliza ampliamente en educación para:

### 🎯 Propósitos Principales

- **Evaluar la dificultad de textos** - Mide qué tan complejo es un texto basándose en vocabulario, estructura de oraciones y otros factores lingüísticos
- **Medir habilidades lectoras** - Determina el nivel de lectura de un estudiante
- **Emparejar lectores con textos** - Ayuda a seleccionar materiales de lectura apropiados

### 📊 La Escala Lexile

La escala Lexile va desde principiantes (alrededor de 200L) hasta lectores avanzados (1600L+):

| Rango Lexile | Nivel en Chile | Edad | Descripción |
|--------------|----------------|------|-------------|
| 200L - 300L | 1º-2º Básico | 6-7 años | Textos simples con oraciones cortas |
| 300L - 500L | 3º-4º Básico | 8-9 años | Vocabulario elemental, estructura básica |
| 500L - 700L | 5º-6º Básico | 10-11 años | Textos intermedios, mayor variedad |
| 700L - 900L | 7º-8º Básico | 12-13 años | Textos más complejos, vocabulario amplio |
| 900L - 1050L | 1º-2º Medio | 14-15 años | Textos académicos intermedios |
| 1050L - 1200L | 3º-4º Medio | 16-17 años | Textos avanzados, conceptos abstractos |
| 1200L+ | Universidad | 18+ años | Textos profesionales y académicos |

### 🔍 Factores que Determinan el Nivel Lexile

1. **Longitud de las oraciones** - Oraciones más largas aumentan la complejidad
2. **Frecuencia de palabras** - Palabras menos comunes elevan el nivel
3. **Vocabulario especializado** - Términos técnicos o académicos
4. **Estructura sintáctica** - Complejidad gramatical
5. **Densidad conceptual** - Cantidad de ideas por oración

**Nota:** Este proyecto utiliza un algoritmo propio inspirado en la metodología Lexile, pero no es la medida oficial propietaria de MetaMetrics. Para más información, consulta [docs/que_es_lexile.md](docs/que_es_lexile.md).

## 💡 Motivación del Proyecto

### ¿Por qué nace este proyecto?

Este analizador surge de una necesidad personal y profesional: **ajustar los textos que proporciono a mis estudiantes y a mi hija para que sean apropiados a su nivel de comprensión lectora**.

Como educador, enfrentaba constantemente el desafío de:

- 📚 **Seleccionar lecturas apropiadas** - ¿Este texto es muy difícil o muy fácil para mis estudiantes de 5º básico?
- 👧 **Apoyar el aprendizaje en casa** - ¿Qué textos son adecuados para que mi hija lea de forma independiente?
- ⚖️ **Evitar la frustración** - Textos muy difíciles desmotivan; textos muy fáciles no desafían
- 📈 **Promover el progreso gradual** - Necesitaba una forma de aumentar la dificultad de manera controlada

### El Problema

Las plataformas comerciales que ofrecen análisis de nivel Lexile:
- 💰 Son costosas para uso individual o de establecimientos pequeños
- 🌍 Están diseñadas principalmente para inglés
- 🔒 Requieren suscripciones o pagos por análisis
- 🚫 No se adaptan al contexto educativo chileno

### La Solución

Este proyecto ofrece:
- ✅ **Gratuito y de código abierto** - Accesible para cualquier educador o padre
- ✅ **Adaptado al español** - Optimizado para textos en nuestro idioma
- ✅ **Contextualizado a Chile** - Niveles alineados con nuestro sistema educativo
- ✅ **Fácil de usar** - Interfaz simple y resultados claros
- ✅ **Flexible** - Analiza PDFs, archivos de texto, o texto directo

### Casos de Uso Reales

#### Para Docentes 👨‍🏫
```python
# ¿Este capítulo de libro es apropiado para 3º Básico?
resultado = analizador.analizar(texto_capitulo)
# → Lexile: 420L, Nivel: 3º-4º Básico ✓
```

#### Para Padres 👨‍👧
```python
# ¿Mi hija de 10 años puede leer este libro?
resultado = analizar_pdf("cuento_infantil.pdf", analizador)
# → Lexile: 550L, Edad: 10-11 años ✓
```

#### Para Bibliotecas 📖
```python
# Clasificar una colección de libros por nivel
libros = {"Libro1": "texto1.pdf", "Libro2": "texto2.pdf"}
resultados = comparar_textos(libros, analizador)
# → Tabla comparativa de niveles
```

## ✨ Características

### Análisis Completo
- 📊 **Nivel Lexile preciso** - Cálculo basado en múltiples métricas lingüísticas
- 🎓 **Clasificación educativa** - Niveles del sistema chileno (Básica, Media, Superior)
- 👥 **Recomendación de edad** - Rango etario apropiado
- 📈 **Estadísticas detalladas** - Métricas de complejidad del texto

### Formatos Soportados
- 📄 **PDF** - Extracción automática de texto
- 📝 **TXT, MD** - Archivos de texto plano
- ✍️ **Texto directo** - Análisis inmediato desde código

### Funcionalidades
- 🔄 **Comparación de textos** - Analiza múltiples documentos simultáneamente
- 💾 **Exportación de resultados** - Guarda análisis en archivos
- 🖥️ **CLI completa** - Herramienta de línea de comandos
- 🐍 **API Python** - Integrable en tus propios proyectos

## 🚀 Instalación

### Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Instalación Rápida

```bash
# 1. Clonar el repositorio
git clone https://github.com/ClaudioRojasMon/analizador-lexile-chile.git
cd analizador-lexile-chile

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Descargar modelo de español de spaCy
python -m spacy download es_core_news_sm

# 4. ¡Listo! Prueba el analizador
python examples.py
```

### Instalación como Paquete

```bash
# Instalar el paquete en tu sistema
pip install -e .

# Ahora puedes usar el comando 'lexile' desde cualquier lugar
lexile --file mi_texto.txt
```

## 🎯 Uso Rápido

### Desde Python

```python
from src.analizador_lexile import AnalizadorLexileChile

# Crear analizador
analizador = AnalizadorLexileChile()

# Analizar texto
texto = """
La fotosíntesis es un proceso mediante el cual las plantas
convierten la luz solar en energía química.
"""

resultado = analizador.analizar(texto)
analizador.imprimir_resultado(resultado)
```

**Salida:**
```
📊 Nivel Lexile: 850L
   Rango: 800L - 900L

🎓 Nivel Educativo: 7º-8º Básico
   Clasificación: Avanzado Básico
   Edad recomendada: 12-13 años
```

### Desde Línea de Comandos

```bash
# Analizar un archivo
python main.py --file documento.txt

# Analizar un PDF
python main.py --file libro.pdf

# Comparar varios textos
python main.py --comparar texto1.txt texto2.pdf texto3.txt

# Guardar resultado
python main.py --file texto.txt --output resultado.txt
```

### Analizar PDF

```python
from src.analizador_lexile import AnalizadorLexileChile
from src.utilidades import analizar_pdf

analizador = AnalizadorLexileChile()
resultado = analizar_pdf("mi_libro.pdf", analizador)
```

## 📊 Ejemplos

### Ejemplo 1: Texto Simple (Nivel Básico)

```python
texto_basico = "El perro corre. El gato salta. Son amigos."

resultado = analizador.analizar(texto_basico)
# → Lexile: 250L (1º-2º Básico)
```

### Ejemplo 2: Comparar Múltiples Textos

```python
from src.utilidades import comparar_textos

textos = {
    "Cuento Infantil": cargar_documento("cuento.txt"),
    "Texto Escolar": cargar_documento("libro_texto.pdf"),
    "Artículo Académico": cargar_documento("paper.pdf")
}

resultados = comparar_textos(textos, analizador)
```

**Salida:**
```
COMPARACIÓN DE MÚLTIPLES TEXTOS
================================================================
Nombre                      Lexile   Grado                Palabras
----------------------------------------------------------------
Cuento Infantil             320L     3º-4º Básico         450
Texto Escolar               720L     7º-8º Básico         2100
Artículo Académico          1350L    Universidad          4500
```

### Ejemplo 3: Uso Práctico - Seleccionar Lecturas

```python
# Tengo 5 libros y quiero saber cuál es apropiado para 5º Básico
libros = {
    "Libro A": cargar_documento("libro_a.pdf"),
    "Libro B": cargar_documento("libro_b.pdf"),
    "Libro C": cargar_documento("libro_c.pdf"),
}

for nombre, texto in libros.items():
    resultado = analizador.analizar(texto)
    if 500 <= resultado['lexile'] <= 700:  # Rango de 5º-6º Básico
        print(f"✓ {nombre} es apropiado: {resultado['lexile']}L")
    else:
        print(f"✗ {nombre} no es apropiado: {resultado['lexile']}L")
```

## 📖 Documentación

### Documentación Completa

- **[¿Qué es Lexile?](docs/que_es_lexile.md)** - Explicación detallada del sistema Lexile
- **[Guía de Inicio Rápido](QUICKSTART.md)** - Primeros pasos en 5 minutos
- **[Ejemplos Avanzados](examples.py)** - Casos de uso completos
- **[API Reference](docs/api_reference.md)** - Documentación técnica de funciones

### Interpretación de Resultados

#### Nivel de Confianza
- **Alta** - 500+ palabras, 20+ oraciones (resultado muy confiable)
- **Media** - 200+ palabras, 10+ oraciones (resultado confiable)
- **Baja** - Menos de 200 palabras (resultado orientativo)

#### Qué Significan las Métricas

| Métrica | Qué indica | Valor ideal |
|---------|------------|-------------|
| Palabras por oración | Complejidad sintáctica | 8-15 para textos escolares |
| Sílabas por palabra | Complejidad léxica | 2-3 para textos básicos |
| Palabras raras % | Vocabulario especializado | <10% para textos escolares |
| Diversidad léxica | Riqueza de vocabulario | 0.4-0.7 es apropiado |

## 🛠️ Solución de Problemas

### Error: Modelo de spaCy no encontrado
```bash
python -m spacy download es_core_news_sm
```

### Error al leer PDF
- Verifica que el PDF contenga texto (no solo imágenes)
- Si es un PDF escaneado, necesitarás OCR
- Intenta convertirlo a .txt primero

### Resultados inesperados
- Textos muy cortos (<100 palabras) pueden dar resultados menos precisos
- Textos con muchos nombres propios pueden alterar el análisis
- Poesía y textos con formato especial requieren interpretación cuidadosa

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Este proyecto busca mejorar continuamente para servir mejor a la comunidad educativa.

### Cómo Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/MejorAnalisis`)
3. Commit tus cambios (`git commit -m 'feat: Mejorar análisis de complejidad'`)
4. Push a la rama (`git push origin feature/MejorAnalisis`)
5. Abre un Pull Request

### Áreas de Mejora

- 📚 Expandir diccionario de frecuencias
- 🎯 Afinar clasificación por niveles
- 📊 Agregar más métricas de complejidad
- 🌐 Mejorar extracción de PDFs
- 📝 Ampliar documentación y ejemplos

## 📊 Limitaciones y Consideraciones

### Importante Saber

- ✅ **Este no es el Lexile oficial** - Es una aproximación inspirada en la metodología
- ✅ **Optimizado para español** - Puede no funcionar bien con otros idiomas
- ✅ **Textos literarios** - Poesía y prosa poética pueden dar resultados variables
- ✅ **Textos técnicos** - Pueden clasificarse más altos por vocabulario especializado

### Cuándo Usar Esta Herramienta

**Ideal para:**
- 👍 Seleccionar lecturas apropiadas para un nivel
- 👍 Comparar dificultad entre textos
- 👍 Organizar bibliotecas por nivel
- 👍 Evaluar materiales educativos

**No ideal para:**
- 👎 Evaluar la calidad literaria de un texto
- 👎 Determinar el valor educativo completo
- 👎 Reemplazar el juicio profesional docente

## 🙏 Créditos

### Autor Principal
**Claudio Rojas** - Docente y desarrollador
- Conceptualización del proyecto
- Análisis inicial y casos de uso
- Adaptación al contexto educativo chileno

### Desarrollo
Este proyecto fue desarrollado mediante colaboración humano-IA:
- **Análisis y diseño:** Claudio Rojas
- **Transformación a proyecto profesional:** Asistencia de Claude (Anthropic)

Para más detalles sobre las contribuciones, ver [CREDITS.md](CREDITS.md)

### Agradecimientos
- A la comunidad educativa chilena
- A MetaMetrics por desarrollar el sistema Lexile original
- A los desarrolladores de spaCy por sus herramientas de NLP
- A todos los docentes que trabajan por mejorar la comprensión lectora

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 📧 Contacto

Si tienes preguntas, sugerencias o quieres reportar un problema:
- 🐛 Abre un [Issue](https://github.com/ClaudioRojasMon/analizador-lexile-chile/issues)
- 💬 Inicia una [Discusión](https://github.com/ClaudioRojasMon/analizador-lexile-chile/discussions)

---

⭐ Si este proyecto te es útil, ¡considera darle una estrella en GitHub!

💙 Desarrollado con pasión por la educación y la lectura desde el sur de Chile 🇨🇱
