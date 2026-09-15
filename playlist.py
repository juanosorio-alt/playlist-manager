"""Playlist stored in a custom doubly linked list."""
from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Track:
    id: str
    title: str
    artist: str


class Node:
    def __init__(self, track):
        self.track = track
        self.prev = None
        self.next = None


class Playlist:
    def __init__(self):
        self.head = self.tail = self.current = None
        self.size = 0

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.track
            node = node.next

    def _find(self, track_id):
        node = self.head
        while node is not None:
            if node.track.id == track_id:
                return node
            node = node.next
        raise ValueError('Track not found')

    def add(self, title, artist):
        title, artist = title.strip(), artist.strip()
        if not title or not artist:
            raise ValueError('Enter both a title and an artist.')
        node = Node(Track(uuid4().hex, title, artist))
        node.prev = self.tail
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        if self.current is None:
            self.current = node
        self.size += 1
        return node.track.id

    def _detach(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        node.prev = node.next = None

    def remove(self, track_id):
        node = self._find(track_id)
        if self.current is node:
            self.current = node.next or node.prev
        self._detach(node)
        self.size -= 1

    def select(self, track_id):
        self.current = self._find(track_id)

    def next_track(self):
        if self.current is not None and self.current.next is not None:
            self.current = self.current.next

    def previous_track(self):
        if self.current is not None and self.current.prev is not None:
            self.current = self.current.prev

    def move(self, track_id, position):
        """Move the actual node to a zero-based final position."""
        if not 0 <= position < self.size:
            raise IndexError('Position out of range')
        node = self._find(track_id)
        self._detach(node)
        target = self.head
        for _ in range(position):
            target = target.next
        if target is None:
            node.prev = self.tail
            if self.tail is None:
                self.head = node
            else:
                self.tail.next = node
            self.tail = node
        else:
            node.prev, node.next = target.prev, target
            if target.prev is None:
                self.head = node
            else:
                target.prev.next = node
            target.prev = node
