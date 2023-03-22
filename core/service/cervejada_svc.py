from core.models import Cervejada

def add_cervejada(qntd_cervejas, minutos_corridos):
    cervejada = Cervejada(qntd_cervejas=qntd_cervejas, tempo_corrida=minutos_corridos, done=False)
    cervejada.save()
    return cervejada.to_dict_json()


def delete_cervejada(id: int):
    Cervejada.objects.get(id=id).delete()


def list_cervejadas():
    cervejadas = Cervejada.objects.all()
    return [cervejada.to_dict_json() for cervejada in cervejadas]