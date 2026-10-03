### Backend Lab

<p align="left">
  <img src="https://img.shields.io/badge/Raspberry%20Pi-Backend%20Lab-C51A4A" />
  <img src="https://img.shields.io/badge/Linux-Debian%20Based-blue" />
  <img src="https://img.shields.io/badge/Python-Hardware%20Dashboard-3776AB" />
  <img src="https://img.shields.io/badge/Docker-Compose-2496ED" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-336791" />
  <img src="https://img.shields.io/badge/Tailscale-Remote%20Access-242424" />
  <img src="https://img.shields.io/badge/Version-v0.3.0-blue" />
  <img src="https://img.shields.io/badge/Status-Active-success" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" />
</p>

Laboratorio personal de infraestructura backend construido sobre una Raspberry Pi.

Este proyecto documenta la configuración, despliegue, monitorización y mantenimiento de un entorno real utilizado para alojar aplicaciones backend desarrolladas en Python.

---

#### Objetivos

- Disponer de un entorno de despliegue propio.
- Practicar administración de sistemas Linux.
- Desplegar APIs utilizando Docker Compose.
- Gestionar bases de datos PostgreSQL.
- Implementar copias de seguridad automatizadas y verificables.
- Monitorizar el estado del sistema y de los servicios críticos.
- Acceder de forma segura mediante SSH y Tailscale.
- Automatizar servicios mediante systemd.
- Simular flujos de trabajo similares a entornos profesionales.

---

#### Stack Tecnológico

- Raspberry Pi
- Raspberry Pi OS Lite
- Linux
- Python
- Docker
- Docker Compose
- PostgreSQL
- Nginx
- Tailscale
- Git
- GitHub
- SSH
- systemd
- Pillow
- psutil
- PySerial

---

#### Arquitectura General

```text
          Laptop
            │
            │ Git / SSH
            ▼
       Backend Lab
            │
     ┌──────┼───────────────┐
     │      │               │
   Nginx  Docker        systemd
     │      │               │
     │   FastAPI            ├── Backups
     │      │               │
     │  PostgreSQL          └── Hardware Dashboard
     │                          │
     │                          ▼
     └───────────────────── USB Display
```

---

#### Componentes Configurados

##### Sistema Base

- Raspberry Pi OS Lite.
- Acceso remoto mediante SSH.
- Actualizaciones y mantenimiento del sistema.
- Zona horaria configurada en `Europe/Madrid`.
- Servicios gestionados mediante systemd.

##### Contenedores

- Docker Engine.
- Docker Compose.
- Gestión de imágenes y contenedores.
- Healthchecks para servicios contenerizados.

##### Bases de Datos

- PostgreSQL en contenedor.
- Volúmenes persistentes.
- Healthchecks.
- Backups mediante `pg_dump`.
- Validación mediante `pg_restore`.
- Retención automática de los dos backups más recientes.
- Backup automático durante apagados y reinicios mediante systemd.
- Registro explícito del resultado de la última copia de seguridad.

##### Redes y Acceso

- Red local.
- Tailscale.
- Acceso remoto seguro sin apertura de puertos.
- Nginx como reverse proxy.

##### Hardware Dashboard

Dashboard físico desarrollado en Python para monitorizar externamente el estado de Backend Lab mediante una pantalla USB de 3.5".

Actualmente muestra:

- Uso de CPU.
- Uso de RAM.
- Uso de disco.
- Temperatura de la CPU.
- Uptime.
- Estado de Nginx.
- Estado de Docker.
- Estado de PostgreSQL.
- Resultado del último backup.

La información se actualiza automáticamente cada 5 segundos.

El dashboard genera completamente la interfaz mediante Pillow y utiliza `turing-smart-screen-python` únicamente como capa de comunicación de bajo nivel con la pantalla.

El proceso se ejecuta mediante `systemd` y arranca automáticamente junto con la Raspberry Pi.

La documentación específica del componente se encuentra en:

- [Hardware Dashboard](dashboard/README.md)

---

#### Documentación

- [Configuración inicial Raspberry Pi](docs/01-raspberry-setup.md)
- [Seguridad y SSH](docs/02-ssh-security.md)
- [Docker Compose](docs/03-docker-compose.md)
- [PostgreSQL](docs/04-postgresql.md)
- [Tailscale](docs/05-tailscale.md)
- [Mantenimiento](docs/06-maintenance.md)
- [Backups de PostgreSQL](docs/07-postgresql-backups.md)
- [Hardware Dashboard](dashboard/README.md)

---

#### Aprendizajes

Este laboratorio se utiliza para consolidar conocimientos relacionados con:

- Linux.
- Redes.
- Docker.
- Bases de datos.
- Backups y restauración de datos.
- systemd.
- Despliegue de aplicaciones.
- Administración de servidores.
- Monitorización de sistemas.
- Dispositivos USB en Linux.
- Permisos y grupos del sistema.
- Integración de hardware mediante Python.

---

#### Estado

Proyecto activo y en evolución continua.

Backend Lab funciona actualmente como un entorno real de pruebas, despliegue y monitorización sobre Raspberry Pi.

---

#### Roadmap

- [x] Raspberry Pi Setup
- [x] SSH Administration
- [x] Docker Compose
- [x] PostgreSQL
- [x] Tailscale
- [x] Maintenance
- [x] Automated Backups
- [x] Reverse Proxy (Nginx)
- [x] Hardware Monitoring Dashboard
- [x] Automatic Dashboard Startup with systemd
- [ ] Advanced Monitoring
- [ ] Alerting