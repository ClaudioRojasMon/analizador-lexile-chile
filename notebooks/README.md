# 📓 Notebooks Jupyter

Esta carpeta contiene los notebooks Jupyter del proyecto.

## 📚 Notebooks Disponibles

### `Lexile.ipynb` (Original)
El notebook original de donde surgió este proyecto. Contiene:
- Exploración inicial del análisis Lexile
- Pruebas y experimentación
- Código que luego fue modularizado

**Uso:**
```bash
jupyter notebook notebooks/Lexile.ipynb
```

## 🎯 Cuándo Usar Notebooks vs Scripts

### Usa Notebooks Cuando:
- ✅ Estés experimentando con nuevas ideas
- ✅ Quieras visualizar resultados interactivamente
- ✅ Necesites hacer análisis exploratorios
- ✅ Estés aprendiendo cómo funciona el sistema

### Usa Scripts (`main.py`, `examples.py`) Cuando:
- ✅ Necesites analizar muchos archivos
- ✅ Quieras automatizar procesos
- ✅ El análisis sea repetitivo
- ✅ Necesites integrar con otros sistemas

## 🚀 Empezar con Jupyter

### Instalación

```bash
# Si no tienes Jupyter
pip install jupyter

# O si ya instalaste requirements.txt, ya lo tienes
```

### Ejecutar Notebook

```bash
# Desde la raíz del proyecto
jupyter notebook

# O específicamente este notebook
jupyter notebook notebooks/Lexile.ipynb
```

### Uso en Google Colab

1. Sube `Lexile.ipynb` a Google Drive
2. Abre con Google Colab
3. Ejecuta las celdas (puede que necesites instalar bibliotecas primero)

```python
# En la primera celda de Colab
!pip install spacy
!python -m spacy download es_core_news_sm
!pip install PyPDF2 pdfplumber
```

## 📝 Crear Tus Propios Notebooks

Puedes crear notebooks adicionales para tus análisis:

```
notebooks/
├── Lexile.ipynb                 # Original
├── mis_experimentos.ipynb       # Tus pruebas
├── analisis_biblioteca.ipynb    # Análisis específico
└── visualizaciones.ipynb        # Gráficos y reportes
```

### Plantilla Básica

```python
# Celda 1: Imports
from src.analizador_lexile import AnalizadorLexileChile
from src.utilidades import cargar_documento

# Celda 2: Inicializar
analizador = AnalizadorLexileChile()

# Celda 3: Tu análisis
texto = "Tu texto aquí"
resultado = analizador.analizar(texto)
analizador.imprimir_resultado(resultado)
```

## 💡 Tips para Notebooks

### Organización de Celdas

```python
# 🔧 Celda de Configuración
import sys
sys.path.append('..')  # Acceder a src desde notebooks

# 📚 Celda de Imports
from src.analizador_lexile import AnalizadorLexileChile

# 🎯 Celda de Inicialización
analizador = AnalizadorLexileChile()

# 🔬 Celdas de Análisis
# ... tu código ...

# 📊 Celdas de Visualización
# ... gráficos ...
```

### Buenas Prácticas

1. **Documenta con Markdown**: Usa celdas de texto para explicar
2. **Una tarea por celda**: Mantén las celdas enfocadas
3. **Guarda frecuentemente**: `Ctrl+S` o `Cmd+S`
4. **Ejecuta en orden**: Kernel → Restart & Run All

## 🎨 Visualizaciones (Avanzado)

Puedes agregar visualizaciones en notebooks:

```python
import matplotlib.pyplot as plt

# Comparar niveles de varios textos
niveles = [resultado1['lexile'], resultado2['lexile'], resultado3['lexile']]
nombres = ['Texto 1', 'Texto 2', 'Texto 3']

plt.bar(nombres, niveles)
plt.ylabel('Nivel Lexile')
plt.title('Comparación de Textos')
plt.show()
```

## 🔄 De Notebook a Script

Si tienes código útil en un notebook y quieres convertirlo en script:

```bash
# Convertir notebook a script Python
jupyter nbconvert --to script notebooks/Lexile.ipynb

# Esto crea Lexile.py
```

## ⚠️ Nota sobre Control de Versiones

Los notebooks pueden tener problemas con git porque incluyen outputs. 

Para limpiar outputs antes de commit:

```bash
# Limpiar outputs de un notebook
jupyter nbconvert --clear-output --inplace notebooks/Lexile.ipynb
```

O configurar git para ignorar cambios en outputs (avanzado).

## 📚 Recursos para Aprender Jupyter

- [Documentación oficial de Jupyter](https://jupyter.org/documentation)
- [Tutorial de Jupyter](https://jupyter-notebook.readthedocs.io/)
- [Jupyter en Google Colab](https://colab.research.google.com/)

---

💡 **Recuerda:** Los notebooks son excelentes para explorar y aprender, pero para producción es mejor usar los scripts modulares en `src/`.
