# 🚀 Scraper de Tiendanube - Focus Group Recruiter

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://TU-USUARIO-scraper-tiendanube.streamlit.app)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Sistema automatizado para identificar y extraer datos de contacto de emprendedoras de Tiendanube en los sectores de **moda y belleza** para reclutamiento de focus groups.

---

## 🎯 ¿Qué hace esta herramienta?

Esta aplicación web permite:

- ✅ **Extraer automáticamente** datos de contacto de tiendas Tiendanube
- ✅ **Encontrar** Instagram, Email, WhatsApp y Facebook
- ✅ **Clasificar** tiendas por nicho (Belleza, Moda, Joyería, etc.)
- ✅ **Priorizar** contactos por calidad de datos (scoring automático)
- ✅ **Exportar** CSVs listos para campañas de outreach
- ✅ **Visualizar** estadísticas y métricas en tiempo real

---

## 🌐 Demo en Vivo

**🔗 [Abrir App](https://TU-USUARIO-scraper-tiendanube.streamlit.app)**

> **Nota:** Reemplaza `TU-USUARIO` con tu usuario de GitHub en el link de arriba

---

## 📊 Resultados Esperados

| Métrica | Tasa de Éxito |
|---------|---------------|
| 📷 Instagram | 70-90% |
| 📱 WhatsApp | 40-60% |
| 📧 Email | 20-40% |
| 👥 Facebook | 30-50% |

**Ejemplo:** De 100 tiendas scrapeadas, obtendrás aproximadamente:
- 80+ perfiles de Instagram
- 50+ números de WhatsApp
- 30+ emails
- 40+ páginas de Facebook

---

## 🚀 Uso Rápido

### Opción 1: Usar la App Online (Recomendado)

1. **Abre el link:** https://TU-USUARIO-scraper-tiendanube.streamlit.app
2. **Selecciona el modo:**
   - 📝 Ingresar URLs manualmente
   - 📂 Subir archivo .txt
   - 🧪 Usar URLs de prueba (para testing)
3. **Inicia el scraping:** Click en "🚀 Iniciar Scraping"
4. **Descarga resultados:** Los CSVs se generan automáticamente

⏱️ **Tiempo estimado:**
- 10 tiendas: ~2 minutos
- 50 tiendas: ~10 minutos
- 100 tiendas: ~20 minutos

### Opción 2: Ejecutar Localmente

```bash
# Clonar repositorio
git clone https://github.com/TU-USUARIO/scraper-tiendanube.git
cd scraper-tiendanube

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar app
streamlit run app.py
```

La app se abrirá automáticamente en `http://localhost:8501`

---

## 📁 Estructura del Proyecto

```
scraper-tiendanube/
├── app.py                 # Aplicación principal Streamlit
├── requirements.txt       # Dependencias Python
├── README.md             # Esta documentación
├── .gitignore            # Archivos ignorados por Git
└── LICENSE               # Licencia MIT
```

---

## 🛠️ Tecnologías Utilizadas

- **[Streamlit](https://streamlit.io)** - Framework de UI
- **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)** - Web scraping
- **[Pandas](https://pandas.pydata.org/)** - Procesamiento de datos
- **[Requests](https://requests.readthedocs.io/)** - HTTP requests

---

## 📋 Características

### ✨ Extracción de Datos
- Nombre de la tienda
- URL completa
- Descripción (primeros 200 caracteres)
- Nicho automático (10+ categorías)
- Redes sociales (Instagram, Facebook)
- Datos de contacto (Email, WhatsApp)
- Score de calidad (0-8 puntos)

### 📊 Análisis y Visualización
- Métricas en tiempo real
- Gráficos por nicho
- Distribución de scores
- Filtros interactivos
- Tablas ordenables

### 📥 Exportación
- **CSV Completo:** Todos los datos
- **CSV Top 50:** Las 50 mejores tiendas por score
- Formato UTF-8 compatible con Excel
- Nombres de archivo con timestamp

---

## 🎯 Sistema de Scoring

Cada tienda recibe un **score de contacto** de 0 a 8 puntos:

| Dato Encontrado | Puntos |
|----------------|--------|
| Instagram | +3 |
| WhatsApp | +2 |
| Email | +2 |
| Facebook | +1 |

**Ejemplo:**
- Tienda con IG + WA + Email = 7 puntos ⭐⭐⭐
- Tienda con solo IG = 3 puntos ⭐
- Tienda sin contactos = 0 puntos (descartada)

---

## 📖 Guía de Uso Detallada

### 1️⃣ Preparar tus URLs

Tienes 3 opciones:

**A) Ingresar manualmente**
```
https://beautymakeup.mitiendanube.com
https://modafashion.mitiendanube.com
https://joyasarte.mitiendanube.com
```

**B) Crear archivo .txt**
```
# urls_input.txt
https://tienda1.mitiendanube.com
https://tienda2.mitiendanube.com
https://tienda3.mitiendanube.com
```

**C) Usar URLs de prueba**
- La app incluye 5 URLs reales para testing

