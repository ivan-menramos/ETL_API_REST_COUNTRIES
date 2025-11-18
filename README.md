Proyecto ETL: Integración de datos desde API RestCountries hacia PostgreSQL

Desarrollé un pipeline ETL completo utilizando Python para extraer información de países desde la API pública RestCountries. Implementé un módulo de extracción con requests para obtener datos en formato JSON, seguido de un proceso de transformación que estructuró y limpió la información (capital, región, población, idiomas, moneda y densidad poblacional). Finalmente, construí un módulo de carga empleando SQLAlchemy para insertar los datos procesados en una tabla dentro de una base de datos PostgreSQL, gestionando credenciales mediante variables de entorno (.env).
El proceso permite consultar múltiples países, generar un DataFrame consolidado y almacenarlo de forma segura y escalable.

Tecnologías: Python, Pandas, Requests, SQLAlchemy, PostgreSQL, dotenv
Conceptos aplicados: ETL, APIs REST, JSON parsing, data cleaning, carga en base de datos, manejo de excepciones, diseño modular de pipelines.
