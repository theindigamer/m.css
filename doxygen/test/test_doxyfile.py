import unittest

from dox2html5 import parse_doxyfile, State

class Doxyfile(unittest.TestCase):
    def test(self):
        state = State()
        parse_doxyfile(state, 'test/doxyfile/Doxyfile')
        self.assertEqual(state.doxyfile, {
            'HTML_EXTRA_FILES': ['css', 'another.png', 'hello'],
            'HTML_EXTRA_STYLESHEET': ['a.css', 'b.css'],
            'HTML_OUTPUT': 'html',
            'IMAGE_PATH': [],
            'M_CLASS_TREE_EXPAND_LEVELS': 1,
            'M_EXPAND_INNER_TYPES': 0,
            'M_FILE_TREE_EXPAND_LEVELS': 1,
            'M_THEME_COLOR': '#22272e',
            'OUTPUT_DIRECTORY': '',
            'PROJECT_BRIEF': 'is cool',
            'PROJECT_NAME': 'My Project',
            'XML_OUTPUT': 'xml'
        })

if __name__ == '__main__':
    unittest.main()
