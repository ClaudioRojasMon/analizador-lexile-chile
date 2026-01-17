# 📊 Carpeta de Resultados

Esta carpeta almacena los resultados de tus análisis cuando usas la opción `--output`.

## 📄 Tipos de Archivos

### Resultados de Análisis (`.txt`)
Contienen la información completa del análisis:
- Nivel Lexile
- Clasificación educativa
- Estadísticas del texto
- Métricas de complejidad

### Comparaciones (`.txt`)
Tablas comparativas de múltiples textos

### Reportes (opcional, futuras versiones)
- PDFs con gráficos
- Tablas Excel
- JSON para integración con otros sistemas

## 🎯 Cómo Guardar Resultados

### Desde Línea de Comandos

```bash
# Guardar resultado de un análisis
python main.py --file data/texto.txt --output outputs/resultado.txt

# Los resultados se guardarán automáticamente aquí
```

### Desde Python

```python
from src.utilidades import guardar_resultado

# Después de analizar
resultado = analizador.analizar(texto)

# Guardar
guardar_resultado(resultado, "outputs/mi_analisis.txt")
```

## 📁 Organización Sugerida

```
outputs/
├── por_grado/
│   ├── 1basico_resultados.txt
│   ├── 2basico_resultados.txt
│   └── 3basico_resultados.txt
├── comparaciones/
│   ├── libros_infantiles_comparacion.txt
│   └── textos_escolares_comparacion.txt
└── reportes_mensuales/
    ├── enero_2025.txt
    └── febrero_2025.txt
```

## 💡 Ejemplos de Uso

### Guardar Análisis Individual

```bash
python main.py --file "Cuento Infantil.pdf" --output "outputs/cuento_analisis.txt"
```

### Guardar Comparación

```python
from src.utilidades import comparar_textos

resultados = comparar_textos(mis_textos, analizador)

# Guardar la tabla en archivo
with open('outputs/comparacion.txt', 'w') as f:
    f.write(str(resultados))
```

### Crear Reporte de Biblioteca

```python
import os

# Analizar todos los libros
resultados_biblioteca = {}

for archivo in os.listdir('data/biblioteca/'):
    texto = cargar_documento(f'data/biblioteca/{archivo}')
    resultado = analizador.analizar(texto)
    resultados_biblioteca[archivo] = resultado

# Guardar reporte completo
with open('outputs/reporte_biblioteca.txt', 'w') as f:
    for libro, resultado in resultados_biblioteca.items():
        f.write(f"\n{libro}: {resultado['lexile']}L - {resultado['grado']}\n")
```

## ⚠️ Nota sobre Git

Los archivos `.txt` en esta carpeta están configurados para NO subirse a GitHub por defecto.

Si quieres compartir algunos resultados:
1. Edita `.gitignore`
2. Elimina la línea `outputs/*.txt`
3. Commit los archivos que quieras compartir

## 🔄 Limpieza

Para mantener esta carpeta organizada:

```bash
# Borrar todos los resultados antiguos
rm outputs/*.txt

# O crear script de limpieza
python scripts/limpiar_outputs.py  # (si lo creas)
```

## 📈 Análisis de Tendencias (Avanzado)

Puedes usar los resultados guardados para analizar tendencias:

```python
import os
import re

# Leer todos los resultados
niveles = []
for archivo in os.listdir('outputs/'):
    with open(f'outputs/{archivo}', 'r') as f:
        contenido = f.read()
        # Extraer nivel Lexile
        match = re.search(r'(\d+)L', contenido)
        if match:
            niveles.append(int(match.group(1)))

# Calcular estadísticas
promedio = sum(niveles) / len(niveles)
print(f"Nivel promedio de tu biblioteca: {promedio}L")
```

---

💡 **Tip:** Establece una rutina de análisis y guarda los resultados aquí para tener un registro histórico.
