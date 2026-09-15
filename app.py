import streamlit as st
from playlist import Playlist

st.set_page_config(page_title='Playlist Manager', page_icon='🎵')
if 'playlist' not in st.session_state:
    st.session_state.playlist = Playlist()
p = st.session_state.playlist
st.title('🎵 Playlist Manager')
st.caption('Organiza tus canciones y recorre tu playlist.')

with st.form('add_track', clear_on_submit=True):
    title = st.text_input('Título')
    artist = st.text_input('Artista')
    if st.form_submit_button('Agregar canción'):
        try:
            p.add(title, artist)
            st.success('Canción agregada.')
        except ValueError as error:
            st.error(str(error))

st.subheader('Canción actual')
if p.current is None:
    st.info('Agrega una canción para empezar.')
else:
    st.write(f'{p.current.track.title} — {p.current.track.artist}')
left, right = st.columns(2)
left.button('← Anterior', on_click=p.previous_track,
            disabled=p.current is None or p.current.prev is None)
right.button('Siguiente →', on_click=p.next_track,
             disabled=p.current is None or p.current.next is None)
st.subheader(f'Tu playlist · {p.size} canciones')
for index, track in enumerate(p):
    with st.container(border=True):
        marker = '▶ ' if p.current.track.id == track.id else ''
        st.write(f'{marker}{index + 1}. {track.title} — {track.artist}')
        a, b, c, d = st.columns(4)
        a.button('Seleccionar', key=f's{track.id}', on_click=p.select, args=(track.id,))
        b.button('Subir ↑', key=f'u{track.id}', on_click=p.move,
                 args=(track.id, index - 1), disabled=index == 0)
        c.button('Bajar ↓', key=f'd{track.id}', on_click=p.move,
                 args=(track.id, index + 1), disabled=index == p.size - 1)
        d.button('Eliminar', key=f'r{track.id}', on_click=p.remove, args=(track.id,))
st.caption('Los datos se mantienen durante la sesión. Esta aplicación organiza canciones; no reproduce audio.')
