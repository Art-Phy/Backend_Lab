```markdown
## Backend Lab Hardware Dashboard

Dashboard físico para monitorizar el estado de **Backend Lab** mediante una pantalla USB de 3.5" conectada a la Raspberry Pi.

El componente recoge métricas del sistema, comprueba el estado de servicios críticos y muestra la información en tiempo real mediante una interfaz generada en Python.

---

### Hardware probado

La implementación actual ha sido validada con el siguiente hardware:

- Raspberry Pi 3 Model B
- Raspberry Pi OS Lite 64-bit
- Pantalla USB IPS de 3.5"
- Resolución: `320x480`
- VID:PID: `1a86:5722`
- Product: `UsbMonitor`
- Serial: `serial number`
- Dispositivo Linux: `/dev/ttyACM0`
- Driver Linux: `cdc_acm`
- Hardware revision: `A`

Linux reconoce automáticamente la pantalla como un dispositivo serie USB.

---

### Arquitectura

```text
System Metrics
      │
      ├── CPU
      ├── RAM
      ├── Disk
      ├── Temperature
      └── Uptime
      │
      ▼
Service Status
      │
      ├── Nginx
      ├── Docker
      ├── PostgreSQL
      └── PostgreSQL Backup
      │
      ▼
Renderer
      │
      ▼
PIL Image
      │
      ▼
Display Adapter
      │
      ▼
Turing Rev A Driver
      │
      ▼
/dev/ttyACM0
      │
      ▼
USB Display
```

La aplicación genera completamente el frame mostrado en pantalla.

La librería externa `turing-smart-screen-python` se utiliza únicamente como capa de comunicación con el protocolo de la pantalla.

La recopilación de métricas, comprobación de servicios, renderizado, lógica de actualización y gestión del dashboard forman parte de Backend Lab.

---

### Información mostrada

#### Sistema

El dashboard muestra las siguientes métricas:

- CPU
- RAM
- Uso de disco
- Temperatura de la CPU
- Uptime

#### Infraestructura

También comprueba el estado de los principales componentes de infraestructura:

- Nginx
- Docker
- PostgreSQL
- Último backup de PostgreSQL

Los servicios se representan mediante indicadores simples:

- Verde: estado correcto
- Rojo: error detectado

---

### Actualización

El dashboard actualiza automáticamente la información cada 5 segundos.

En cada ciclo:

1. Se recopilan las métricas del sistema.
2. Se comprueba el estado de los servicios.
3. Se genera un nuevo frame mediante Pillow.
4. El frame se envía a la pantalla USB.

La pantalla se inicializa una sola vez al arrancar el proceso.

---

### Estructura

```text
dashboard/
├── backend_dashboard/
│   ├── __init__.py
│   ├── display.py
│   ├── main.py
│   ├── metrics.py
│   ├── renderer.py
│   └── services.py
├── systemd/
│   └── backend-dashboard.service
├── pyproject.toml
└── README.md
```

#### `main.py`

Coordina el ciclo principal del dashboard:

- Recopila métricas.
- Comprueba servicios.
- Genera el frame.
- Actualiza la pantalla.
- Repite el proceso cada 5 segundos.

#### `metrics.py`

Obtiene las métricas del sistema:

- CPU
- RAM
- Disco
- Temperatura
- Uptime

La temperatura se obtiene directamente desde la interfaz térmica de Linux:

```text
/sys/class/thermal/thermal_zone0/temp
```

#### `services.py`

Comprueba el estado de:

- Nginx
- Docker
- PostgreSQL
- Último backup de PostgreSQL

Los servicios gestionados por `systemd` se consultan mediante:

```bash
systemctl is-active
```

#### `renderer.py`

Genera el frame completo de `320x480` mediante Pillow.

El renderer no conoce detalles del hardware ni del protocolo USB.

Su única responsabilidad es convertir los datos del sistema en una imagen.

#### `display.py`

Actúa como adaptador entre Backend Lab y la pantalla física.

Es el único módulo que conoce:

- `/dev/ttyACM0`
- `turing-smart-screen-python`
- `LcdCommRevA`
- La resolución física de la pantalla

---

### Dependencias

El componente utiliza las siguientes dependencias principales:

- `Pillow`
- `numpy`
- `pyserial`
- `psutil`

Las dependencias se gestionan mediante `pyproject.toml`.

---

### Driver de pantalla

La comunicación de bajo nivel utiliza el proyecto:

`turing-smart-screen-python`

Backend Lab utiliza únicamente su implementación para pantallas Rev A.

Por defecto, el dashboard busca el driver en:

```text
~/turing-smart-screen-python
```

También puede utilizarse otra ubicación mediante la variable de entorno:

```text
TURING_DRIVER_PATH
```

El orden de resolución es:

1. Ruta proporcionada explícitamente al adaptador.
2. Variable `TURING_DRIVER_PATH`.
3. `~/turing-smart-screen-python`.

---

### Instalación

La instalación utilizada actualmente en la Raspberry Pi se encuentra en:

```text
/home/<usuario>/Backend_Lab
```

Entrar en el componente:

```bash
cd /home/<usuario>/Backend_Lab/dashboard
```

Crear el entorno virtual:

```bash
python3 -m venv .venv
```

Activarlo:

```bash
source .venv/bin/activate
```

Instalar el proyecto en modo editable:

```bash
python -m pip install -e .
```

Comprobar dependencias:

```bash
python -m pip check
```

---

### Permisos USB

La pantalla aparece en Linux como:

```text
/dev/ttyACM0
```

El dispositivo pertenece al grupo:

```text
dialout
```

El usuario que ejecuta el dashboard debe pertenecer a ese grupo.

Comprobar grupos:

```bash
groups
```

Añadir un usuario a `dialout`:

```bash
sudo usermod -aG dialout <usuario>
```

Es necesario cerrar sesión y volver a entrar para aplicar el cambio.

Se puede comprobar el acceso al dispositivo mediante:

```bash
test -r /dev/ttyACM0 && echo "READ OK"
test -w /dev/ttyACM0 && echo "WRITE OK"
```

---

### Ejecución manual

Desde:

```text
/home/<usuario>/Backend_Lab/dashboard
```

activar el entorno:

```bash
source .venv/bin/activate
```

Ejecutar:

```bash
backend-dashboard
```

El proceso permanecerá activo y actualizará la pantalla continuamente.

Puede detenerse mediante:

```text
Ctrl+C
```

---

### Backup PostgreSQL

El dashboard no realiza ni valida directamente las copias de seguridad.

El proceso de backup está gestionado por:

```text
scripts/backup_postgresql.sh
```

El script:

1. Ejecuta `pg_dump`.
2. Comprueba que el archivo generado no esté vacío.
3. Valida el dump mediante `pg_restore -l`.
4. Mantiene la política de rotación configurada.
5. Registra el resultado de la ejecución.

El estado se guarda en:

```text
~/.local/state/backend-lab/backup-postgresql.status
```

Durante la ejecución:

```text
running
```

Si el backup termina correctamente:

```text
success
```

Si ocurre un error:

```text
failed
```

El Hardware Dashboard únicamente consulta este fichero.

El indicador `BACKUP` aparece en verde cuando el último estado registrado es:

```text
success
```

---

### Servicio systemd

El dashboard puede ejecutarse automáticamente durante el arranque de la Raspberry Pi mediante `systemd`.

La unidad incluida en el proyecto se encuentra en:

```text
dashboard/systemd/backend-dashboard.service
```

Contenido:

```ini
[Unit]
Description=Backend Lab Hardware Dashboard
After=network.target docker.service
Requires=docker.service

