# 🚀 Scraper de Tiendanube - Reclutamiento Focus Group

Sistema automatizado para encontrar y contactar emprendedoras de Tiendanube en los sectores de moda y belleza.

---

## 📋 Índice

1. [Requisitos](#requisitos)
2. [Instalación](#instalación)
3. [Uso Rápido](#uso-rápido)
4. [Guía Completa](#guía-completa)
5. [Solución de Problemas](#solución-de-problemas)
6. [FAQ](#faq)

---

## 🎯 ¿Qué hace este scraper?

- ✅ Busca tiendas de Tiendanube (moda y belleza)
- ✅ Extrae Instagram, email, WhatsApp y Facebook
- ✅ Clasifica por nicho automáticamente
- ✅ Genera CSVs listos para outreach
- ✅ Prioriza tiendas por calidad de datos

**Resultado esperado:** 100-150 tiendas con datos de contacto en 1-2 horas.

---

## 💻 Requisitos

### Sistema Operativo
- ✅ Windows 10/11
- ✅ macOS 10.14+
- ✅ Linux (Ubuntu 18.04+)

### Software Necesario
- **Python 3.7 o superior** ([Descargar aquí](https://www.python.org/downloads/))
- Conexión a Internet
- 100 MB de espacio libre

### Conocimientos Necesarios
- ❌ NO necesitas saber programar
- ✅ Saber abrir la terminal/cmd
- ✅ Copiar y pegar comandos

---

## 📥 Instalación

### Paso 1: Descargar el Proyecto

**Opción A: Descarga ZIP**
```bash
# 1. Click en "Code" → "Download ZIP"
# 2. Descomprime el archivo
# 3. Abre la carpeta en tu terminal
```

**Opción B: Git Clone**
```bash
git clone https://github.com/tuusuario/scraper-tiendanube.git
cd scraper-tiendanube
```

### Paso 2: Instalar Dependencias

**Windows:**
```bash
# Abre PowerShell o CMD en la carpeta del proyecto
python -m pip install -r requirements.txt
```

**macOS/Linux:**
```bash
# Abre Terminal en la carpeta del proyecto
python3 -m pip install -r requirements.txt
```

**Verificar instalación:**
```bash
python --version
# Debe mostrar: Python 3.7.0 o superior
```

---

## 🚀 Uso Rápido (5 minutos)

### Opción 1: Modo Testing (Para Probar)

```bash
# Ejecuta con tiendas de ejemplo
python master_scraper.py 3
```

Resultado: Genera 3 archivos CSV con datos de 5 tiendas de prueba.

### Opción 2: Modo Automático (Producción)

```bash
# 1. Crea archivo urls_input.txt con tus URLs:
# (Una URL por línea)

# 2. Ejecuta:
python master_scraper.py 2

# 3. Espera 10-30 minutos según cantidad de URLs
```

### Opción 3: Modo Interactivo (Guiado)

```bash
# Te guía paso a paso
python master_scraper.py 1
```

---

## 📚 Guía Completa

### 1. Preparar URLs de Entrada

Crea un archivo `urls_input.txt` con URLs de Tiendanube:

```
https://beautymakeupok.mitiendanube.com
https://cherrybomb9.mitiendanube.com
https://kohphangan2.mitiendanube.com
```

**¿Cómo encontrar URLs?**

Método A: Google Manual
```
1. Ve a Google
2. Busca: site:mitiendanube.com moda mujer
3. Copia las URLs que veas
4. Pégalas en urls_input.txt
```

Método B: Script Extractor
```bash
python url_extractor.py
# Sigue las instrucciones en pantalla
```

### 2. Ejecutar Scraper

```bash
python master_scraper.py 2
```

**Lo que verás en pantalla:**
```
🚀 Iniciando Master Scraper
============================================================
FASE 2: SCRAPING
============================================================
[1/100] https://tienda1.mitiendanube.com...
    ✓ Instagram: ✓ | Email: ✗ | WhatsApp: ✓
[2/100] https://tienda2.mitiendanube.com...
    ✓ Instagram: ✓ | Email: ✓ | WhatsApp: ✓
...
```

### 3. Revisar Resultados

**Archivos generados:**
```
✅ tiendas_completo_YYYYMMDD_HHMMSS.csv    → Todos los datos
✅ tiendas_top50_YYYYMMDD_HHMMSS.csv       → Top 50 mejores
✅ tiendas_YYYYMMDD_HHMMSS.json            → Formato JSON
✅ reporte_YYYYMMDD_HHMMSS.txt             → Resumen texto
```

**Abrir con:**
- Excel / Google Sheets (CSV)
- Notepad / VS Code (TXT)
- Cualquier visor JSON (JSON)

### 4. Validar y Enriquecer Datos

```bash
# Limpia y valida el CSV generado
python validar_y_enriquecer.py

# Ingresa el nombre del CSV cuando te lo pida
```

---

## 📊 Entendiendo los Resultados

### Columnas del CSV

| Columna | Descripción | Ejemplo |
|---------|-------------|---------|
| `url` | URL de la tienda | https://tienda.mitiendanube.com |
| `nombre_tienda` | Nombre de la tienda | Beauty Make Up |
| `nicho` | Categoría | Belleza - Maquillaje |
| `instagram` | URL de Instagram | https://instagram.com/beautymakeup |
| `email` | Email de contacto | contacto@tienda.com |
| `whatsapp` | Número de WhatsApp | 5491112345678 |
| `facebook` | URL de Facebook | https://facebook.com/tienda |
| `score_contacto` | Calidad (0-8) | 5 |
| `fecha_scraping` | Cuándo se scrapeó | 2025-10-24 16:46:43 |

### Score de Contacto

```
8 puntos = Instagram + Email + WhatsApp + Facebook (Excelente)
5 puntos = Instagram + WhatsApp (Muy bueno)
3 puntos = Solo Instagram (Aceptable)
0 puntos = Sin contactos (Descartar)
```

### Tasas de Éxito Esperadas

```
Instagram:  70-90% de las tiendas
WhatsApp:   40-60% de las tiendas
Email:      20-40% de las tiendas
Facebook:   30-50% de las tiendas
```

---

## 🛠️ Solución de Problemas

### Error: "Python no se reconoce"

**Windows:**
```bash
# Reinstala Python desde:
# https://www.python.org/downloads/
# ✅ Marca: "Add Python to PATH"
```

**macOS:**
```bash
# Usa python3 en lugar de python:
python3 master_scraper.py 3
```

### Error: "No module named 'requests'"

```bash
# Instala las dependencias:
pip install -r requirements.txt

# Si no funciona:
pip install requests beautifulsoup4 pandas lxml
```

### Error: "Permission denied"

**Windows:**
```bash
# Ejecuta PowerShell como Administrador
# Click derecho en PowerShell → "Ejecutar como administrador"
```

**macOS/Linux:**
```bash
# Agrega permisos de ejecución:
chmod +x master_scraper.py
```

### El scraper es muy lento

```python
# Edita master_scraper.py
# Busca: time.sleep(2)
# Cambia por: time.sleep(1)

# ⚠️ Riesgo: Podrías ser bloqueado temporalmente
```

### No encuentra Instagram/Email

```
✓ Normal: Solo 70-90% tienen Instagram público
✓ Solución: Usa Hunter.io para emails
✓ Solución: Búsqueda manual en los perfiles
```

### "Google me bloqueó"

```
✓ Espera 24 horas
✓ Usa VPN
✓ Búsqueda manual (copia/pega URLs)
✓ Usa SerpAPI (100 búsquedas gratis/mes)
```

---

## 🎓 FAQ (Preguntas Frecuentes)

### ¿Cuántas tiendas puedo scrapear?

- **Sin límite técnico**, pero recomendamos:
- 50-100 para empezar
- 150-200 para campaña completa
- Respetar 2-3 segundos entre requests

### ¿Es legal hacer scraping?

- ✅ Scraping de datos públicos: Legal
- ✅ Para investigación/análisis: Permitido
- ❌ Spam/acoso: Prohibido
- ❌ Venta de datos: Ilegal

**Recomendación:** Usa los datos solo para contacto legítimo (focus group).

### ¿Cuánto tarda?

```
10 tiendas   = 1 minuto
50 tiendas   = 5 minutos
100 tiendas  = 15 minutos
200 tiendas  = 30 minutos
```

### ¿Funciona en otros países?

✅ Sí, Tiendanube opera en:
- Argentina
- México
- Brasil (como Nuvemshop)
- Colombia
- Chile

Ajusta las búsquedas según el país.

### ¿Puedo scrapear otros e-commerce?

❌ Este scraper es específico para Tiendanube (`.mitiendanube.com`)

Para otros:
- Shopify → Necesita adaptación
- WooCommerce → Necesita adaptación
- MercadoShops → Necesita adaptación

### ¿Necesito pagar algo?

```
Scraper:        GRATIS ✅
Python:         GRATIS ✅
Hunter.io:      $49/mes (opcional)
SerpAPI:        $50/mes (opcional)
```

**Total mínimo:** $0 (todo funciona gratis)

---

## 📞 Soporte

### Reportar un Bug

```bash
# Incluye en tu reporte:
1. Sistema operativo
2. Versión de Python (python --version)
3. Mensaje de error completo
4. Pasos para reproducir
```

### Solicitar Ayuda

```bash
# Antes de preguntar:
1. Lee el README completo
2. Revisa "Solución de Problemas"
3. Busca en FAQ
```

---

## 📄 Licencia

MIT License - Uso libre para proyectos personales y comerciales.

---

## 🙏 Créditos

Desarrollado para reclutamiento de focus groups en el sector e-commerce.

**Autor:** [Tu Nombre]  
**Versión:** 1.0.0  
**Última actualización:** Octubre 2025

---

## 🚀 Próximos Pasos

1. ✅ Completar scraping de 100-150 tiendas
2. ✅ Enriquecer emails con Hunter.io
3. ✅ Verificar Instagrams manualmente
4. ✅ Crear templates de outreach
5. ✅ Iniciar campaña de contacto

**¿Listo para comenzar? Ejecuta:**
```bash
python master_scraper.py 1
```