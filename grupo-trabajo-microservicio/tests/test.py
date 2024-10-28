import unittest
import requests


class TestGrupoTrabajo(unittest.TestCase):
    def test_get_grupos_trabajo(self):
        response = requests.get('http://grupo-trabajo')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        grupos_trabajo = response.json()
        self.assertIsInstance(grupos_trabajo, list)
        for grupo_trabajo in grupos_trabajo:
            self.assertIsInstance(grupo_trabajo, dict)
            self.assertIn('id', grupo_trabajo)
            self.assertIsInstance(grupo_trabajo['id'], int)
            self.assertIn('nombre', grupo_trabajo)
            self.assertIsInstance(grupo_trabajo['nombre'], str)
            self.assertIn('descripcion', grupo_trabajo)
            self.assertIsInstance(grupo_trabajo['descripcion'], str)
            self.assertIn('id_usuario', grupo_trabajo)
            self.assertIsInstance(grupo_trabajo['id_usuario'], int)


    def test_get_grupo_trabajo(self):
        response = requests.get('http://grupo-trabajo/1')    # Cambiar por la URL de tu microservicio
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        grupo_trabajo = response.json()
        self.assertIsInstance(grupo_trabajo, dict)
        self.assertIn('id', grupo_trabajo)
        self.assertIsInstance(grupo_trabajo['id'], int)
        self.assertIn('nombre', grupo_trabajo)
        self.assertIsInstance(grupo_trabajo['nombre'], str)
        self.assertIn('descripcion', grupo_trabajo)
        self.assertIsInstance(grupo_trabajo['descripcion'], str)
        self.assertIn('id_usuario', grupo_trabajo)
        self.assertIsInstance(grupo_trabajo['id_usuario'], int)

    def test_post_grupo_trabajo(self):
        response = requests.post('http://grupo-trabajo', json={
            'nombre': 'Grupo de trabajo 1',
            'descripcion': 'Descripción del grupo de trabajo 1',
            'id_usuario': 1
        })    # Cambiar por la URL de tu microservicio
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        grupo_trabajo = response.json()
        self.assertIsInstance(grupo_trabajo, dict)
        self.assertIn('id', grupo_trabajo)
        self.assertIsInstance(grupo_trabajo['id'], int)


if __name__ == '__main__':
    unittest.main()