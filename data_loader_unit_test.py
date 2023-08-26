import unittest
from unittest.mock import patch
from data_loader import SourceLoader

class TestSourceLoader(unittest.TestCase):
    def setUp(self):
        self.sources_config = [
            # Configuración de fuentes de ejemplo
            {
                'type': 'ftp',
                'host': 'example.com',
                'protocol': 'ftp',
                'username': 'user',
                'password': 'password',
                'path': '/remote/path',
                'dataset': 'dataset',
                'table_name': 'table',
            },
            {
                'type': 'mysql',
                'host': 'localhost',
                'port': 3306,
                'username': 'user',
                'password': 'password',
                'database': 'database',
                'query': 'SELECT * FROM table',
                'dataset': 'dataset',
                'table_name': 'table',
            }
        ]
    
    @patch('builtins.print')
    def test_load_ftp(self, mock_print):
        source_loader = SourceLoader(self.sources_config)
        source_loader.load_ftp(self.sources_config[0])
        # Verifica que se haya llamado a print con el mensaje esperado
        
    def test_load_mysql(self):
        source_loader = SourceLoader(self.sources_config)
        # Agrega pruebas para cargar datos desde MySQL
        # Puedes utilizar una base de datos de prueba o mocks
    
    # Agrega más pruebas según tus necesidades

if __name__ == "__main__":
    unittest.main()
