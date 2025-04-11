# Asistente Baty con OpenAI y Chainlit

Este repositorio contiene un asistente virtual diseñado para ayudar en tareas comunes al sistema de Batuta desarrollado por Metabase Q, aprovechando los servicios de OpenAI y la plataforma LiteralAI. El asistente está configurado para utilizar APIs de ambas plataformas para el procesamiento y generación de respuestas.

## Requisitos previos

- Python 3.8+
- Una cuenta de OpenAI con claves API
- Docker (opcional para la ejecución en un contenedor)

## Configuración

### Variables de Entorno

Antes de ejecutar el proyecto, asegúrate de tener configuradas las siguientes variables de entorno:

- **`OPENAI_API_KEY`**: Clave API de OpenAI.
- **`ASSISTANT_ID`**: ID del asistente de OpenAI.
- **`LITERAL_API_KEY`**: Clave API de LiteralAI.

Puedes agregar estas variables en tu entorno local o en un archivo `.env`.

### Instalación

1. Clona el repositorio:

```bash
git clone <url-del-repositorio>
cd <nombre-del-repositorio>
```

## Instalación

Instala las dependencias:
```bash
pipenv install
```

### Ejecutar el asistente
```bash
pipenv shell
chainlit run main.py -w
```

### APIKEYS
- Generar una api key en openai
- Generar una api key en LiteralAI
