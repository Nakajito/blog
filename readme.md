# ✍️ Reflex Blog Pro

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Reflex](https://img.shields.io/badge/Reflex-Framework-black?style=for-the-badge&logo=reflex)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> Un sistema de gestión de contenidos (CMS) y blog moderno, minimalista y de alto rendimiento, construido 100% en Python utilizando el framework [Reflex](https://reflex.dev/).

## 📖 Descripción

Este proyecto es una demostración de cómo construir una aplicación web full-stack orientada al contenido sin escribir una sola línea de JavaScript. **Reflex Blog Pro** ofrece una experiencia de lectura limpia, soporte para Markdown avanzado con resaltado de sintaxis y una arquitectura optimizada para SEO.

Es ideal para desarrolladores que quieren su propio blog personalizable o como base para documentaciones técnicas.

## ✨ Características Principales

* 📝 **Renderizado Markdown:** Escribe tus posts en Markdown estándar y visualízalos con estilos ricos.
* 🎨 **Syntax Highlighting:** Bloques de código con colores automáticos (ideal para blogs técnicos).
* 📱 **Diseño Responsivo:** UI adaptable a móviles, tablets y escritorio.
* 🔍 **SEO Optimizado:** Generación dinámica de metatags (título, descripción, imagen OG) para cada artículo.
* 🏷️ **Sistema de Categorías/Tags:** Organización eficiente del contenido.
* 🌗 **Modo Oscuro/Claro:** Cambio de tema nativo integrado.
* ⚡ **Backend Integrado:** Base de datos gestionada con SQLModel (SQLAlchemy).

## 📸 Capturas de Pantalla

*(Coloca aquí capturas de tu blog. Ejemplo: Home, Vista de Artículo, Mobile)*

| Home Page | Vista de Artículo |
|:---:|:---:|
| ![Home](https://via.placeholder.com/400x250?text=Home+Page) | ![Article](https://via.placeholder.com/400x250?text=Article+View) |

## 🛠️ Stack Tecnológico

* **Framework:** [Reflex](https://reflex.dev/)
* **Lenguaje:** Python 3.10+
* **Base de Datos:** SQLite (Desarrollo) / PostgreSQL (Producción)
* **ORM:** SQLModel
* **Estilos:** Reflex UI (basado en Radix UI)
* **Procesamiento de Texto:** `markdown`, `pygments`

## 🚀 Instalación y Configuración

Sigue estos pasos para levantar el proyecto en tu entorno local.

### 1. Prerrequisitos

* Python 3.8 o superior.
* Git.

### 2. Clonar el Repositorio

```bash
git clone https://github.com/Nakajito/blog
cd blog
```

### 3. Entorno Virtual
Se recomienda encarecidamente usar un entorno virtual.

```Bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

### 4. Instalar Dependencias

```Bash
pip install -r requirements.txt
```

### 5. Inicializar Base de Datos y App

Inicializa Reflex (descargará el backend de Node.js necesario y configurará la DB).

```Bash
reflex init
```
Aplica las migraciones de base de datos (si usas modelos personalizados):

```Bash
reflex db migrate
```

### 6. Ejecutar en Desarrollo
```Bash
reflex run
```
La aplicación estará disponible en: http://localhost:3000

📂 Estructura del Proyecto
```Plaintext

blog/
├── .venv/                  # Entorno virtual (ignorado en git)
├── .gitignore              # Archivos que git debe ignorar
├── assets/                 # Imágenes, favicons, fuentes locales
│   ├── img/
│   └── fonts/
├── rxconfig.py             # Configuración principal (nombre app, puerto, DB)
├── blog/                   # CÓDIGO FUENTE PRINCIPAL
│   ├── __init__.py
│   ├── blog.py             # Punto de entrada (Entry point)
│   ├── components/         # Piezas de UI reutilizables
│   │   ├── __init__.py
│   │   ├── navbar.py       # Barra de navegación
│   │   ├── footer.py       # Pie de página
│   │   └── post_card.py    # Tarjeta de resumen del post
│   ├── models/             # Definición de Tablas (Base de Datos)
│   │   ├── __init__.py
│   │   └── post.py         # Modelos User, Post, Tag
│   ├── pages/              # Rutas de la web (Vistas)
│   │   ├── __init__.py
│   │   ├── index.py        # Página de inicio
│   │   ├── detail.py       # Lectura del artículo
│   │   └── dashboard.py    # Panel de admin
│   ├── state/              # Lógica del Backend (Eventos y Estado)
│   │   ├── __init__.py
│   │   ├── base.py         # Estado base (usuario logueado, configuración)
│   │   └── post_state.py   # Lógica para cargar/guardar posts
│   ├── styles/             # Estilos globales y fuentes
│   │   ├── __init__.py
│   │   └── styles.py       # Diccionarios de estilo y temas
│   └── utils/              # Funciones auxiliares
│       └── auth.py         # Lógica de seguridad/hashing
└── requirements.txt        # Lista de dependencias (pip freeze > requirements.txt)
```
### 📝 Gestión de Contenido
Actualmente, los artículos se gestionan a través de Base de Datos.

Para agregar un post: ingresa a la URL /admin.

### 🌍 Despliegue (Deploy)
Este proyecto está listo para ser desplegado utilizando Reflex Cloud o contenedores Docker.

#### Opción A: Reflex Cloud (Recomendado)
```Bash
reflex deploy
```

#### Opción B: Docker
Construye la imagen:

```Bash
docker build -t blog.
docker run -p 3000:3000 blog
```

### 🤝 Contribución
¡Las contribuciones son bienvenidas!

1. Haz un Fork del proyecto.

2. Crea una rama (git checkout -b feature/AmazingFeature).

3. Haz Commit de tus cambios (git commit -m 'Add some AmazingFeature').

4. Haz Push a la rama (git push origin feature/AmazingFeature).

5. Abre un Pull Request.

### 📄 Licencia
Distribuido bajo la licencia MIT. Ver LICENSE para más información.

Construido con ❤️ usando Reflex.