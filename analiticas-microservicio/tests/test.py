import unittest
import requests


class TestAnaliticas(unittest.TestCase):
    def test_get_analiticas(self):
        response = requests.get('http://analiticas')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        analiticas = response.json()
        self.assertIsInstance(analiticas, list)
        for analitica in analiticas:
            self.assertIsInstance(analitica, dict)
            self.assertIn('id', analitica)
            self.assertIsInstance(analitica['id'], int)
            self.assertIn('fecha', analitica)
            self.assertIsInstance(analitica['fecha'], str)
            self.assertIn('valor', analitica)
            self.assertIsInstance(analitica['valor'], float)
            self.assertIn('tipo', analitica)
            self.assertIsInstance(analitica['tipo'], str)
            self.assertIn('id_dispositivo', analitica)
            self.assertIsInstance(analitica['id_dispositivo'], int)
            self.assertIn('id_usuario', analitica)
            self.assertIsInstance(analitica['id_usuario'], int)


    def test_get_analitica(self):
        response = requests.get('http://   /analiticas/1')    # Cambiar por la URL de tu microservicio
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        analitica = response.json()
        self.assertIsInstance(analitica, dict)
        self.assertIn('id', analitica)
        self.assertIsInstance(analitica['id'], int)
        self.assertIn('fecha', analitica)
        self.assertIsInstance(analitica['fecha'], str)
        self.assertIn('valor', analitica)
        self.assertIsInstance(analitica['valor'], float)
        self.assertIn('tipo', analitica)
        self.assertIsInstance(analitica['tipo'], str)
        self.assertIn('id_dispositivo', analitica)
        self.assertIsInstance(analitica['id_dispositivo'], int)
        self.assertIn('id_usuario', analitica)
        self.assertIsInstance(analitica['id_usuario'], int)

    def test_post_analitica(self):
        response = requests.post('http://   /analiticas', json={
            'fecha': '2021-06-15',
            'valor': 10.5,
            'tipo': 'temperatura',
            'id_dispositivo': 1,
            'id_usuario': 1
        })    # Cambiar por la URL de tu microservicio
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        analitica = response.json()
        self.assertIsInstance(analitica, dict)
        self.assertIn('id', analitica)
        self.assertIsInstance(analitica['id'], int)
        self.assertIn('fecha', analitica)
        self.assertIsInstance(analitica['fecha'], str)
        self.assertIn('valor', analitica)
        self.assertIsInstance(analitica['valor'], float)
        self.assertIn('tipo', analitica)
        self.assertIsInstance(analitica['tipo'], str)
        self.assertIn('id_dispositivo', analitica)
        self.assertIsInstance(analitica['id_dispositivo'], int)
        self.assertIn('id_usuario', analitica)
        self.assertIsInstance(analitica['id_usuario'], int)


    def test_put_analitica(self):
        response = requests.put('http://   /analiticas/1', json={
            'fecha': '2021-06-15',
            'valor': 10.5,
            'tipo': 'temperatura',
            'id_dispositivo': 1,
            'id_usuario': 1
        })    # Cambiar por la URL de tu microservicio
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        analitica = response.json()
        self.assertIsInstance(analitica, dict)
        self.assertIn('id', analitica)
        self.assertIsInstance(analitica['id'], int)
        self.assertIn('fecha', analitica)
        self.assertIsInstance(analitica['fecha'], str)
        self.assertIn('valor', analitica)
        self.assertIsInstance(analitica['valor'], float)
        self.assertIn('tipo', analitica)
        self.assertIsInstance(analitica['tipo'], str)
        self.assertIn('id_dispositivo', analitica)
        self.assertIsInstance(analitica['id_dispositivo'], int)
        self.assertIn('id_usuario', analitica)
        self.assertIsInstance(analitica['id_usuario'], int)


    def test_delete_analitica(self):
        response = requests.delete('http://   /analiticas/1')    # Cambiar por la URL de tu microservicio
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        self.assertEqual(response.text, '')

if __name__ == '__main__':
    unittest.main()
