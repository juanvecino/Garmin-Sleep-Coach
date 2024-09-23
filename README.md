## **Sleep Coach Application**

### **Descripción**
Esta es una aplicación de coaching de sueño que permite a los usuarios conectar sus datos de **Garmin** y generar análisis de su sueño, además de ofrecer predicciones personalizadas y recomendaciones basadas en datos históricos. Los usuarios pueden visualizar gráficos interactivos con métricas como horas de sueño, calidad del sueño y estrés. 

### **Tecnologías Usadas**
- **Backend**: [Django](https://www.djangoproject.com/) con [Django Rest Framework](https://www.django-rest-framework.org/) para construir la API y manejar las credenciales y datos de Garmin.
- **Frontend**: [React](https://reactjs.org/) para crear una interfaz interactiva y visualización de datos usando [Plotly](https://plotly.com/react/).
- **Base de Datos**: Usaremos PostgreSQL para almacenar datos de usuarios y registros de sueño.
- **Integración con Garmin**: Se utiliza el script [garmin_db](https://github.com/cyberjunky/garminconnect) para obtener los datos de Garmin.
- **Despliegue**:
  - **Backend**: Desplegado en [Heroku](https://www.heroku.com/).
  - **Frontend**: Desplegado en [Netlify](https://www.netlify.com/).

### **Estructura del Proyecto**
```bash
my_project/
│
├── backend/                     # Carpeta del backend (Django)
│   ├── garmin_db/               # Script garmin_db (para extraer datos de Garmin)
│   ├── my_project/              # Configuración del proyecto Django
│   │   ├── settings.py          # Configuración del proyecto (bases de datos, API keys, etc.)
│   │   └── urls.py              # Rutas principales del proyecto
│   ├── api/                     # Aplicación API de Django
│   │   ├── models.py            # Modelos de base de datos (credenciales, datos de sueño)
│   │   ├── views.py             # Vistas para manejar la lógica de API y acceso a Garmin
│   │   ├── urls.py              # Rutas API (endpoints)
│   └── manage.py                # Comando principal de Django
│
├── frontend/                    # Carpeta del frontend (React)
│   ├── public/                  # Archivos estáticos (HTML)
│   ├── src/                     # Código fuente de React
│   │   ├── components/          # Componentes de React (formularios, gráficos, etc.)
│   │   ├── pages/               # Páginas del frontend
│   │   └── App.js               # Componente principal de React
│   └── package.json             # Dependencias de React
│
├── docker-compose.yml           # Configuración de Docker para levantar backend y frontend
├── Dockerfile                   # Dockerfile para el backend (Django)
├── Dockerfile.react             # Dockerfile para el frontend (React)
├── README.md                    # Este archivo
└── requirements.txt             # Dependencias del backend (Django)
```


### **Características de la Aplicación**
1. **Registro de Usuarios**: Los usuarios pueden registrarse e ingresar sus credenciales de Garmin.
2. **Visualización de Datos**: La aplicación extrae datos de Garmin, como horas de sueño, fases de sueño (profundo, ligero), y estrés, y los muestra en gráficos interactivos.
3. **Predicciones**: Usamos modelos de machine learning para predecir la calidad del sueño y ofrecer recomendaciones personalizadas basadas en el historial de datos.
4. **Recomendaciones NLP**: La app genera recomendaciones basadas en el análisis de datos usando procesamiento de lenguaje natural (NLP).

---