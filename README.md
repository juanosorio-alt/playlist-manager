# Playlist Manager

A Python Streamlit application backed by a custom doubly linked list.

## Live application

[Open Playlist Manager](https://playlist-manager-mxqymdcwmqutxzfla6vuz2.streamlit.app)

## Features

- Add a track with a title and artist.
- Remove a track or select the current track.
- Move to the next or previous track.
- Reorder tracks using Move up and Move down.

Navigation stops at the ends of the playlist; it does not wrap around. Removing the current track selects the next track, or the previous track if there is no next track. Duplicate titles are supported through unique track IDs. Blank titles and artists are rejected.

Tracks are stored for the current Streamlit session. The application does not provide permanent storage or audio playback.

## Run locally in PyCharm

Open this folder as a separate project and select Python 3.10 or later. Run these commands in the PyCharm terminal:

```sh
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL printed in the terminal. Press Ctrl+C to stop the application.

## Tests

```sh
python -m unittest -v
```

The four test methods cover navigation boundaries, all source/destination combinations for reordering playlists of one through six tracks, removal at every position with different current tracks, reuse after emptying, invalid input, and duplicate titles. They also verify forward and backward links.

To check the interface manually, add three tracks, select one, navigate in both directions, move tracks up and down, and remove tracks until the playlist is empty.

## Project structure

- `playlist.py`: Track, Node, and the custom Playlist implementation.
- `app.py`: Streamlit interface and session state.
- `test_playlist.py`: automated tests using unittest.
- `requirements.txt`: application dependency.

## Linked list design

Each Node stores a track and two references: prev and next. Playlist maintains head, tail, current, and size. Tracks are stored in linked nodes rather than a Python list.

Reordering detaches and reconnects the actual node. The current reference continues to point to the same track. The `_detach` method updates neighboring links and the head or tail when necessary.

`st.session_state` preserves the Playlist object between interface reruns within the same session. Button callbacks update the playlist before Streamlit redraws the interface.

### Complexity

Adding a track and moving to the next or previous track take O(1) time. Finding, selecting, removing by ID, and reordering take O(n) time because the node must be located. Updating links for an already located node takes O(1). Traversal takes O(n), and storage takes O(n).

## Code defense preparation

Be ready to draw three connected nodes and explain head, tail, and current. Show how removing the middle node or moving the last node to the front changes prev and next. Explain why unique IDs support duplicate titles and why Streamlit session state is necessary.

## GitHub and commit history

Save meaningful commits for actual changes as the project develops. Describe the initial implementation honestly and record subsequent testing, fixes, and improvements. Do not include .venv, .idea, or __pycache__ in the repository.

## Deployment

1. Push the project files to GitHub.
2. Sign in to Streamlit Community Cloud and select Create app.
3. Select the repository, its branch, and `app.py` as the entrypoint.
4. Deploy and test adding, removing, navigating, and reordering tracks at the public URL.
5. Keep the live application link above up to date.

[Official deployment documentation](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy)

## Validation status

The included logic tests pass. The live application URL is listed above. Verify the English interface and all actions on the deployed application after uploading this version.