### 2️⃣ Configurar Scraping

En la barra lateral puedes ver:
- Modo de ingreso seleccionado
- Estadísticas esperadas
- Información de la app

### 3️⃣ Ejecutar y Monitorear

Durante el scraping verás:
- Barra de progreso
- Tienda actual siendo procesada
- Resultados en tiempo real:
  - ✓ = Dato encontrado
  - ✗ = Dato no encontrado

### 4️⃣ Analizar Resultados

Después del scraping verás:
- **Métricas:** Total, con IG, con email, con WA
- **Gráficos:** Distribución por nicho y score
- **Tabla:** Datos completos con filtros

### 5️⃣ Exportar Datos

Descarga los CSVs:
- **Completo:** Para análisis exhaustivo
- **Top 50:** Para priorizar outreach

---

## 🔍 Nichos Detectados Automáticamente

La app clasifica las tiendas en:

- 💄 **Belleza - Maquillaje:** Cosméticos, labiales, sombras
- 🧴 **Belleza - Skincare:** Cremas, serums, faciales
- 💎 **Joyería:** Oro, plata, anillos, collares
- ✨ **Bijouterie:** Accesorios de fantasía
- 👗 **Moda - Ropa:** Vestidos, blusas, indumentaria
- 👜 **Accesorios:** Carteras, bolsos, cinturones
- 🎁 **Otro:** Categorías no especificadas

---

## ⚙️ Configuración Avanzada

### Ajustar Velocidad de Scraping

Edita `app.py` línea 48:

```python
# Más lento pero más seguro (menos riesgo de bloqueo)
time.sleep(2.0)

# Más rápido pero mayor riesgo
time.sleep(0.8)

# Balance recomendado
time.sleep(1.5)  # Default
```

### Cambiar Timeout de Requests

Línea 35:

```python
response = self.session.get(url, timeout=15)  # 15 segundos
```

---

## 🚨 Limitaciones y Consideraciones

### Técnicas
- ❌ No funciona con tiendas que requieren login
- ❌ JavaScript pesado puede no cargar completamente
- ⚠️ Rate limiting: 2 segundos entre requests
- ⚠️ Timeout: 15 segundos por tienda

### Legales
- ✅ Solo datos públicos disponibles en web
- ✅ Respeta `robots.txt` de Tiendanube
- ❌ No usar para spam o acoso
- ❌ No revender datos personales

### Éticas
- 🎯 Uso exclusivo para research/focus groups
- 🤝 Contacto respetuoso y transparente
- 📧 Ofrecer opt-out en comunicaciones
- 🛡️ Proteger privacidad de datos

---

## 📈 Roadmap y Mejoras Futuras

- [ ] Soporte para Selenium (tiendas con JS)
- [ ] Integración con Hunter.io API (emails)
- [ ] Verificación de Instagram (seguidores, actividad)
- [ ] Export a Google Sheets
- [ ] Búsqueda integrada en Google
- [ ] Detección de duplicados inteligente
- [ ] Histórico de scraping
- [ ] Autenticación de usuarios
- [ ] Scheduler para scraping automático
- [ ] API REST

