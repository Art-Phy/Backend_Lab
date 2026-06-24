
### Backend Lab

<p align="left">
  <img src="https://img.shields.io/badge/Raspberry%20Pi-Backend%20Lab-C51A4A" />
  <img src="https://img.shields.io/badge/Linux-Debian%20Based-blue" />
  <img src="https://img.shields.io/badge/Docker-Compose-2496ED" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-336791" />
  <img src="https://img.shields.io/badge/Tailscale-Remote%20Access-242424" />
  <img src="https://img.shields.io/badge/Status-Active-success" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" />
</p>

Laboratorio personal de infraestructura backend construido sobre una Raspberry Pi.

Este proyecto documenta la configuración, despliegue y mantenimiento de un entorno real utilizado para alojar aplicaciones backend desarrolladas en Python.

---

#### Objetivos

- Disponer de un entorno de despliegue propio.
- Practicar administración básica de sistemas Linux.
- Desplegar APIs utilizando Docker Compose.
- Gestionar bases de datos PostgreSQL.
- Acceder de forma segura mediante SSH y Tailscale.
- Simular flujos de trabajo similares a entornos profesionales.

---

#### Stack Tecnológico

- Raspberry Pi
- Raspberry Pi OS Lite
- Linux
- Docker
- Docker Compose
- PostgreSQL
- Nginx
- Tailscale
- Git
- GitHub
- SSH

---

#### Arquitectura General

```
      Laptop
        │
        │ GitHub
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

#### Componentes Configurados

##### Sistema Base

- Raspberry Pi OS Lite
- Acceso remoto mediante SSH
- Actualizaciones y mantenimiento del sistema

##### Contenedores

- Docker Engine
- Docker Compose
- Gestión de imágenes y contenedores

##### Bases de Datos

- PostgreSQL en contenedor
- Volúmenes persistentes
- Healthchecks

##### Redes y Acceso

- Red local
- Tailscale
- Acceso remoto seguro sin apertura de puertos

---

#### Documentación

- [Configuración inicial Raspberry Pi](docs/01-raspberry-setup.md)
- [Seguridad y SSH](docs/02-ssh-security.md)
- [Docker Compose](docs/03-docker-compose.md)
- [PostgreSQL](docs/04-postgresql.md)
- [Tailscale](docs/05-tailscale.md)
- [Mantenimiento](docs/06-maintenance.md)

---

#### Aprendizajes

Este laboratorio se utiliza para consolidar conocimientos relacionados con:

- Linux
- Redes
- Docker
- Bases de datos
- Despliegue de aplicaciones
- Administración de servidores

---

#### Estado

Proyecto activo y en evolución continua.

---

#### Roadmap

- [x] Raspberry Pi Setup
- [x] SSH Administration
- [x] Docker Compose
- [x] PostgreSQL
- [x] Tailscale
- [x] Maintenance
- [ ] Reverse Proxy (Nginx)
- [ ] Monitoring
- [ ] Automated Backups