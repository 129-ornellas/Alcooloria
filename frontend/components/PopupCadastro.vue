<template>
  <div>
    <v-dialog v-model="visible" >
    <v-card >
      <v-card-text>
        <v-card-title>Cadastro</v-card-title>
        <v-container fluid>
          <v-text-field label="Nome" required v-model="username"/>
          <v-text-field label="Email" required v-model="email"></v-text-field>
          <v-text-field label="Senha" required v-model="password" type="password"></v-text-field>
          </v-container>
        </v-card-text>
        <v-btn class="blue--text darken-1" flat @click="cadastro()" :loading="loading" :disabled="loading">Criar Cadastro</v-btn>
        <v-btn class="blue--text darken-1" flat @click="close()">Cancela</v-btn>
      </v-card>
    </v-dialog>
    <v-dialog v-model="visible_metrica">
      <PopupMetricas />
    </v-dialog>
  </div>
 
</template>

<script>
import Vuex from 'vuex'
import AppApi from '~apijs'
import PopupMetricas from './PopupMetricas.vue';
export default {
  components:{
    PopupMetricas,
  },
  data () {
    return {
      visible: false,
      visible_metrica: false,      
      loading: false,
      username: '',
      email: '',
      password:'',
    };
  },
  computed: Object.assign(
      {},
      Vuex.mapGetters([
        'logged_user'
      ])
    ),
  props: ['state'],
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
      console.log('user:', this.username)
      console.log('pass:', this.password)
      AppApi.cadastro(this.username, this.email, this.password).then(()=>{
          AppApi.login(this.username, this.password).then((result)=>{
          console.log('result' ,result.data)
          var user = result.data;
          if(user){
            this.$store.commit('SET_LOGGED_USER', user);
            this.visible = false;
            console.log('logged')
          } else {
            this.error = true;
          }
          this.loading = false;
        });
      })
      console.log(this.username,'passou')
      this.loading = false;
      this.visible_metrica= true
    },
  },
}
</script>
