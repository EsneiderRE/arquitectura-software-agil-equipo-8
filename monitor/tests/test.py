
import unittest
import requests


class TestMonitor(unittest.TestCase):
    def test_get_monitores(self):
        response = requests.get('http://monitor')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        monitores = response.json()
        self.assertIsInstance(monitores, list)
        for monitor in monitores:
            self.assertIsInstance(monitor, dict)
            self.assertIn('id', monitor)
            self.assertIsInstance(monitor['id'], int)
            self.assertIn('nombre', monitor)
            self.assertIsInstance(monitor['nombre'], str)
            self.assertIn('descripcion', monitor)
            self.assertIsInstance(monitor['descripcion'], str)
            self.assertIn('id_usuario', monitor)
            self.assertIsInstance(monitor['id_usuario'], int)


    def test_get_monitor(self):
        response = requests.get('http://monitor/1')    # Cambiar por la URL de tu microservicio
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        monitor = response.json()
        self.assertIsInstance(monitor, dict)
        self.assertIn('id', monitor)
        self.assertIsInstance(monitor['id'], int)
        self.assertIn('nombre', monitor)
        self.assertIsInstance(monitor['nombre'], str)
        self.assertIn('descripcion', monitor)
        self.assertIsInstance(monitor['descripcion'], str)
        self.assertIn('id_usuario', monitor)
        self.assertIsInstance(monitor['id_usuario'], int)

    def test_post_monitor(self):
        response = requests.post('http://monitor', json={
            'nombre': 'Monitor 1',
            'descripcion': 'Descripción del monitor 1',
            'id_usuario': 1
        })    # Cambiar por la URL de tu microservicio
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        monitor = response.json()
        self.assertIsInstance(monitor, dict)
        self.assertIn('id', monitor)
        self.assertIsInstance(monitor['id'], int)



if __name__ == '__main__':
    unittest.main()
