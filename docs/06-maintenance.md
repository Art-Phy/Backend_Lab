
### Mantenimiento y Operaciones

#### Objetivo

Una vez desplegados los distintos componentes de Backend Lab, resulta fundamental establecer procedimientos básicos de mantenimiento para garantizar la estabilidad y disponibilidad del entorno.

Este documento recopila las tareas habituales realizadas sobre el laboratorio.

---

#### Actualización del Sistema

Periódicamente se actualizan los paquetes del sistema operativo para incorporar mejoras de seguridad y estabilidad.

```bash
sudo apt update
sudo apt upgrade -y
```

Tras determinadas actualizaciones puede ser recomendable reiniciar el servidor.

```bash
sudo reboot
```

---

#### Supervisión de Servicios

La comprobación periódica del estado de los servicios permite detectar incidencias antes de que afecten al funcionamiento del laboratorio.

Verificación de contenedores Docker:

```bash
docker ps
```

Verificación de servicios Docker Compose:

```bash
docker compose ps
```

Consulta de logs:

```bash
docker compose logs
```

---

#### Gestión de Despliegues

El flujo habitual de despliegue sigue el siguiente proceso:

```text
Desarrollo Local
        │
        ▼
GitHub
        │
        ▼
Backend Lab
```

Una vez actualizada la rama principal:

```bash
git pull
```

Reconstrucción y despliegue:

```bash
docker compose up -d --build
```

---

#### Comprobación de Conectividad

Verificación del acceso remoto mediante Tailscale:

```bash
tailscale status
```

Verificación de conectividad general:

```bash
ping 8.8.8.8
```

Verificación de red:

```bash
ip addr
```

---

#### Supervisión de Almacenamiento

Comprobación del espacio disponible:

```bash
df -h
```

Consulta del uso de Docker:

```bash
docker system df
```

La supervisión periódica ayuda a evitar problemas derivados del crecimiento de imágenes, volúmenes o registros.

---

#### Limpieza de Recursos

Eliminación de imágenes no utilizadas:

```bash
docker image prune
```

Eliminación de recursos no utilizados:

```bash
docker system prune
```

Estas operaciones deben realizarse con precaución.

---

#### Resolución de Incidencias

Algunas herramientas habituales de diagnóstico son:

```bash
docker logs <container>
```

```bash
journalctl -xe
```

```bash
systemctl status <service>
```

```bash
docker compose logs
```

Estas utilidades permiten identificar errores relacionados con servicios, contenedores o conectividad.

---

#### Buenas Prácticas

Durante la administración de Backend Lab se siguen varias recomendaciones:

- Mantener el sistema actualizado.
- Evitar modificaciones directas en producción siempre que sea posible.
- Probar los cambios previamente en entorno local.
- Utilizar Git para controlar todas las modificaciones.
- Mantener la documentación actualizada.
- Revisar periódicamente el estado de Docker y PostgreSQL.

---

#### Resultado

Backend Lab dispone de una serie de procedimientos básicos de mantenimiento que permiten administrar el entorno de forma segura y predecible.

Estas tareas garantizan la estabilidad del laboratorio y facilitan la evolución futura de la infraestructura.