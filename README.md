# Playlist Manager

Aplicación Python con Streamlit y una lista doblemente enlazada propia.

## Aplicación publicada
[Abre Playlist Manager](https://playlist-manager-mxqymdcwmqutxzfla6vuz2.streamlit.app)

## Ejecutar en PyCharm
Abre esta carpeta como un proyecto separado y selecciona Python 3.10 o posterior. En la terminal de PyCharm ejecuta:

```sh
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Abre la dirección local que aparece en la terminal. Para detener la aplicación, presiona Ctrl+C.

## Pruebas

```sh
python -m unittest -v
```

Las cuatro pruebas propias incluyen navegación y límites, todas las combinaciones de movimiento para listas de 1 a 6 canciones, eliminación en cada posición con distintas canciones actuales, reutilización, entradas inválidas y duplicados. Verifican también los enlaces anteriores y posteriores. La interfaz debe comprobarse manualmente: agregar tres canciones, seleccionar una, avanzar/retroceder, subir/bajar y eliminar hasta vaciar la playlist.

## Funciones
Agregar título y artista, eliminar canciones, seleccionar la actual, avanzar/retroceder y reordenar mediante Subir/Bajar. Los botones se desactivan en los extremos. No hay salto circular. Al eliminar la canción actual se selecciona la siguiente o, si no existe, la anterior.

Las canciones duplicadas se distinguen con identificadores únicos. Los campos vacíos se rechazan. Los datos viven en la sesión de Streamlit; no hay almacenamiento permanente ni reproducción de audio.

## Estructura y defensa del código
- `playlist.py`: Track representa una canción. Node contiene track, prev y next. Playlist mantiene head, tail, current y size.
- `app.py`: interfaz. `st.session_state` conserva la playlist entre ejecuciones de la interfaz en la misma sesión. Los callbacks modifican la playlist antes de redibujarla.
- `test_playlist.py`: pruebas con unittest, independientes de Streamlit.

La playlist almacena sus elementos mediante nodos enlazados. Al reordenar se desconecta y reconecta el nodo real; la referencia current permanece en la misma canción. `_detach` actualiza los vecinos y los extremos. Se permiten títulos repetidos porque las operaciones identifican las canciones por ID.

Agregar y avanzar/retroceder cuestan O(1). Buscar por ID, seleccionar, eliminar por ID y mover cuestan O(n); cambiar los enlaces de un nodo ya localizado cuesta O(1). Recorrer toda la playlist cuesta O(n). El espacio es O(n).

Para la defensa, practica dibujar tres nodos, explicar head/tail/current, eliminar el nodo central y mover el último al principio actualizando prev y next. Explica también por qué la interfaz usa session_state.

## GitHub e historial
Crea un repositorio llamado `playlist-manager` y conecta este proyecto con él. Guarda un primer commit que describa honestamente esta versión inicial. A medida que revises, pruebes y mejores el proyecto, guarda commits de esos cambios reales. No inventes un historial retrospectivo. No subas .venv, .idea ni __pycache__.

## Publicar
1. Sube los archivos del proyecto al repositorio de GitHub.
2. En https://share.streamlit.io conecta tu cuenta de GitHub y selecciona Create app.
3. Selecciona tu repositorio, la rama correspondiente y `app.py` como archivo principal.
4. Despliega y comprueba agregar, eliminar, navegar y reordenar en la URL pública.
5. Copia esa URL en la sección Aplicación publicada de este README y guarda el cambio en GitHub.

Documentación oficial: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

## Estado de entrega
La lógica fue validada con las pruebas incluidas. El despliegue y la comprobación de la interfaz publicada están pendientes. El requisito de publicación solo estará cumplido cuando exista una URL funcional en este README.
