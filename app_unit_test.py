import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, g
from flask_login import current_user
from app import app, UserController, ETLController, ProcessController

class TestApp(unittest.TestCase):
    @patch('app.render_template')
    def test_index(self, mock_render_template):
        # Simula la función current_user
        with app.test_request_context():
            with unittest.mock.patch('flask_login.current_user', MagicMock()):
                response = app.test_client().get('/')
        
        self.assertEqual(response.status_code, 200)
        mock_render_template.assert_called_once_with("index.html")
        
    @patch('app.redirect', side_effect=lambda url: url)
    @patch('app.url_for')
    @patch('app.UserController')
    @patch('app.User')
    @patch('app.db')
    def test_create_config(self, mock_db, mock_User, mock_UserController, mock_url_for, mock_redirect):
        # Simula la función current_user
        with app.test_request_context(method='POST'):
            with unittest.mock.patch('flask_login.current_user', MagicMock()):
                response = app.test_client().post('/create_config', data={'key': 'value'})
        
        self.assertEqual(response, '/')

    @patch('app.flash')
    @patch('app.redirect', side_effect=lambda url: url)
    @patch('app.url_for')
    @patch('app.ETLController')
    @patch('app.Config')
    @patch('app.Transformer')
    @patch('app.DataQualityChecker')
    @patch('app.ETLProcessor')
    @patch('app.data_navigator')
    def test_start_etl(self, mock_data_navigator, mock_ETLProcessor, mock_DataQualityChecker, mock_Transformer, mock_Config, mock_ETLController, mock_url_for, mock_redirect, mock_flash):
        # Simula la función current_user
        with app.test_request_context():
            with unittest.mock.patch('flask_login.current_user', MagicMock()):
                response = app.test_client().get('/start_etl/config_file')
        
        self.assertEqual(response, '/')
        mock_flash.assert_called_once_with("ETL process started successfully!", "success")

    @patch('app.render_template')
    @patch('app.ProcessController')
    @patch('app.current_user')
    def test_etl_status(self, mock_current_user, mock_ProcessController, mock_render_template):
        # Simula la función current_user
        with app.test_request_context():
            with unittest.mock.patch('flask_login.current_user', MagicMock()):
                response = app.test_client().get('/etl_status')
        
        self.assertEqual(response.status_code, 200)
        mock_ProcessController.assert_called_once_with(mock_current_user)
        mock_render_template.assert_called_once_with("etl_status.html", status_info=mock_ProcessController.return_value.check_etl_status.return_value)

if __name__ == '__main__':
    unittest.main()
