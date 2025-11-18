# Proyecto ETL: Integración de datos desde API RestCountries hacia PostgreSQL

Desarrollé un pipeline ETL completo utilizando Python para extraer información de países desde la API pública RestCountries. Implementé un módulo de extracción con requests para obtener datos en formato JSON, seguido de un proceso de transformación que estructuró y limpió la información (capital, región, población, idiomas, moneda y densidad poblacional). Finalmente, construí un módulo de carga empleando SQLAlchemy para insertar los datos procesados en una tabla dentro de una base de datos PostgreSQL, gestionando credenciales mediante variables de entorno (.env).
El proceso permite consultar múltiples países, generar un DataFrame consolidado y almacenarlo de forma segura y escalable.

## Tecnologías
Python, Pandas, Requests, SQLAlchemy, PostgreSQL, dotenv

## Conceptos aplicados
ETL, APIs REST, JSON parsing, data cleaning, carga en base de datos, manejo de excepciones, diseño modular de pipelines.

---

## 1. Extracción (Extract)

Se utiliza requests para realizar una consulta a la API:
- Recibe el nombre de un país.
- Valida el código de respuesta.
- Retorna los datos en formato JSON.

---

## 2. Transformación (Transform)

La función de transformación:
- Toma la respuesta JSON (lista con datos del país).
- Limpia y estructura los campos principales.
- Genera un diccionario con información como:
  - nombre común
  - capital
  - región / subregión
  - población
  - área
  - idiomas
  - moneda
  - densidad poblacional

También incluye una función para procesar múltiples países y devolver un DataFrame consolidado.

---

## 3. Carga en PostgreSQL (Load)

Se utiliza SQLAlchemy para:
- Crear la conexión a PostgreSQL.
- Cargar el DataFrame en la tabla especificada.
- Manejar credenciales mediante .env.

