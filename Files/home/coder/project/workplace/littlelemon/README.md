# 🍋 Little Lemon Restaurant - Proyecto Django

## Descripción del Proyecto

Little Lemon es una aplicación web desarrollada en Django que simula el sitio web de un restaurante mediterráneo. El proyecto permite a los usuarios navegar por las diferentes páginas del restaurante, explorar el menú con elementos ordenados alfabéticamente, y acceder a información detallada sobre cada plato.

## 🎯 Funcionalidades Implementadas

### Páginas Web
- **Página Principal** (`/`): Página de bienvenida con información del restaurante
- **Acerca de** (`/about/`): Información detallada sobre la historia y filosofía del restaurante
- **Menú** (`/menu/`): Lista completa de elementos del menú ordenados alfabéticamente
- **Elementos Individuales** (`/menu_item/<id>/`): Páginas detalladas para cada plato del menú
- **Reservar** (`/book/`): Información para hacer reservas

### Características Técnicas
- ✅ Navegación completa entre todas las páginas
- ✅ Elementos del menú ordenados alfabéticamente
- ✅ Precios mostrados para cada elemento
- ✅ Enlaces clicables a páginas individuales de cada plato
- ✅ Pie de página incluido en todas las páginas
- ✅ Diseño responsive y moderno
- ✅ Panel de administración para gestionar elementos del menú
- ✅ Base de datos SQLite para almacenar información

## 🏗️ Estructura del Proyecto

```
littlelemon/
├── littlelemon/                 # Configuración del proyecto Django
│   ├── __init__.py
│   ├── settings.py             # Configuración de la aplicación
│   ├── urls.py                 # URLs principales del proyecto
│   ├── wsgi.py
│   └── asgi.py
├── restaurant/                  # Aplicación principal
│   ├── __init__.py
│   ├── models.py               # Modelo MenuItem
│   ├── views.py                # Vistas de las páginas
│   ├── urls.py                 # URLs de la aplicación
│   ├── admin.py                # Configuración del panel de administración
│   └── apps.py
├── templates/                   # Plantillas HTML
│   ├── base.html               # Plantilla base con navegación y pie de página
│   ├── home.html               # Página principal
│   ├── about.html              # Página "Acerca de"
│   ├── menu.html               # Página del menú
│   ├── menu_item.html          # Página individual de cada plato
│   └── book.html               # Página de reservas
├── db.sqlite3                  # Base de datos SQLite
├── manage.py                   # Script de gestión de Django
└── README.md                   # Este archivo
```

## 🚀 Cómo Arrancar el Proyecto

### Prerrequisitos
- Python 3.8 o superior
- Django 4.2.5 (se instalará automáticamente)

### Pasos para Ejecutar

1. **Navegar al directorio del proyecto:**
   ```bash
   cd Files/home/coder/project/workplace/littlelemon
   ```

2. **Instalar dependencias (si es necesario):**
   ```bash
   pip install django
   ```

3. **Aplicar migraciones de la base de datos:**
   ```bash
   python manage.py migrate
   ```

4. **Crear un superusuario (opcional, ya existe uno):**
   ```bash
   python manage.py createsuperuser
   ```
   - Usuario existente: `admin`
   - Contraseña: `admin123`

5. **Arrancar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

6. **Acceder a la aplicación:**
   - Abrir el navegador en: http://127.0.0.1:8000/

## 🌐 URLs Disponibles

| URL | Descripción |
|-----|-------------|
| `/` | Página principal con bienvenida |
| `/about/` | Información sobre el restaurante |
| `/menu/` | Lista de elementos del menú |
| `/menu_item/<id>/` | Página individual de cada plato |
| `/book/` | Información para reservas |
| `/admin/` | Panel de administración |

## 🍽️ Elementos del Menú Incluidos

El proyecto incluye 8 elementos de menú de ejemplo:

1. **Bruschetta Clásica** - $8.50
2. **Ensalada Mediterránea** - $9.99
3. **Gelato de Limón** - $6.50
4. **Lasaña de Vegetales** - $15.25
5. **Pasta Carbonara** - $14.50
6. **Pizza Margherita** - $12.99
7. **Risotto de Hongos** - $16.75
8. **Tiramisú** - $7.99

## 🔧 Gestión del Menú

### Panel de Administración
- URL: http://127.0.0.1:8000/admin/
- Usuario: `admin`
- Contraseña: `admin123`

### Agregar Nuevos Elementos
1. Acceder al panel de administración
2. Ir a "Restaurant" > "Menu items"
3. Hacer clic en "Add Menu item"
4. Completar los campos:
   - **Name**: Nombre del plato
   - **Price**: Precio (formato decimal)
   - **Description**: Descripción detallada
   - **Image**: Imagen del plato (opcional)

### Editar Elementos Existentes
1. En el panel de administración, seleccionar el elemento a editar
2. Modificar los campos necesarios
3. Guardar los cambios

## 🎨 Características del Diseño

- **Responsive**: Se adapta a diferentes tamaños de pantalla
- **Navegación Intuitiva**: Menú principal con enlaces a todas las páginas
- **Diseño Moderno**: Colores y tipografías profesionales
- **Experiencia de Usuario**: Transiciones suaves y hover effects
- **Accesibilidad**: Estructura semántica HTML

## 📋 Criterios de Evaluación Cumplidos

- ✅ Página de inicio con enlace que carga la página del menú
- ✅ Página del menú contiene una lista de elementos del menú
- ✅ Elementos del menú se muestran en orden alfabético
- ✅ Elementos del menú se muestran con su precio asociado
- ✅ Se puede hacer clic en los elementos del menú para navegar a páginas individuales
- ✅ Página del menú presenta toda la información sobre el mismo
- ✅ Contiene una sección de pie de página

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 4.2.5
- **Base de Datos**: SQLite3
- **Frontend**: HTML5, CSS3
- **Lenguaje**: Python 3.11+

## 📝 Notas Adicionales

- El proyecto está configurado para desarrollo local
- La base de datos SQLite se crea automáticamente
- Los archivos estáticos (CSS) están incluidos en los templates
- El proyecto es completamente funcional y listo para revisión por pares

## 🚨 Solución de Problemas

### Error: "No such file or directory"
- Asegúrate de estar en el directorio correcto: `Files/home/coder/project/workplace/littlelemon`

### Error: "Module not found"
- Instala Django: `pip install django`

### Error: "Database is locked"
- Detén el servidor (Ctrl+C) y vuelve a ejecutarlo

### El servidor no arranca
- Verifica que el puerto 8000 esté disponible
- Usa un puerto diferente: `python manage.py runserver 8080`

---

**Desarrollado para el curso de Django de Meta en Coursera** 🎓