---

## 🤝 Contribuir

¿Quieres mejorar el scraper? ¡Contribuciones son bienvenidas!

1. Fork el proyecto
2. Crea tu rama: `git checkout -b feature/nueva-funcionalidad`
3. Commit cambios: `git commit -m 'Agrega nueva funcionalidad'`
4. Push a la rama: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

---

## 🐛 Reportar Bugs

Si encuentras un error:

1. Ve a [Issues](https://github.com/TU-USUARIO/scraper-tiendanube/issues)
2. Crea un nuevo issue
3. Incluye:
   - Descripción del error
   - Pasos para reproducir
   - Screenshots (si aplica)
   - Sistema operativo y versión de Python

---

## 📞 Soporte

- 📧 **Email:** tu-email@ejemplo.com
- 💬 **GitHub Issues:** [Abrir issue](https://github.com/TU-USUARIO/scraper-tiendanube/issues)
- 📱 **WhatsApp:** +54 9 11 XXXX-XXXX

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

```
MIT License

Copyright (c) 2025 [Tu Nombre]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🌟 Reconocimientos

Desarrollado para facilitar el reclutamiento de focus groups en el ecosistema de e-commerce latinoamericano.

**Tecnologías de código abierto utilizadas:**
- Streamlit Community Cloud
- Beautiful Soup
- Pandas
- Python

---

## 📊 Estadísticas del Proyecto

![GitHub stars](https://img.shields.io/github/stars/TU-USUARIO/scraper-tiendanube?style=social)
![GitHub forks](https://img.shields.io/github/forks/TU-USUARIO/scraper-tiendanube?style=social)
![GitHub issues](https://img.shields.io/github/issues/TU-USUARIO/scraper-tiendanube)
![GitHub last commit](https://img.shields.io/github/last-commit/TU-USUARIO/scraper-tiendanube)

---

## 🎓 Casos de Uso

### Research y Academia
- Estudios de mercado en e-commerce
- Análisis de emprendedoras digitales
- Investigación de ecosistemas startup

### Reclutamiento
- Focus groups de productos
- User research para apps
- Beta testers de herramientas

### Marketing
- Base de datos para outreach
- Identificación de influencers
- Análisis de competencia

---

## ✅ Checklist de Setup

Para nuevos usuarios:

- [ ] Python 3.8+ instalado
- [ ] Git instalado (opcional)
- [ ] Cuenta de GitHub creada
- [ ] Repositorio clonado/forked
- [ ] Dependencias instaladas
- [ ] App probada localmente
- [ ] Deploy en Streamlit Cloud completado
- [ ] URL personalizada configurada
- [ ] README personalizado con tu info

---

## 🚀 Deploy Rápido

```bash
# 1 minuto setup
git clone https://github.com/TU-USUARIO/scraper-tiendanube.git
cd scraper-tiendanube
pip install -r requirements.txt
streamlit run app.py

# Deploy en cloud: https://share.streamlit.io
# Connect GitHub → Select repo → Deploy!
```

---

## 💡 Tips y Trucos

### Mejorar Tasa de Éxito de Emails
1. Usar Hunter.io después del scraping
2. Buscar en bio de Instagram
3. Revisar página de contacto manualmente

### Optimizar Velocidad
- Scrapear en lotes de 50-100
- Usar URLs de alta calidad
- Filtrar por nicho antes de scrapear

### Mantener Datos Actualizados
- Re-scrapear cada 2-3 meses
- Verificar Instagrams activos
- Validar emails periódicamente

---

## 📚 Documentación Adicional

- [Guía de Deployment](DEPLOYMENT.md)
- [Quick Start Guide](QUICK_START.md)
- [Troubleshooting](TROUBLESHOOTING.md)

---

## 🎉 ¡Empecemos!

**👉 [Abrir App en Streamlit](https://TU-USUARIO-scraper-tiendanube.streamlit.app)**

---

<div align="center">

**Hecho con ❤️ para la comunidad de e-commerce**

⭐ Si te fue útil, deja una estrella en el repo

</div>