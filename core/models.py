from django.db import models
from django.contrib.auth.models import User

class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser", on_delete=models.PROTECT)
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )


class Cervejada(models.Model):
    qntd_cervejas = models.IntegerField()
    tempo_corrida = models.IntegerField()
    done = models.BooleanField(default=False)
    def to_dict_json(self):
        return {
            'id': self.id,
            'qntd_cervejas': self.qntd_cervejas,
            'tempo_corrida': self.tempo_corrida,
            'done': self.done,
        }


class Metricas(models.Model):
    user = models.ForeignKey(User, unique=True,  on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.IntegerField()
    gender = models.CharField(max_length=25)
    exercise = models.CharField(max_length=25)
    def to_dict_json(self):
        return {
            'id': self.id,
            'height': self.height,
            'weight': self.weight,
            'gender': self.gender,
            'exercise': self.exercise,
        }

class Cerveja(models.Model):
    marca = models.CharField(max_length=25)
    mls = models.IntegerField()
    valor_calorico = models.IntegerField()
    def to_dict_json(self):
        return {
            'id': self.id,
            'marca': self.marca,
            'mls': self.mls,
            'valor_calorico': self.valor_calorico,
        }
