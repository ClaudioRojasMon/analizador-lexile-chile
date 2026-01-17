# 📁 Carpeta de Datos

Esta carpeta está destinada para almacenar tus archivos de texto y PDF que desees analizar.

## 📄 Tipos de Archivos Soportados

- **PDF** (`.pdf`) - Documentos, libros, artículos
- **Texto plano** (`.txt`) - Archivos de texto simple
- **Markdown** (`.md`) - Archivos con formato markdown
- Cualquier archivo de texto con encoding UTF-8 o Latin-1

## 🎯 Cómo Usar Esta Carpeta

### Opción 1: Colocar Archivos Aquí

```bash
# Copiar tus archivos a esta carpeta
cp mi_libro.pdf data/
cp mi_texto.txt data/

# Analizar desde código
python main.py --file data/mi_libro.pdf
```

### Opción 2: Usar Rutas Completas

```bash
# No necesitas copiar archivos aquí
python main.py --file /ruta/completa/a/tu/archivo.pdf
```

## 📚 Ejemplos de Organización

Puedes organizar tus archivos por categorías:

```
data/
├── libros_infantiles/
│   ├── cuento1.pdf
│   └── cuento2.txt
├── textos_escolares/
│   ├── 5basico_lenguaje.pdf
│   └── 7basico_ciencias.pdf
├── literatura/
│   ├── cien_años.pdf
│   └── cronica.txt
└── articulos/
    ├── ciencia1.pdf
    └── historia1.pdf
```

## ⚠️ Nota Importante

Los archivos en esta carpeta **NO se subirán a GitHub** por defecto (están en `.gitignore`). 

Esto es porque:
- Pueden ser archivos grandes
- Pueden contener material con derechos de autor
- Son específicos de cada usuario

## 💡 Tips

### Para Docentes
- Crea subcarpetas por grado: `1basico/`, `2basico/`, etc.
- Organiza por asignatura: `lenguaje/`, `ciencias/`, `historia/`
- Guarda textos de referencia para cada nivel

### Para Padres
- Crea carpeta por hijo: `maria/`, `juan/`
- Organiza por edad o nivel de lectura
- Mantén una carpeta `favoritos/` con textos apropiados

### Para Bibliotecas
- Organiza por rango Lexile estimado
- Mantén copias de textos analizados
- Crea índice de niveles encontrados

## 🔒 Privacidad

Si subes tu proyecto a GitHub y NO quieres compartir tus archivos:

El `.gitignore` ya está configurado para ignorar:
- `data/*.pdf`
- `data/*.txt`

Si quieres subir algunos archivos de ejemplo, cámbialos en `.gitignore`.

---

💡 **Recuerda:** Esta carpeta es tu espacio de trabajo personal. Organízala como prefieras.
