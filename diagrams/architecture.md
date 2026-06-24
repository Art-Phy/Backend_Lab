
### Arquitectura de Backend Lab

#### Visión General

Backend Lab es un laboratorio personal de infraestructura backend construido sobre una Raspberry Pi.

Su objetivo es proporcionar un entorno controlado para desplegar, mantener y administrar aplicaciones backend desarrolladas en Python utilizando tecnologías modernas de contenedorización y acceso remoto.

---

#### Arquitectura General

```text
     Laptop
        │
        │ Git / GitHub
        ▼
   Backend Lab
        │
 ┌──────┴──────┐
 │             │
Docker      PostgreSQL
 │
FastAPI
```

---

#### Flujo de Desarrollo

El desarrollo se realiza localmente en un entorno independiente.

```text
Desarrollo Local
        │
        ▼
GitHub
        │
        ▼
Backend Lab
```

Los cambios son desarrollados, probados y validados antes de ser desplegados en el servidor.

---

#### Componentes Principales

##### Raspberry Pi

Actúa como servidor principal del laboratorio.

**Responsabilidades:**

- Hospedar aplicaciones backend.
- Ejecutar contenedores Docker.
- Almacenar datos persistentes.
- Permitir acceso remoto seguro.

---

#### Docker Compose

Gestiona la ejecución coordinada de servicios.

**Responsabilidades:**

- Despliegue de aplicaciones.
- Gestión de redes internas.
- Gestión de volúmenes persistentes.
- Coordinación de múltiples contenedores.

---

#### PostgreSQL

Sistema principal de almacenamiento de datos.

**Responsabilidades:**

- Persistencia de información.
- Gestión de bases de datos relacionales.
- Soporte para aplicaciones desplegadas.

---

#### Tailscale

Proporciona acceso remoto privado al laboratorio.

**Responsabilidades:**

- Acceso seguro desde cualquier ubicación.
- Eliminación de dependencias de configuración de router.
- Comunicación cifrada entre dispositivos autorizados.

---

#### GitHub

Repositorio central de código y documentación.

**Responsabilidades:**

- Control de versiones.
- Gestión de cambios.
- Fuente oficial de los proyectos desplegados.

---

#### Filosofía del Proyecto

Backend Lab sigue una separación clara entre desarrollo y despliegue.

```text
 Laptop
      │
      ▼
Desarrollo
```

```text
GitHub
      │
      ▼
Control de Versiones
```

```text
Backend Lab
      │
      ▼
Despliegue
```

El servidor no se utiliza como entorno principal de desarrollo, sino como plataforma de ejecución y validación de aplicaciones.

---

#### Estado Actual

Actualmente Backend Lab proporciona:

- Servidor Linux dedicado.
- Acceso remoto mediante SSH.
- Red privada mediante Tailscale.
- Contenedorización mediante Docker Compose.
- Bases de datos PostgreSQL.
- Infraestructura preparada para alojar múltiples proyectos backend.

---

#### Próximos Pasos

- Reverse Proxy con Nginx.
- Monitorización básica.
- Automatización de despliegues.
- Copias de seguridad.
- Nuevos servicios desplegados mediante Docker Compose.