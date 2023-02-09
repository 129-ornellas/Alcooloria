<template>
  <v-dialog v-model="visible" max-width="500px">
    <v-card>
      <v-card-text>
        <v-card-title>Cadastro</v-card-title>
        <v-container fluid>
          <v-text-field label="Nome" required v-model="username"/>
          <v-text-field label="Email" required v-model="email"></v-text-field>
          <v-text-field label="Senha" required v-model="senha" type="password"></v-text-field>
          </v-container>
        </v-card-text>
        <v-btn class="blue--text darken-1" flat @click="cadastro()" :loading="loading" :disabled="loading">Criar Cadastro</v-btn>
        <v-btn class="blue--text darken-1" flat @click="close()">Cancela</v-btn>
        <cadastro-user ref="cadastro_user"/>
    </v-card>
  </v-dialog>
</template>

<script>

import AppApi from '~apijs'

export default {
  data () {
    return {
      visible: false,
      loading: false,
      username: '',
      email: '',
      senha:'',
    };
  },
  methods: {
    open(){
      this.visible = true;
      console.log('Open');
    },
    close(){
      this.visible = false;
      console.log('Close');
    },
    cadastro(){
      this.loading = true;
      AppApi.cadastro(this.username, this.email,this.senha)
      this.loading = false;
      this.close()
    },
  },
}
</script>
