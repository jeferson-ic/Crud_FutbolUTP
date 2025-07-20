# ⚽ Fútbol UTP - Gestión de Jugadores

Este proyecto es una aplicación web desarrollada con **Flask** y **MySQL** que permite gestionar la información de los jugadores del equipo de fútbol de la **Universidad Tecnológica del Perú (UTP)**. Incluye funcionalidades CRUD completas, diseño con Bootstrap y secciones informativas como trofeos, historia y ubicación.

---

## 📌 Características Principales

- CRUD de jugadores (Crear, Leer, Actualizar, Eliminar)
- Subida de imágenes de los jugadores
- Sección de historia del equipo
- Trofeos ficticios con imágenes generadas por IA
- Video incrustado desde YouTube
- Mapa con ubicación de la universidad
- Interfaz moderna y responsiva con Bootstrap

---

## 🛠 Tecnologías Usadas

- **Lenguaje**: Python 3.11
- **Framework**: Flask
- **Base de Datos**: MySQL
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Gestión de Dependencias**: pip
- **Control de Versiones**: Git + GitHub

---

## 🧱 Estructura del Proyecto

futbol_utp/
│
├── app.py # Archivo principal con las rutas

├── static/

│ ├── styles.css # Estilos personalizados

│ └── uploads/ # Carpeta donde se guardan las imágenes

├── templates/

│ ├── layout.html # Plantilla base

│ ├── home.html # Página de inicio

│ ├── nosotros.html # Página informativa

│ └── jugadores/ # Carpeta con las vistas CRUD

│ ├── listar.html

│ ├── agregar.html

│ └── editar.html

├── config/

│ └── db.py # Conexión a la base de datos

├── static/

│ └── logo.png # Logo de la universidad

├── futbol_utp.sql # Script SQL con la base de datos

└── README.md # Documentación del proyecto

---

## 🧪 ¿Cómo Ejecutarlo?

### 1. Clonar el repositorio:

bash
git clone https://github.com/tu_usuario/futbol_utp.git
cd futbol_utp

### 2. Crear entorno virtual e instalar dependencias:
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt

### 3. Configurar la base de datos:
Crear una base de datos llamada futbol_utp en MySQL.

Importar el archivo futbol_utp.sql.
CREATE DATABASE futbol_utp;
USE futbol_utp;
-- Luego importar el .sql desde tu gestor (MySQL Workbench, phpMyAdmin, etc.)

### 4. Ejecutar el proyecto:
python app.py
Accede a: http://127.0.0.1:5000



## Autor:
Ronaldhiño Jefferson Inga Castillo - UTP - jefersoninga13@gmail.com

## Licencia
Este proyecto fue desarrollado con fines educativos como parte del curso Lenguaje de Programación (Docente: Pedro Hernán de la Cruz Velazco).
