import streamlit as st
from playlist import Playlist

st.set_page_config(page_title='Playlist Manager', page_icon='🎵')
if 'playlist' not in st.session_state:
    st.session_state.playlist = Playlist()
p = st.session_state.playlist
st.title('🎵 Playlist Manager')
st.caption('Organize your tracks and browse your playlist.')

with st.form('add_track', clear_on_submit=True):
    title = st.text_input('Title')
    artist = st.text_input('Artist')
    if st.form_submit_button('Add track'):
        try:
            p.add(title, artist)
            st.success('Track added.')
        except ValueError as error:
            st.error(str(error))

st.subheader('Current track')
if p.current is None:
    st.info('Add a track to get started.')
else:
    st.write(f'{p.current.track.title} — {p.current.track.artist}')
left, right = st.columns(2)
left.button('← Previous', on_click=p.previous_track,
            disabled=p.current is None or p.current.prev is None)
right.button('Next →', on_click=p.next_track,
             disabled=p.current is None or p.current.next is None)
st.subheader(f'Your playlist · {p.size} tracks')
for index, track in enumerate(p):
    with st.container(border=True):
        marker = '▶ ' if p.current.track.id == track.id else ''
        st.write(f'{marker}{index + 1}. {track.title} — {track.artist}')
        a, b, c, d = st.columns(4)
        a.button('Select', key=f's{track.id}', on_click=p.select, args=(track.id,))
        b.button('Move up ↑', key=f'u{track.id}', on_click=p.move,
                 args=(track.id, index - 1), disabled=index == 0)
        c.button('Move down ↓', key=f'd{track.id}', on_click=p.move,
                 args=(track.id, index + 1), disabled=index == p.size - 1)
        d.button('Remove', key=f'r{track.id}', on_click=p.remove, args=(track.id,))
st.caption('Tracks are kept during this session. This app organizes tracks; it does not play audio.')
