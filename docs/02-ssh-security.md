
### Seguridad y Acceso SSH

#### Objetivo

Una vez completada la instalación inicial del sistema, el siguiente paso consistió en establecer un método seguro y fiable para administrar el servidor de forma remota.

SSH se convirtió en el principal mecanismo de acceso y administración de Backend Lab.

---

#### ¿Por qué SSH?

SSH (Secure Shell) permite conectarse de forma remota a un sistema Linux mediante una conexión cifrada.

Gracias a SSH es posible:

- Administrar el servidor desde cualquier equipo autorizado.
- Ejecutar comandos remotos.
- Gestionar archivos.
- Mantener el sistema sin necesidad de monitor o teclado conectados a la Raspberry Pi.

---

#### Acceso Inicial

Durante las primeras fases del proyecto, el acceso se realizaba mediante:

```bash
ssh usuario@backend-lab.local
```

Esto permitía administrar el sistema desde la red local utilizando el hostname configurado durante la instalación.

---

#### Conceptos Aprendidos

Durante esta fase se trabajó con conceptos fundamentales relacionados con redes y administración Linux:

- Hostname
- Direcciones IP
- Máscaras de red
- Gateway
- DNS
- DHCP
- Resolución de nombres mediante mDNS

---

#### Resolución de Problemas

Uno de los objetivos del laboratorio fue aprender a diagnosticar incidencias habituales relacionadas con conectividad.

Algunas de las herramientas utilizadas fueron:

```bash
ping
```

```bash
hostname
```

```bash
ip addr
```

```bash
systemctl
```

Estas utilidades permitieron verificar el estado de la red y localizar problemas de configuración.

---

#### Administración Remota

A medida que Backend Lab fue creciendo, SSH se convirtió en la herramienta principal para:

- Instalar software.
- Gestionar servicios.
- Revisar logs.
- Administrar contenedores Docker.
- Desplegar aplicaciones.

La mayor parte del trabajo diario sobre el servidor se realiza actualmente mediante terminal remota.

---

#### Buenas Prácticas

Durante el desarrollo del laboratorio se adoptaron algunas prácticas habituales en entornos Linux:

- Mantener el sistema actualizado.
- Evitar cambios innecesarios en producción.
- Realizar pruebas previamente en entorno local.
- Utilizar Git para mantener el código bajo control de versiones.

---

#### Resultado

La Raspberry Pi quedó preparada para ser administrada completamente de forma remota.

SSH se convirtió en la base sobre la que posteriormente se desplegaron servicios como Docker, PostgreSQL, Nginx y Tailscale.