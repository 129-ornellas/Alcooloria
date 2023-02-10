<template>
    <v-container v-model="visible" class="ajusta">
        <v-form class="conserta">
            <v-row >
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
            <v-btn class="blue--text darken-1" flat @click="enviaMetricas()" :loading="loading" :disabled="loading">Enviar Métricas</v-btn>
        </v-form>
    </v-container>
  </template>
  
  <script>
  import calcule from '../pages/calcule.vue';
  import AppApi from '~apijs'
  import { mapGetters } from 'vuex';
  export default {
    data() {
      return {
        visible: false,
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
    components:{
        calcule
    },
    props: ['state'],
    methods: {
    open(){
      this.visible = true;
      console.log('Open');
    },
      enviaMetricas(){
        this.loading = true;
        console.log('this.usuario',this.usuario)
        AppApi.metricas(this.usuario.id,this.height,this.weight,this.gender,this.exercise)
        this.loading = false;
        this.$router.push({ path: '/calcule' })
      },

    }
  }
  </script>
<style>
.conserta{
  width: 20%;
  display: flex;
  flex-direction: column;

}
.ajusta{
  width: 500px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: white


}
</style>
