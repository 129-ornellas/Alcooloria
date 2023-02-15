<template>
  <div>
    <v-dialog v-model="visible" >
    <v-card >
      <v-card-text>
        <v-card-title>Cadastro</v-card-title>
        <v-container fluid>
          <v-text-field label="Nome ou marca" required v-model="marca"/>
          <v-text-field label="mls" required v-model="mls"></v-text-field>
          <v-text-field label="Quantidade de calorias por dose" @keyup.enter="cadastraCerveja()" required v-model="valorCalorico" ></v-text-field>
          </v-container>
        </v-card-text>
        <v-btn class="blue--text darken-1" flat @click="cadastraCerveja()" :loading="loading" :disabled="loading">Salvar Cerveja</v-btn>
        <v-btn class="blue--text darken-1" flat @click="close()">Cancela</v-btn>
      </v-card>
    </v-dialog>
  </div>
 
</template>

<script>

import Vuex from 'vuex'
import AppApi from '~apijs'
import PopupMetricas from './PopupMetricas.vue';
import api from '../components/api/api';

export default{
    data(){
      return{
        marca: null,
        mls: null,
        valorCalorico: null,
        visible: false
      }
    },
    components:{
        PopupMetricas,
    },
    methods:{
        open(){
          this.visible = true;
        },
        cadastraCerveja(){
            this.loading = true
            api.cadastraCerveja(this.marca, this.mls, this.valorCalorico)
            this.loading = false
            this.close()
        },
        close(){
          this.visible = false;
        },
    },
    props: ['state'],
    computed: Object.assign(
      {},
      Vuex.mapGetters([
        'logged_user'
      ])
    ),
}
</script>