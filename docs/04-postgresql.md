
### PostgreSQL

#### Objetivo

Una vez establecido Docker Compose como mecanismo principal de despliegue, el siguiente paso consistió en incorporar una base de datos relacional persistente para alojar la información de las aplicaciones desplegadas en Backend Lab.

La tecnología elegida fue PostgreSQL.

---

#### ¿Por qué PostgreSQL?

PostgreSQL es una de las bases de datos relacionales más utilizadas en entornos profesionales.

Entre sus principales ventajas destacan:

- Software libre y de código abierto.
- Alto nivel de fiabilidad.
- Excelente integración con Python y SQLAlchemy.
- Amplio soporte en entornos Docker.
- Escalabilidad y rendimiento.

---

#### Despliegue mediante Docker

PostgreSQL se ejecuta dentro de un contenedor Docker gestionado por Docker Compose.

Este enfoque permite:

- Simplificar la instalación.
- Aislar la base de datos del sistema operativo.
- Facilitar actualizaciones.
- Mantener una configuración reproducible.

---

#### Persistencia de Datos

Uno de los aspectos más importantes fue la incorporación de volúmenes persistentes.

Sin persistencia, los datos almacenados en la base de datos se perderían al eliminar el contenedor.

```text
PostgreSQL
      │
      ▼
Volumen Persistente
```

---

#### Healthchecks

Backend Lab utiliza healthchecks para verificar automáticamente el estado de PostgreSQL.

Esto permite asegurar que la base de datos se encuentra disponible antes de que otros servicios intenten conectarse a ella.

---

#### Integración con Aplicaciones Backend

Las aplicaciones desplegadas utilizan PostgreSQL como sistema principal de almacenamiento.

```text
FastAPI
   │
   ▼
PostgreSQL
```

---

#### Beneficios Obtenidos

La incorporación de PostgreSQL permitió:

- Disponer de almacenamiento persistente.
- Separar claramente aplicación y base de datos.
- Acercar el entorno a escenarios reales de producción.
- Facilitar el uso de ORM como SQLAlchemy.
- Gestionar datos de forma fiable y estructurada.

---

#### Resultado

PostgreSQL se convirtió en el componente principal de almacenamiento dentro de Backend Lab.

Su integración mediante Docker Compose, junto con volúmenes persistentes y healthchecks, permitió construir una base sólida para desplegar aplicaciones backend con una arquitectura más cercana a entornos profesionales.