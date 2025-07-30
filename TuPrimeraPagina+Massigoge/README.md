# TuPrimeraPaginaMassigoge

## Cómo probar la app

1. Crear entorno virtual:
   ```bash
   python -m venv env
   source env/bin/activate  # o env\Scripts\activate en Windows
   pip install django
   ```

2. Migraciones y servidor:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

3. Acceder a:
   - `/` → Página principal
   - `/autor/` → Agregar autor
   - `/categoria/` → Agregar categoría
   - `/post/` → Agregar post
   - `/buscar/` → Buscar posts por título