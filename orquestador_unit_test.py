import unittest
from unittest.mock import patch, MagicMock
from orquestador import main

class TestScript(unittest.TestCase):
    @patch('builtins.print')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="sources:\n  - type: ftp\n    host: example.com\n    protocol: ftp\n    username: user\n    password: password\n    path: /remote/path\n    dataset: dataset\n    table_name: table\n")
    def test_main(self, mock_open, mock_print):
        # Simula el comportamiento del módulo DataNavigator
        mock_data_navigator = MagicMock()
        mock_data_navigator.find_by_dataset_tablename_date.return_value = [{'data': 'value'}]
        mock_data_navigator.find_by_query.return_value = [{'result': 'item'}]
        mock_data_navigator.collection.insert_many.return_value = None
        mock_data_navigator.db.__getitem__.return_value = mock_data_navigator.collection
        
        with unittest.mock.patch.dict('sys.modules', {'data_navigation': mock_data_navigator}):
            main()

        # Agrega aquí las afirmaciones para verificar la salida esperada
        # Por ejemplo, verificar que se haya llamado a print con los datos esperados

if __name__ == "__main__":
    unittest.main()
