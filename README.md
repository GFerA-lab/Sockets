# Chat TCP con Sockets en Python

Proyecto educativo que implementa un sistema de chat en red utilizando **sockets TCP** en Python con arquitectura cliente-servidor basada en threading.

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema de chat simple donde múltiples clientes pueden conectarse a un servidor central y comunicarse entre sí en tiempo real.

## 📁 Estructura del Proyecto

```
Sockets_chgll3/
├── README.md              # Este archivo
├── prueba.py              # Servidor TCP con threading
└── cliente.py             # Cliente TCP
```

## 🚀 Cómo Usar

### Paso 1: Iniciar el servidor

En la primera terminal:
```bash
python prueba.py
```

Salida esperada:
```
Servidor escuchando en puerto 5000...
```

### Paso 2: Conectar clientes

En otras terminales (puedes abrir varias):
```bash
python cliente.py
```

El cliente se conectará automáticamente al servidor y verás:
```
Conectado al chat.
```

Ahora puedes escribir mensajes - se enviarán a todos los demás clientes conectados.

**Para cerrar un cliente:** Escribe `salir` y presiona Enter.

**Características:**
- ✅ Múltiples clientes simultáneos
- ✅ Arquitectura basada en threading (un hilo por cliente)
- ✅ Difusión de mensajes a todos los clientes conectados
- ✅ Notificación automática de conexiones/desconexiones
- ✅ Manejo seguro de errores

## 🔧 Requisitos

- **Python 3.7+**
- Sin dependencias externas (usa módulos estándar: `socket` y `threading`)

## 📖 Conceptos Implementados

| Concepto | Descripción | Archivo |
|----------|-------------|---------|
| **TCP (SOCK_STREAM)** | Conexión confiable orientada a flujo | `prueba.py`, `cliente.py` |
| **Threading** | Multihilo para manejar clientes concurrentes | `prueba.py` |
| **Sockets no bloqueantes** | Comunicación eficiente con clientes | Ambos |
| **Broadcast interno** | Difusión de mensajes a todos los clientes | `prueba.py` |

## 🔌 Diagrama de Arquitectura

```
┌──────────────────────────────────────────────┐
│    Servidor (prueba.py)                      │
│    • Escucha en localhost:5000               │
│    • Threading: 1 hilo por cliente           │
│    • Difunde mensajes a todos               │
└──────────────────────────────────────────────┘
         ↕          ↕          ↕
    ┌────────┐  ┌────────┐  ┌────────┐
    │ Hilo 1 │  │ Hilo 2 │  │ Hilo 3 │
    │Cliente │  │Cliente │  │Cliente │
    └────────┘  └────────┘  └────────┘
  (cliente.py) (cliente.py) (cliente.py)
```

## 💡 Ejemplo de Uso

### Terminal 1 - Servidor:
```bash
$ python prueba.py
Servidor escuchando en puerto 5000...
Cliente conectado: ('127.0.0.1', 54321)
Cliente conectado: ('127.0.0.1', 54322)
[('127.0.0.1', 54321)]: Hola a todos
[('127.0.0.1', 54322)]: Hola! ¿Cómo estás?
```

### Terminal 2 - Cliente 1:
```bash
$ python cliente.py
Conectado al chat.
Tú: Hola a todos
[127.0.0.1]: Hola! ¿Cómo estás?
Tú: salir
Desconectado del servidor.
```

### Terminal 3 - Cliente 2:
```bash
$ python cliente.py
Conectado al chat.
[127.0.0.1]: Hola a todos
Tú: Hola! ¿Cómo estás?
Tú: salir
Desconectado del servidor.
```

## ⚙️ Configuración

### Cambiar puerto del servidor

Edita `prueba.py`:
```python
server.bind(('localhost', 5000))  # Cambiar 5000 por otro puerto
```

También debes actualizar `cliente.py`:
```python
sktCliente.connect(('localhost', 5000))  # Cambiar al mismo puerto del servidor
```

### Conectar desde otra máquina

En `cliente.py`, cambia `localhost` por la IP del servidor:
```python
sktCliente.connect(('192.168.1.100', 5000))  # Reemplaza con la IP del servidor
```
