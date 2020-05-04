import os
import sys
import unittest

sys.path.append('modules')
from workbench_utils import execute_bootstrap_script


class TestExecuteBootstrapScript(unittest.TestCase):

    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        self.script_path = os.path.join(dir_path, 'assets', 'execute_bootstrap_script_test', 'script.py')
        self.config_file_path = os.path.join(dir_path, 'assets', 'execute_bootstrap_script_test', 'config.yml')

    def test_python_script(self):
        output, return_code = execute_bootstrap_script(self.script_path, self.config_file_path)
        self.assertEqual(output.strip(), b'Hello')


if __name__ == '__main__':
    unittest.main()
