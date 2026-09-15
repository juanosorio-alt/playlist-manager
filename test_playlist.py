import unittest
from playlist import Playlist


class PlaylistTests(unittest.TestCase):
    def check(self, p, ids):
        self.assertEqual([t.id for t in p], ids)
        self.assertEqual(p.size, len(ids))
        node, previous = p.head, None
        for track_id in ids:
            self.assertIs(node.prev, previous)
            self.assertEqual(node.track.id, track_id)
            previous, node = node, node.next
        self.assertIsNone(node)
        self.assertIs(p.tail, previous)
        if ids:
            self.assertIn(p.current.track.id, ids)
        else:
            self.assertIsNone(p.current)

    def test_navigation(self):
        p = Playlist()
        p.next_track()
        p.previous_track()
        self.check(p, [])
        a, b = p.add('A', 'Artist'), p.add('B', 'Artist')
        p.previous_track()
        self.assertEqual(p.current.track.id, a)
        p.next_track()
        p.next_track()
        self.assertEqual(p.current.track.id, b)
        p.previous_track()
        self.assertEqual(p.current.track.id, a)
        p.select(b)
        self.assertEqual(p.current.track.id, b)

    def test_all_moves(self):
        for length in range(1, 7):
            for source in range(length):
                for target in range(length):
                    p = Playlist()
                    ids = [p.add(str(i), 'Artist') for i in range(length)]
                    p.select(ids[source])
                    current = p.current
                    moved = ids.pop(source)
                    ids.insert(target, moved)
                    p.move(moved, target)
                    self.check(p, ids)
                    self.assertIs(p.current, current)

    def test_all_removals(self):
        for selected in range(3):
            for removed in range(3):
                p = Playlist()
                ids = [p.add(str(i), 'Artist') for i in range(3)]
                p.select(ids[selected])
                expected_current = ids[selected]
                if selected == removed:
                    expected_current = ids[removed + 1] if removed < 2 else ids[1]
                p.remove(ids.pop(removed))
                self.check(p, ids)
                self.assertEqual(p.current.track.id, expected_current)
                for track_id in ids[:]:
                    p.remove(track_id)
                self.check(p, [])
                new = p.add('New', 'Artist')
                self.check(p, [new])

    def test_validation_and_duplicates(self):
        p = Playlist()
        for title, artist in [('', 'A'), ('A', '  ')]:
            with self.assertRaises(ValueError):
                p.add(title, artist)
        a, b = p.add(' Same ', 'Artist'), p.add('Same', 'Artist')
        self.assertNotEqual(a, b)
        self.assertEqual(p.head.track.title, 'Same')
        for position in [-1, 2]:
            with self.assertRaises(IndexError):
                p.move(a, position)
        for action in [p.remove, p.select]:
            with self.assertRaises(ValueError):
                action('missing')
        self.check(p, [a, b])


if __name__ == '__main__':
    unittest.main()
