"""
Scraper Tiendanube - Streamlit App
Ejecutar: streamlit run app.py
"""

import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
from datetime import datetime
import io
import json

# Configuración de página
st.set_page_config(
    page_title="Scraper Tiendanube",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
    <style>
    .main {background-color: #f5f7fa;}
    .stProgress > div > div > div > div {background-color: #4CAF50;}
    </style>
    """, unsafe_allow_html=True)

# Clase para buscar URLs
class URLSearcher:
    """Busca URLs de Tiendanube usando diferentes métodos"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def search_with_serper(self, query, num_results=10, api_key=None):
        """Busca usando Serper API (https://serper.dev) - RECOMENDADO"""
        if not api_key:
            return None, "Se requiere API key de Serper"
        
        try:
            all_urls = []
            max_per_request = 10  # Serper limita a 10 por request
            num_requests = (num_results + max_per_request - 1) // max_per_request  # Redondeo hacia arriba
            
            for page in range(num_requests):
                url = "https://google.serper.dev/search"
                payload = json.dumps({
                    "q": query,
                    "num": min(max_per_request, num_results - len(all_urls)),
                    "page": page + 1  # Página actual
                })
                headers = {
                    'X-API-KEY': api_key,
                    'Content-Type': 'application/json'
                }
                
                response = requests.post(url, headers=headers, data=payload, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # Extraer URLs orgánicas
                    if 'organic' in data:
                        for result in data['organic']:
                            url_found = result.get('link', '')
                            if 'mitiendanube.com' in url_found and url_found not in all_urls:
                                all_urls.append(url_found)
                                
                                # Si ya tenemos suficientes, salir
                                if len(all_urls) >= num_results:
                                    return all_urls, None
                    
                    # Si no hay más resultados, salir
                    if not data.get('organic'):
                        break
                    
                    # Pequeña pausa entre requests
                    if page < num_requests - 1:
                        time.sleep(0.5)
                else:
                    # Si falla en la primera página, retornar error
                    if page == 0:
                        return None, f"Error API: {response.status_code}"
                    # Si falla en páginas siguientes, retornar lo que tenemos
                    break
            
            if all_urls:
                return all_urls, None
            else:
                return None, "No se encontraron URLs"
                
        except Exception as e:
            return None, f"Error: {str(e)}"
    
    def search_with_serpapi(self, query, num_results=10, api_key=None):
        """Busca usando SerpAPI (https://serpapi.com)"""
        if not api_key:
            return None, "Se requiere API key de SerpAPI"
        
        try:
            all_urls = []
            max_per_request = 10
            num_requests = (num_results + max_per_request - 1) // max_per_request
            
            for page in range(num_requests):
                params = {
                    'q': query,
                    'api_key': api_key,
                    'num': min(max_per_request, num_results - len(all_urls)),
                    'start': page * max_per_request,
                    'engine': 'google'
                }
                
                response = requests.get('https://serpapi.com/search', params=params, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    if 'organic_results' in data:
                        for result in data['organic_results']:
                            url_found = result.get('link', '')
                            if 'mitiendanube.com' in url_found and url_found not in all_urls:
                                all_urls.append(url_found)
                                
                                if len(all_urls) >= num_results:
                                    return all_urls, None
                    
                    if not data.get('organic_results'):
                        break
                    
                    if page < num_requests - 1:
                        time.sleep(0.5)
                else:
                    if page == 0:
                        return None, f"Error API: {response.status_code}"
                    break
            
            if all_urls:
                return all_urls, None
            else:
                return None, "No se encontraron URLs"
                
        except Exception as e:
            return None, f"Error: {str(e)}"
    
    def search_with_duckduckgo(self, query, num_results=10):
        """Busca usando DuckDuckGo (sin API, menos confiable pero gratis)"""
        try:
            from duckduckgo_search import DDGS
            
            urls = []
            with DDGS() as ddgs:
                results = ddgs.text(query, max_results=num_results)
                for result in results:
                    url = result.get('href', '')
                    if 'mitiendanube.com' in url:
                        urls.append(url)
            
            return urls, None
            
        except ImportError:
            return None, "Instalar: pip install duckduckgo-search"
        except Exception as e:
            return None, f"Error: {str(e)}"
    
    def validate_tiendanube_url(self, url):
        """Valida que sea una URL válida de Tiendanube"""
        pattern = r'https?://[a-zA-Z0-9-]+\.mitiendanube\.com/?'
        return bool(re.match(pattern, url))

# Clase Scraper
class TiendaNubeScraper:
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def scrape_tienda(self, url):
        try:
            if not url.startswith('http'):
                url = 'https://' + url
            
            response = self.session.get(url, timeout=15)
            if response.status_code != 200:
                return None
            
            soup = BeautifulSoup(response.text, 'html.parser')
            texto = soup.get_text()
            
            title = soup.find('title')
            nombre = title.text.strip() if title else url.split('//')[1].split('.')[0]
            
            meta = soup.find('meta', attrs={'name': 'description'})
            descripcion = meta.get('content', '')[:200] if meta else ''
            
            instagram = self._extraer_instagram(soup, texto)
            email = self._extraer_email(soup, texto)
            whatsapp = self._extraer_whatsapp(soup, texto)
            facebook = self._extraer_facebook(soup)
            nicho = self._clasificar_nicho(nombre + ' ' + descripcion)
            
            return {
                'url': url,
                'nombre_tienda': nombre,
                'descripcion': descripcion,
                'nicho': nicho,
                'instagram': instagram,
                'facebook': facebook,
                'email': email,
                'whatsapp': whatsapp,
                'fecha_scraping': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'estado': 'Activa'
            }
        except:
            return None
        finally:
            time.sleep(1.5)
    
    def _extraer_instagram(self, soup, texto):
        for link in soup.find_all('a', href=True):
            if 'instagram.com' in link['href']:
                return link['href'].split('?')[0]
        match = re.search(r'instagram\.com/([a-zA-Z0-9._]+)', texto)
        if match:
            return f"https://instagram.com/{match.group(1)}"
        return None
    
    def _extraer_email(self, soup, texto):
        mailto = soup.find('a', href=re.compile(r'mailto:'))
        if mailto:
            return mailto['href'].replace('mailto:', '').strip()
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)
        for email in emails:
            if not any(x in email.lower() for x in ['noreply', 'example', 'test']):
                return email
        return None
    
    def _extraer_whatsapp(self, soup, texto):
        for link in soup.find_all('a', href=True):
            if 'wa.me' in link['href'] or 'whatsapp.com' in link['href']:
                match = re.search(r'\d{10,15}', link['href'])
                if match:
                    return match.group(0)
        texto_limpio = texto.replace(' ', '').replace('-', '')
        match = re.search(r'\+?549?11\d{8}', texto_limpio)
        if match:
            return match.group(0)
        return None
    
    def _extraer_facebook(self, soup):
        for link in soup.find_all('a', href=True):
            if 'facebook.com' in link['href'] and 'sharer' not in link['href']:
                return link['href'].split('?')[0]
        return None
    
    def _clasificar_nicho(self, texto):
        texto = texto.lower()
        if any(w in texto for w in ['maquillaje', 'makeup', 'labial', 'cosmetic']):
            return 'Belleza - Maquillaje'
        elif any(w in texto for w in ['joya', 'joyeria', 'anillo', 'arete']):
            return 'Joyería'
        elif any(w in texto for w in ['bijou', 'fantasia']):
            return 'Bijouterie'
        elif any(w in texto for w in ['ropa', 'vestido', 'blusa', 'moda']):
            return 'Moda - Ropa'
        elif any(w in texto for w in ['cartera', 'bolso', 'accesorio']):
            return 'Accesorios'
        return 'Otro'

# Función para convertir DataFrame a CSV descargable
@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')

# Interfaz principal
def main():
    
    # Header
    st.title("🚀 Scraper de Tiendanube")
    st.markdown("### Encuentra y extrae datos de contacto de tiendas de moda y belleza")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.image("https://via.placeholder.com/300x100/4CAF50/FFFFFF?text=Tiendanube+Scraper", use_container_width=True)
        st.markdown("## ⚙️ Configuración")
        
        modo = st.radio(
            "Selecciona modo:",
            ["🔍 Buscar URLs en Google", "📝 Ingresar URLs manualmente", "📂 Subir archivo .txt", "🧪 Usar URLs de prueba"]
        )
        
        # Configuración de búsqueda
        if modo == "🔍 Buscar URLs en Google":
            st.markdown("---")
            st.markdown("### 🔑 API Configuration")
            
            api_service = st.selectbox(
                "Servicio:",
                ["Serper (Recomendado)", "SerpAPI", "DuckDuckGo (Gratis, limitado)"],
                help="Serper: 10 resultados por búsqueda | SerpAPI: Hasta 100 por búsqueda | DuckDuckGo: Gratis pero limitado"
            )
            
            api_key = None
            if api_service != "DuckDuckGo (Gratis, limitado)":
                api_key = st.text_input(
                    "API Key:",
                    type="password",
                    help=f"Obtén tu clave en: {'https://serper.dev' if 'Serper' in api_service else 'https://serpapi.com'}"
                )
        
        st.markdown("---")
        st.markdown("### 📊 Estadísticas esperadas")
        st.info("✅ Instagram: 70-90%\n\n✅ WhatsApp: 40-60%\n\n✅ Email: 20-40%")
        
        st.markdown("---")
        st.markdown("### ℹ️ Información")
        st.markdown("**Versión:** 2.0.0")
        st.markdown("**Autor:** Growth Team")
    
    # Main content
    urls_a_procesar = []
    
    if modo == "🔍 Buscar URLs en Google":
        st.markdown("### 🔍 Búsqueda de URLs")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            search_query = st.text_input(
                "Consulta de búsqueda:",
                value="site:mitiendanube.com moda mujer",
                help="Usa 'site:mitiendanube.com' seguido de palabras clave"
            )
        
        with col2:
            num_results = st.number_input(
                "Cantidad de URLs:",
                min_value=5,
                max_value=100,
                value=20,
                step=5
            )
        
        st.markdown("**💡 Ejemplos de búsqueda:**")
        ejemplos = st.expander("Ver ejemplos")
        with ejemplos:
            st.code("site:mitiendanube.com moda mujer")
            st.code("site:mitiendanube.com joyería artesanal")
            st.code("site:mitiendanube.com maquillaje belleza")
            st.code("site:mitiendanube.com accesorios colombia")
        
        if st.button("🔎 Buscar URLs", type="primary"):
            if not search_query:
                st.error("❌ Ingresa una consulta de búsqueda")
            elif api_service != "DuckDuckGo (Gratis, limitado)" and not api_key:
                st.error("❌ Ingresa tu API Key")
            else:
                with st.spinner(f"🔍 Buscando URLs con {api_service}..."):
                    searcher = URLSearcher()
                    
                    # Mostrar progreso
                    progress_text = st.empty()
                    
                    # Seleccionar método de búsqueda
                    if api_service == "Serper (Recomendado)":
                        progress_text.text(f"🔍 Buscando en Google... (puede tardar unos segundos para {num_results} URLs)")
                        urls, error = searcher.search_with_serper(search_query, num_results, api_key)
                    elif api_service == "SerpAPI":
                        progress_text.text(f"🔍 Buscando en Google... (puede tardar unos segundos para {num_results} URLs)")
                        urls, error = searcher.search_with_serpapi(search_query, num_results, api_key)
                    else:
                        progress_text.text("🔍 Buscando con DuckDuckGo...")
                        urls, error = searcher.search_with_duckduckgo(search_query, num_results)
                    
                    progress_text.empty()
                    
                    if error:
                        st.error(f"❌ {error}")
                    elif urls:
                        urls_a_procesar = list(set(urls))  # Eliminar duplicados
                        st.success(f"✅ Se encontraron {len(urls_a_procesar)} URLs únicas")
                        
                        # Guardar en session state
                        st.session_state['urls_encontradas'] = urls_a_procesar
                        st.session_state['search_query'] = search_query
                        
                        with st.expander("🔗 Ver URLs encontradas"):
                            for i, url in enumerate(urls_a_procesar, 1):
                                st.text(f"{i}. {url}")
                    else:
                        st.warning("⚠️ No se encontraron URLs con esa búsqueda. Intenta con otras palabras clave.")
        
        # Usar URLs guardadas
        if 'urls_encontradas' in st.session_state:
            urls_a_procesar = st.session_state['urls_encontradas']
            st.info(f"📦 {len(urls_a_procesar)} URLs listas para scrapear (búsqueda: '{st.session_state.get('search_query', '')}')")
    
    elif modo == "📝 Ingresar URLs manualmente":
        st.markdown("### 📝 Ingresa las URLs")
        st.markdown("Una URL por línea (ejemplo: `https://tienda.mitiendanube.com`)")
        
        urls_text = st.text_area(
            "URLs de Tiendanube:",
            height=200,
            placeholder="https://beautymakeup.mitiendanube.com\nhttps://modafashion.mitiendanube.com\nhttps://joyasarte.mitiendanube.com"
        )
        
        if urls_text:
            urls_a_procesar = [url.strip() for url in urls_text.split('\n') 
                             if url.strip() and 'mitiendanube.com' in url]
            st.success(f"✅ {len(urls_a_procesar)} URLs detectadas")
    
    elif modo == "📂 Subir archivo .txt":
        st.markdown("### 📂 Sube tu archivo")
        uploaded_file = st.file_uploader("Archivo .txt con URLs (una por línea)", type=['txt'])
        
        if uploaded_file:
            contenido = uploaded_file.read().decode('utf-8')
            urls_a_procesar = [url.strip() for url in contenido.split('\n') 
                             if url.strip() and 'mitiendanube.com' in url]
            st.success(f"✅ {len(urls_a_procesar)} URLs cargadas desde archivo")
            
            with st.expander("Ver URLs cargadas"):
                for i, url in enumerate(urls_a_procesar[:10], 1):
                    st.text(f"{i}. {url}")
                if len(urls_a_procesar) > 10:
                    st.text(f"... y {len(urls_a_procesar) - 10} más")
    
    else:  # URLs de prueba
        urls_a_procesar = [
            'https://beautymakeupok.mitiendanube.com',
            'https://cherrybomb9.mitiendanube.com',
            'https://kohphangan2.mitiendanube.com',
            'https://alphajoyas.mitiendanube.com',
            'https://moodindumentaria.mitiendanube.com'
        ]
        st.info(f"🧪 Usando {len(urls_a_procesar)} URLs de prueba")
        with st.expander("Ver URLs de prueba"):
            for url in urls_a_procesar:
                st.text(f"• {url}")
    
    st.markdown("---")
    
    # Botón de scraping
    if urls_a_procesar:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Iniciar Scraping", type="primary", use_container_width=True):
                
                # Progress bar
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Contenedor de resultados en tiempo real
                results_container = st.container()
                
                scraper = TiendaNubeScraper()
                resultados = []
                
                for i, url in enumerate(urls_a_procesar):
                    status_text.text(f"Procesando {i+1}/{len(urls_a_procesar)}: {url[:50]}...")
                    
                    resultado = scraper.scrape_tienda(url)
                    if resultado:
                        resultados.append(resultado)
                        
                        with results_container:
                            cols = st.columns([3, 1, 1, 1])
                            cols[0].text(f"✅ {resultado['nombre_tienda'][:30]}")
                            cols[1].text("✓" if resultado['instagram'] else "✗")
                            cols[2].text("✓" if resultado['email'] else "✗")
                            cols[3].text("✓" if resultado['whatsapp'] else "✗")
                    
                    progress_bar.progress((i + 1) / len(urls_a_procesar))
                
                status_text.text("✅ Scraping completado!")
                
                if resultados:
                    df = pd.DataFrame(resultados)
                    
                    # Calcular score
                    df['score_contacto'] = (
                        df['instagram'].notna().astype(int) * 3 +
                        df['whatsapp'].notna().astype(int) * 2 +
                        df['email'].notna().astype(int) * 2 +
                        df['facebook'].notna().astype(int) * 1
                    )
                    
                    df = df.sort_values('score_contacto', ascending=False)
                    
                    # Guardar en session state
                    st.session_state['df_resultados'] = df
                    st.session_state['scraping_done'] = True
                    
                    st.rerun()
    
    # Mostrar resultados si existen
    if 'scraping_done' in st.session_state and st.session_state['scraping_done']:
        df = st.session_state['df_resultados']
        
        st.markdown("---")
        st.markdown("## 📊 Resultados")
        
        # Métricas
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Tiendas", len(df))
        col2.metric("Con Instagram", df['instagram'].notna().sum())
        col3.metric("Con Email", df['email'].notna().sum())
        col4.metric("Con WhatsApp", df['whatsapp'].notna().sum())
        
        # Gráficos
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🎯 Por Nicho")
            nicho_counts = df['nicho'].value_counts()
            st.bar_chart(nicho_counts)
        
        with col2:
            st.markdown("### ⭐ Por Score de Contacto")
            score_counts = df['score_contacto'].value_counts().sort_index(ascending=False)
            st.bar_chart(score_counts)
        
        # Tabla de resultados
        st.markdown("### 📋 Datos Completos")
        
        # Filtros
        col1, col2 = st.columns(2)
        with col1:
            nichos_filter = st.multiselect(
                "Filtrar por nicho:",
                options=df['nicho'].unique(),
                default=df['nicho'].unique()
            )
        with col2:
            score_min = st.slider("Score mínimo:", 0, 8, 0)
        
        df_filtered = df[
            (df['nicho'].isin(nichos_filter)) & 
            (df['score_contacto'] >= score_min)
        ]
        
        st.dataframe(
            df_filtered[['nombre_tienda', 'nicho', 'instagram', 'email', 
                        'whatsapp', 'score_contacto']],
            use_container_width=True,
            height=400
        )
        
        # Descargas
        st.markdown("### 📥 Descargar Resultados")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            csv_completo = convert_df_to_csv(df)
            st.download_button(
                label="📄 CSV Completo",
                data=csv_completo,
                file_name=f"tiendas_completo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
        
        with col2:
            df_top = df.nlargest(min(50, len(df)), 'score_contacto')
            csv_top = convert_df_to_csv(df_top)
            st.download_button(
                label="⭐ CSV Top 50",
                data=csv_top,
                file_name=f"tiendas_top50_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
        
        with col3:
            if st.button("🔄 Nuevo Scraping"):
                st.session_state['scraping_done'] = False
                st.rerun()

if __name__ == "__main__":
    main()
