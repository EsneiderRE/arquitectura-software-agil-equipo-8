import unittest
import requests


class TestErrores(unittest.TestCase):
    def test_get_errores(self):
        response = requests.get('http://errores')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        errores = response.json()
        self.assertIsInstance(errores, list)
        for error in errores:
            self.assertIsInstance(error, dict)
            self.assertIn('id', error)
            self.assertIsInstance(error['id'], int)
            self.assertIn('fecha', error)
            self.assertIsInstance(error['fecha'], str)
            self.assertIn('descripcion', error)
            self.assertIsInstance(error['descripcion'], str)
            self.assertIn('id_dispositivo', error)
            self.assertIsInstance(error['id_dispositivo'], int)
            self.assertIn('id_usuario', error)
            self.assertIsInstance(error['id_usuario'], int)


    def test_get_error(self):
        response = requests.get('http://errores/1')    # Cambiar por la URL de tu microservicio
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        error = response.json()
        self.assertIsInstance(error, dict)
        self.assertIn('id', error)
        self.assertIsInstance(error['id'], int)
        self.assertIn('fecha', error)
        self.assertIsInstance(error['fecha'], str)
        self.assertIn('descripcion', error)
        self.assertIsInstance(error['descripcion'], str)
        self.assertIn('id_dispositivo', error)
        self.assertIsInstance(error['id_dispositivo'], int)
        self.assertIn('id_usuario', error)
        self.assertIsInstance(error['id_usuario'], int)

    def test_post_error(self):
        response = requests.post('http://errores', json={
            'fecha': '2021-06-15',
            'descripcion': 'Error de prueba',
            'id_dispositivo': 1,
            'id_usuario': 1
        })    # Cambiar por la URL de tu microservicio
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        error = response.json()
        self.assertIsInstance(error, dict)
        self.assertIn('id', error)
        self.assertIsInstance(error['id'], int)


if __name__ == '__main__':
    unittest.main()
