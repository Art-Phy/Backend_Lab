
### Configuración Inicial de la Raspberry Pi

##### Contexto

Backend Lab nace como un laboratorio personal para practicar despliegue de aplicaciones backend en un entorno Linux real.

El objetivo inicial era disponer de una máquina dedicada donde experimentar con tecnologías como Docker, PostgreSQL, Nginx, Tailscale y FastAPI sin depender de servicios cloud externos.

---

#### Objetivo

Preparar una Raspberry Pi como servidor base para alojar aplicaciones backend, administrar servicios desde terminal y simular un entorno de despliegue similar al de un servidor real.

Este primer paso se centró en:

- Instalar el sistema operativo.
- Configurar acceso remoto.
- Validar conectividad.
- Preparar el sistema para futuras fases de despliegue.

---

#### Hardware Utilizado

- Raspberry Pi 3 Model B
- Tarjeta microSD de 128 GB
- Conexión WiFi doméstica
- Fuente de alimentación para Raspberry Pi

---

#### Sistema Operativo

Se utilizó **Raspberry Pi OS Lite (64 bits)**.

La versión Lite fue elegida porque el objetivo del laboratorio no era disponer de un entorno gráfico, sino trabajar como en un servidor Linux real, administrado principalmente por terminal.

---

#### Configuración Inicial

La instalación se realizó con Raspberry Pi Imager.

Durante el proceso inicial se configuraron los elementos básicos del sistema:

- Hostname personalizado: `backend-lab`
- Usuario principal
- Conexión WiFi
- Acceso SSH habilitado
- Zona horaria y configuración regional

---

#### Primer Arranque

Tras insertar la microSD y encender la Raspberry Pi, se verificó que el dispositivo se conectaba correctamente a la red local.

El acceso inicial se realizó mediante SSH desde otro equipo dentro de la misma red:

```bash
ssh usuario@backend-lab.local
```

En el caso de este laboratorio, el hostname personalizado permite acceder al dispositivo sin depender inicialmente de una IP fija.

---

#### Actualización del Sistema

Una vez dentro de la Raspberry Pi, se actualizaron los paquetes del sistema:

```bash
sudo apt update
sudo apt upgrade -y
```

Este paso asegura que el sistema parte de una base actualizada antes de instalar servicios adicionales.

---

#### Comprobaciones Básicas

Se verificaron aspectos esenciales del sistema:

```bash
hostname
```

```bash
ip addr
```

```bash
ping 8.8.8.8
```

Estas comprobaciones permiten validar:

- Nombre del dispositivo.
- Dirección IP asignada.
- Conectividad a Internet.

---

#### Acceso por Red Local

Durante la fase inicial, el acceso al servidor se realizó desde la red local utilizando:

```bash
ssh usuario@backend-lab.local
```

Más adelante, el acceso remoto privado se ampliaría mediante Tailscale, evitando la necesidad de abrir puertos en el router.

---

#### Resultado

Al finalizar esta fase, la Raspberry Pi quedó preparada como servidor base:

- Sistema operativo instalado.
- Acceso SSH funcional.
- Conectividad de red validada.
- Hostname personalizado configurado.
- Sistema actualizado y listo para instalar servicios.

Este fue el punto de partida para convertir la Raspberry Pi en un laboratorio backend real.