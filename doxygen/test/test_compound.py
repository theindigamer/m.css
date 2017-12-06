import os
import unittest

from test import IntegrationTestCase

class Listing(IntegrationTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(__file__, 'listing', *args, **kwargs)

    def test_index_pages(self):
        self.run_dox2html5(wildcard='index.xml', index_pages=['annotated', 'namespaces'])
        self.assertEqual(*self.expected_actual_contents('annotated.html'))
        self.assertEqual(*self.expected_actual_contents('namespaces.html'))

    def test_index_pages_custom_expand_level(self):
        self.run_dox2html5(wildcard='index.xml', index_pages=['files'])
        self.assertEqual(*self.expected_actual_contents('files.html'))

    def test_dir(self):
        self.run_dox2html5(wildcard='dir_*.xml')
        self.assertEqual(*self.expected_actual_contents('dir_4b0d5f8864bf89936129251a2d32609b.html'))
        self.assertEqual(*self.expected_actual_contents('dir_bbe5918fe090eee9db2d9952314b6754.html'))

    def test_file(self):
        self.run_dox2html5(wildcard='*_8h.xml')
        self.assertEqual(*self.expected_actual_contents('File_8h.html'))
        self.assertEqual(*self.expected_actual_contents('Class_8h.html'))

    @unittest.expectedFailure
    def test_empty_file_doc_not_generated(self):
        self.run_dox2html5(wildcard='Root_8h.xml')
        self.assertFalse(os.path.exists(os.path.join(self.path, 'html', 'Root_8h.html')))

    def test_namespace(self):
        self.run_dox2html5(wildcard='namespaceRoot_1_1Directory.xml')
        self.assertEqual(*self.expected_actual_contents('namespaceRoot_1_1Directory.html'))

    def test_namespace_empty(self):
        self.run_dox2html5(wildcard='namespaceAnother.xml')
        self.assertEqual(*self.expected_actual_contents('namespaceAnother.html'))

    def test_class(self):
        self.run_dox2html5(wildcard='classRoot_1_1Directory_1_1Sub_1_1Class.xml')
        self.assertEqual(*self.expected_actual_contents('classRoot_1_1Directory_1_1Sub_1_1Class.html'))

    @unittest.expectedFailure
    def test_empty_class_doc_not_generated(self):
        self.run_dox2html5(wildcard='union*Bar*.xml')
        self.assertFalse(os.path.exists(os.path.join(self.path, 'html', 'unionRoot_1_1Directory_1_1Sub_1_1Class_1_1Bar.html')))

    def test_page_toc(self):
        self.run_dox2html5(wildcard='page-toc.xml')
        self.assertEqual(*self.expected_actual_contents('page-toc.html'))

    def test_page_no_toc(self):
        self.run_dox2html5(wildcard='page-no-toc.xml')
        self.assertEqual(*self.expected_actual_contents('page-no-toc.html'))

class Detailed(IntegrationTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(__file__, 'detailed', *args, **kwargs)

    def test_namespace(self):
        self.run_dox2html5(wildcard='namespaceNamee.xml')
        self.assertEqual(*self.expected_actual_contents('namespaceNamee.html'))

    def test_class_template(self):
        self.run_dox2html5(wildcard='structTemplate.xml')
        self.assertEqual(*self.expected_actual_contents('structTemplate.html'))

    def test_class_template_specialized(self):
        self.run_dox2html5(wildcard='structTemplate_3_01void_01_4.xml')
        self.assertEqual(*self.expected_actual_contents('structTemplate_3_01void_01_4.html'))

    def test_class_template_warnings(self):
        self.run_dox2html5(wildcard='structTemplateWarning.xml')
        self.assertEqual(*self.expected_actual_contents('structTemplateWarning.html'))

    def test_function(self):
        self.run_dox2html5(wildcard='namespaceFoo.xml')
        self.assertEqual(*self.expected_actual_contents('namespaceFoo.html'))

    def test_enum(self):
        self.run_dox2html5(wildcard='namespaceEno.xml')
        self.assertEqual(*self.expected_actual_contents('namespaceEno.html'))

    def test_function_enum_warnings(self):
        self.run_dox2html5(wildcard='namespaceWarning.xml')
        self.assertEqual(*self.expected_actual_contents('namespaceWarning.html'))

    def test_typedef(self):
        self.run_dox2html5(wildcard='namespaceType.xml')
        self.assertEqual(*self.expected_actual_contents('namespaceType.html'))

    def test_var(self):
        self.run_dox2html5(wildcard='namespaceVar.xml')
        self.assertEqual(*self.expected_actual_contents('namespaceVar.html'))

    def test_define(self):
        self.run_dox2html5(wildcard='File_8h.xml')
        self.assertEqual(*self.expected_actual_contents('File_8h.html'))

if __name__ == '__main__':
    unittest.main()
