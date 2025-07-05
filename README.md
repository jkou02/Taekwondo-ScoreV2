---

## 🧾 **Descripción de la API: Combate FastAPI**

### 📌 **Propósito**

Esta API recibe señales de golpe enviadas por jueces desde una app móvil en el contexto de combates deportivos. Las señales se validan solo si al menos **dos jueces coinciden** en el tipo de golpe dentro de un margen de tiempo configurable (por defecto: ±300 ms).

---

## 📐 **Arquitectura técnica**

* **Backend:** FastAPI (Python)
* **Base de datos:** SQLite (puede migrarse a PostgreSQL)
* **ORM:** SQLAlchemy + Databases (modo asíncrono)
* **Esquema validado:** `Pydantic` para entrada de datos
* **Validación de eventos:** Lógica custom por coincidencia de jueces

---

## 📤 **Ruta principal**

### `POST /events`

📌 **Descripción**: Recibe un evento (golpe) reportado por un juez.

📥 **Cuerpo del JSON (EventIn)**:

```json
{
  "judge_id": "juez_1",
  "match_id": "match_001",
  "event_type": "kick_chest",
  "timestamp": "2025-06-25T21:35:00Z"
}
```

🔢 `event_type` puede ser uno de:

* `"kick_chest"`
* `"kick_head"`
* `"punch"`
* `"spin_kick"`

📤 **Respuesta**:

```json
{
  "message": "Evento registrado",
  "validado": true,
  "jueces_confirmantes": ["juez_1", "juez_2"]
}
```

* `"validado": true` si coincidió con otro juez dentro del rango de ±300ms.
* `"jueces_confirmantes"` lista de jueces que coincidieron (al menos dos).

---

## 🗃️ **Tablas utilizadas**

### `events` (eventos crudos)

Registra todos los eventos individuales recibidos, aunque no estén validados aún.

| Campo       | Tipo     | Descripción             |
| ----------- | -------- | ----------------------- |
| id          | UUID     | Identificador único     |
| judge\_id   | str      | ID del juez             |
| match\_id   | str      | ID del combate          |
| event\_type | str      | Tipo de evento recibido |
| timestamp   | datetime | Hora del evento         |

---

### `validated_events` (eventos validados)

Contiene los eventos que fueron confirmados por coincidencia de al menos 2 jueces.

| Campo         | Tipo       | Descripción                             |
| ------------- | ---------- | --------------------------------------- |
| id            | UUID       | ID único del evento validado            |
| match\_id     | str        | Combate al que pertenece                |
| event\_type   | str        | Tipo de evento confirmado               |
| judges        | list\[str] | Lista de IDs de jueces que coincidieron |
| validated\_at | datetime   | Fecha y hora de validación              |

---

## ⚙️ **Lógica de validación**

Cuando llega un evento:

1. Se guarda en la tabla `events`.
2. Se busca en la base de datos si **otro juez** ha enviado el **mismo `event_type` y `match_id`** en un rango de ±300 ms respecto al `timestamp`.
3. Si hay coincidencia:

   * Se guarda un nuevo registro en `validated_events`.
   * Se responde con `"validado": true`.

---

## 🧪 **Dependencias (requirements.txt)**

```txt
fastapi
uvicorn
sqlalchemy
databases
aiosqlite
```

---

## 🚀 **Ejecución local**

```bash
uvicorn app.main:app --reload
```

Documentación Swagger disponible en:

```
http://127.0.0.1:8000/docs
```

---

## ✅ ¿Para qué sirve esta descripción?

* Puedes copiarla y pegarla en un nuevo chat conmigo para que entienda tu proyecto.
* Puedes documentar tu proyecto para ti, otros desarrolladores o jurado técnico.
* Puedes usarla para escribir un `README.md`.

¿Quieres que te prepare esta misma descripción en formato Markdown para que la pegues directo en GitHub o en Obsidian?

