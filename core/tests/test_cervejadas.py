from http import HTTPStatus
from core.models import User, Cervejada
from django.test.client import Client
from django.test.testcases import TestCase
from core.tests import fixtures
import json


class TestAuthApi(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.user_jon()

    def test_auth_api(self):
        client = Client()
        client.force_login(User.objects.get(username='jon'))
        r1 = client.post('/api/add_cervejada', {'qntd_cerveja': 2, 'tempo_corrida': 19})
        r2 = client.post('/api/add_cervejada', {'qntd_cerveja': 2, 'tempo_corrida': 19})
        r3 = client.get('/api/list_cervejadas')
        self.assertEqual({200}, {r.status_code for r in [r1, r2, r3]})
        cervejadas = json.loads(r3.content.decode('utf-8'))
        self.assertEqual(2, len(cervejadas['cervejadas']))


def test_list_cervejadas_return_cervejadas(client, db):
    cervejada = Cervejada.objects.create(
        qntd_cervejas=2,
        tempo_corrida=19,
        done=False
    )

    resp = client.post("/api/list_cervejadas")
    assert resp.json() == {"cervejadas": [cervejada.to_dict_json()]}
    assert resp.status_code == HTTPStatus.OK


def test_delete_cervejada(client, db, cervejada):
    resp = client.post(
        "/api/delete_cervejada",
        {
            "id": cervejada.id
        },
    )
    assert Cervejada.objects.all().count() == 0
    assert resp.status_code == HTTPStatus.OK
