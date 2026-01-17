# 🚀 Guía de Inicio Rápido - 5 Minutos

¿Quieres empezar a analizar textos inmediatamente? Esta guía te llevará de cero a tu primer análisis en 5 minutos.

## ⏱️ Instalación Express

```bash
# 1. Clonar (30 segundos)
git clone https://github.com/ClaudioRojasMon/analizador-lexile-chile.git
cd analizador-lexile-chile

# 2. Instalar (2 minutos)
pip install -r requirements.txt
python -m spacy download es_core_news_sm

# 3. ¡Listo para usar!
```

## 🎯 Tu Primer Análisis (60 segundos)

### Opción 1: Menú Interactivo

```bash
python examples.py
```

Selecciona una opción del menú y ve los resultados inmediatamente.

### Opción 2: Desde Python

Crea un archivo `prueba.py`:

```python
from src.analizador_lexile import AnalizadorLexileChile

# Crear analizador
analizador = AnalizadorLexileChile()

# Tu texto
texto = """
La fotosíntesis es un proceso bioquímico fundamental.
Las plantas convierten la luz solar en energía química.
Este proceso es esencial para la vida en la Tierra.
"""

# Analizar
resultado = analizador.analizar(texto)
analizador.imprimir_resultado(resultado)
```

Ejecuta:
```bash
python prueba.py
```

**Resultado:**
```
📊 Nivel Lexile: 920L
🎓 Nivel Educativo: 1º-2º Medio
   Edad recomendada: 14-15 años
```

## 📄 Analizar un Archivo

### Archivo de Texto

```bash
python main.py --file mi_texto.txt
```

### PDF

```bash
python main.py --file documento.pdf
```

### Comparar Varios

```bash
python main.py --comparar texto1.txt texto2.pdf texto3.txt
```

## 💡 Casos de Uso Rápidos

### Caso 1: "¿Este libro es apropiado para mi hijo de 10 años?"

```python
from src.analizador_lexile import AnalizadorLexileChile
from src.utilidades import cargar_documento

analizador = AnalizadorLexileChile()
texto = cargar_documento("libro.pdf")
resultado = analizador.analizar(texto)

if 500 <= resultado['lexile'] <= 700:
    print("✓ Apropiado para 10-11 años")
else:
    print(f"Nivel: {resultado['grado']}")
```

### Caso 2: "Organizar mi biblioteca por nivel"

```python
from src.utilidades import cargar_multiples_documentos, comparar_textos

# Cargar todos los libros
libros = {
    "Libro 1": "libros/libro1.pdf",
    "Libro 2": "libros/libro2.pdf",
    "Libro 3": "libros/libro3.txt",
}

documentos = cargar_multiples_documentos(libros)
resultados = comparar_textos(documentos, analizador)

# Resultado: Tabla ordenada por nivel
```

### Caso 3: "Encontrar textos para 5º Básico"

```python
for nombre, texto in mis_textos.items():
    resultado = analizador.analizar(texto)
    
    # 5º-6º Básico = 500L - 700L
    if 500 <= resultado['lexile'] <= 700:
        print(f"✓ {nombre}: {resultado['lexile']}L")
```

## 📊 Entender los Resultados

### Nivel Lexile
```
200L   = Muy básico (1º-2º Básico)
500L   = Elemental (3º-4º Básico)
800L   = Intermedio (7º-8º Básico)
1100L  = Avanzado (3º-4º Medio)
1400L+ = Universitario
```

### Nivel de Confianza
- **Alta**: 500+ palabras → Muy confiable
- **Media**: 200+ palabras → Confiable
- **Baja**: <200 palabras → Orientativo

## 🛠️ Solución de Problemas Rápida

### Error: "Modelo no encontrado"
```bash
python -m spacy download es_core_news_sm
```

### Error: "Archivo no encontrado"
Verifica la ruta:
```bash
# Ver archivos en carpeta actual
ls
# O con ruta completa
python main.py --file /ruta/completa/archivo.txt
```

### PDF no se puede leer
- ¿Está protegido? → Desproteger
- ¿Solo imágenes? → Necesitas OCR
- ¿Archivo corrupto? → Probar con otro PDF

## 📚 Próximos Pasos

Ahora que sabes lo básico:

1. **Lee la documentación completa:** [README.md](README.md)
2. **Aprende sobre Lexile:** [docs/que_es_lexile.md](docs/que_es_lexile.md)
3. **Explora ejemplos avanzados:** `python examples.py`
4. **Adapta a tus necesidades:** Modifica el código en `src/`

## 💡 Tips Rápidos

### Para Docentes
```python
# Crear colección de textos por nivel
nivel_basico = []
nivel_intermedio = []
nivel_avanzado = []

for texto in mis_textos:
    lexile = analizador.analizar(texto)['lexile']
    
    if lexile < 600:
        nivel_basico.append(texto)
    elif lexile < 1000:
        nivel_intermedio.append(texto)
    else:
        nivel_avanzado.append(texto)
```

### Para Padres
```python
# Verificar si un libro es apropiado
edad_hijo = 12  # años
texto_libro = cargar_documento("libro.pdf")
resultado = analizador.analizar(texto_libro)

# Regla simple: edad × 100 ± 100
lexile_ideal = edad_hijo * 100
es_apropiado = abs(resultado['lexile'] - lexile_ideal) <= 100

print(f"¿Apropiado? {es_apropiado}")
```

## 🎯 Comandos Esenciales

```bash
# Analizar texto
python main.py --file archivo.txt

# Analizar PDF
python main.py --file documento.pdf

# Comparar textos
python main.py --comparar archivo1.txt archivo2.pdf

# Guardar resultado
python main.py --file texto.txt --output resultado.txt

# Menú interactivo
python examples.py

# Ayuda
python main.py --help
```

## ✅ Checklist de Inicio

- [x] Python 3.7+ instalado
- [x] Repositorio clonado
- [x] Dependencias instaladas (`pip install -r requirements.txt`)
- [x] Modelo de spaCy descargado (`python -m spacy download es_core_news_sm`)
- [x] Primer análisis realizado
- [ ] Documentación completa leída
- [ ] Ejemplos explorados
- [ ] Adaptado a mi caso de uso

## 🚀 ¡Estás Listo!

Ya sabes lo básico. Ahora explora, experimenta y adapta la herramienta a tus necesidades educativas.

**¿Preguntas?** Lee el [README completo](README.md) o abre un [Issue](https://github.com/ClaudioRojasMon/analizador-lexile-chile/issues).

---

💙 Desarrollado para la educación en Chile 🇨🇱
