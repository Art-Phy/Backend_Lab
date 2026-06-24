
### Tailscale

#### Objetivo

Una vez completadas las fases de despliegue y almacenamiento, el siguiente objetivo fue disponer de acceso remoto seguro al servidor desde cualquier ubicación sin necesidad de abrir puertos en el router.

Para ello se adoptó Tailscale como solución principal de conectividad remota.

---

#### ¿Por qué Tailscale?

Tailscale permite crear una red privada virtual basada en WireGuard de forma sencilla y segura.

Cada dispositivo conectado obtiene una dirección IP privada dentro de la red Tailscale, permitiendo la comunicación directa entre equipos autorizados.

Entre sus principales ventajas destacan:

- Configuración sencilla.
- Conexiones cifradas.
- Sin necesidad de abrir puertos.
- Acceso remoto seguro desde cualquier lugar.
- Compatibilidad con múltiples sistemas operativos.

---

#### Problema a Resolver

Durante las primeras fases del laboratorio, el acceso al servidor estaba limitado a la red local.

```text
Laptop
   │
   ▼
WiFi Local
   │
   ▼
Backend Lab
```

Esto impedía administrar el servidor cuando se estaba fuera de casa.

---

#### Solución Implementada

Mediante Tailscale, tanto el servidor como los equipos de administración se incorporaron a una misma red privada virtual.

```text
Laptop
   │
   ▼
Tailscale Network
   │
   ▼
Backend Lab
```

De esta forma, ambos dispositivos pueden comunicarse independientemente de la red WiFi o conexión a Internet utilizada.

---

#### Acceso Remoto

Una vez configurado Tailscale, el acceso al servidor puede realizarse utilizando su dirección IP privada asignada dentro de la red.

```bash
ssh usuario@100.x.x.x
```

Esto permite administrar Backend Lab desde cualquier ubicación con conexión a Internet.

---

#### Beneficios Obtenidos

La incorporación de Tailscale permitió:

- Acceso remoto seguro sin abrir puertos.
- Administración del servidor desde cualquier red.
- Reducción de riesgos de seguridad.
- Simplificación de la configuración de red.
- Mayor comodidad para mantenimiento y despliegues.

---

#### Casos de Uso

Actualmente Tailscale se utiliza para:

- Acceso SSH remoto.
- Administración de contenedores Docker.
- Consulta de servicios desplegados.
- Mantenimiento general del sistema.
- Supervisión del laboratorio desde ubicaciones externas.

---

#### Seguridad

Solo los dispositivos autorizados dentro de la red Tailscale pueden comunicarse con Backend Lab.

Esto reduce significativamente la superficie de exposición del servidor frente a Internet pública.

---

#### Resultado

La incorporación de Tailscale transformó Backend Lab en un entorno accesible desde cualquier lugar sin necesidad de configuraciones complejas de red.

Gracias a esta solución, el laboratorio puede administrarse de forma segura tanto desde la red local como desde ubicaciones remotas, manteniendo una experiencia de uso similar a la de una red privada.