[Service]
Type=simple
User=<usuario>
WorkingDirectory=/home/<usuario>/Backend_Lab/dashboard

ExecStart=/home/<usuario>/Backend_Lab/dashboard/.venv/bin/backend-dashboard

Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Instalar la unidad:

```bash
sudo cp systemd/backend-dashboard.service \
  /etc/systemd/system/backend-dashboard.service
```

Recargar la configuración de `systemd`:

```bash
sudo systemctl daemon-reload
```

Activar el servicio durante el arranque:

```bash
sudo systemctl enable backend-dashboard.service
```

Iniciar manualmente:

```bash
sudo systemctl start backend-dashboard.service
```

Comprobar estado:

```bash
systemctl status backend-dashboard.service
```

Reiniciar:

```bash
sudo systemctl restart backend-dashboard.service
```

Detener:

```bash
sudo systemctl stop backend-dashboard.service
```

Consultar logs:

```bash
sudo journalctl -u backend-dashboard.service
```

---

### Arranque automático

Una vez habilitado el servicio, el flujo de arranque es:

```text
Raspberry Pi
      │
      ▼
Linux
      │
      ▼
Docker y servicios del sistema
      │
      ▼
backend-dashboard.service
      │
      ▼
Hardware Dashboard
      │
      ▼
Pantalla USB
```

No es necesario iniciar sesión mediante SSH ni ejecutar manualmente el dashboard.

Al conectar la Raspberry Pi a la corriente, el Hardware Dashboard se inicia automáticamente cuando el sistema termina de cargar los servicios necesarios.

---

### Estado actual

El Hardware Dashboard funciona actualmente sobre una Raspberry Pi 3 Model B con Raspberry Pi OS Lite 64-bit.

Actualmente dispone de:

- Renderizado propio mediante Pillow.
- Métricas del sistema en tiempo real.
- Monitorización de infraestructura.
- Estado fiable del último backup.
- Actualización automática cada 5 segundos.
- Comunicación USB con la pantalla.
- Ejecución automática mediante `systemd`.
- Reinicio automático del proceso en caso de fallo.

La interfaz visual actual es funcional y está pendiente de una futura revisión de diseño.
```
