
### Docker Compose

#### Objetivo

Una vez preparado el servidor base y validado el acceso remoto mediante SSH, el siguiente paso consistió en simplificar el despliegue de aplicaciones backend.

Para ello se adoptó Docker Compose como herramienta principal de despliegue y gestión de servicios.

---

#### ¿Por qué Docker?

Docker permite empaquetar una aplicación junto con todas sus dependencias en una imagen reproducible.

Esto aporta varias ventajas:

- Entornos consistentes.
- Despliegues reproducibles.
- Aislamiento de servicios.
- Menor dependencia de la configuración del sistema operativo.

---

#### ¿Por qué Docker Compose?

Aunque Docker permite ejecutar contenedores individuales, muchas aplicaciones modernas dependen de varios servicios.

Por ejemplo:

```text
Aplicación Backend
        │
        ▼
PostgreSQL
```

Docker Compose permite definir toda la infraestructura necesaria mediante un único archivo.

---

#### Arquitectura

```text
Docker Compose
│
├── API Backend
└── PostgreSQL
```

---

#### Comandos Habituales

```bash
docker compose up -d --build
```

```bash
docker compose ps
```

```bash
docker compose logs
```

```bash
docker compose down
```

---

#### Resultado

Docker Compose se convirtió en la base del proceso de despliegue de Backend Lab.

Actualmente los servicios desplegados en el laboratorio utilizan contenedores para garantizar consistencia, aislamiento y facilidad de mantenimiento.