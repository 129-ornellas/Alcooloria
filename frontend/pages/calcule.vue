<template>
    <v-container class="ajusta">
        <h1>{{ usuario.username }}, insira suas informações!</h1>
        <v-form class="conserta">
            <v-row>
                <v-col cols="3" offset="3">
                <v-text-field
                    label="Altura (em metros)"
                    type="number"
                    v-model="height"
                />
                </v-col>
                <v-col cols="3" offset="3">
                <v-text-field
                    label="Peso (em kg)"
                    type="number"
                    v-model="weight"
                />
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="3" offset="3">
                <v-select
                    label="Sexo"
                    v-model="gender"
                    :items="[
                    'Masculino',
                    'Feminino'
                    ]"
                />
                </v-col>
                <v-col cols="3" offset="3">
                <v-select
                    label="Pratica exercício?"
                    v-model="exercise"
                    :items="[
                    'Sedentário',
                    'Pouco Exercício diário',
                    'Muito exercício diário'
                    ]"
                />
                </v-col>
            </v-row>
            <v-btn class="blue--text darken-1" flat @click="enviaMetricas()" :loading="loading" :disabled="loading">Criar Cadastro</v-btn>
        </v-form>
    </v-container>
  </template>
  
  <script>
  import AppApi from '~apijs'
  import { mapGetters } from 'vuex';
  export default {
    data() {
      return {
        loading: false,
        height: 0,
        weight: 0,
        gender: '',
        exercise: '',
      }
    },
    computed: {
    ...mapGetters({
        usuario:"logged_user"
      })
    },
    methods: {
      enviaMetricas(){
        this.loading = true;
        console.log('tenta pegar user',this.usuario.username)
        AppApi.metricas(this.usuario.id,this.height,this.weight,this.gender,this.exercise)
        this.loading = false;
      }
    }
  }
  </script>
<style>
.conserta{
  width: 20%;
  height: 50%;
  display: flex;
  margin-top: 5%;
  flex-direction: column;

}
.ajusta{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-top: 10%;


}
</style>
