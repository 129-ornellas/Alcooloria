<template>
  <div>
    <div class="alinha">
        <img class="imagem" src="https://diageo.vtexassets.com/arquivos/new-home-newsletter-banner-desk.png" alt="">
        <v-card
          :loading="loading"
          
          max-width="374"
          min-height="300"
        >
        <v-card-title>
            <h2>Passou da conta?</h2>
            <h1>o Alcooloria te ajuda! ;)</h1>
        </v-card-title>
        <div class="mt-4 ">
            <v-btn v-if="!logged_user" light ripple class="ma-0 ml-5"  @click="open_login_dialog($event)">Login</v-btn>
            <v-btn v-if="!logged_user" light ripple class="ma-0 ml-5"  @click="open_cadastro_user($event)">Cadastre-se!</v-btn>
        </div>
        </v-card>
        <popup-login ref="popup_login"/>
        <popup-cadastro ref="popup_cadastro"/>
    </div>
  </div>
  
</template>

<script>

import toolbar from '~/components/toolbar.vue'
import PopupCadastro from '../components/PopupCadastro.vue';
import PopupLogin from '../components/PopupLogin.vue';
export default {
  components: {
    toolbar,
    PopupLogin,
    PopupCadastro
  },
  data: () => ({
    layout: {
      drawer: true,
    },
  }),
  computed: {
    snack () {
      return this.$store.getters.snack
    },
  },
  props: ['state'],
  methods: {
    open_login_dialog (evt) {
      this.$refs.popup_login.open();
      evt.stopPropagation();
    },
    open_cadastro_user (evt) {
      this.$refs.popup_cadastro.open();
      evt.stopPropagation();
    },
    logout(){
      AppApi.logout().then(()=>{
        this.$store.commit('SET_LOGGED_USER', null);
        Snacks.show(this.$store, {text: 'Até logo!'})
      });
    }
  }
}
</script>
<style>
  .alinha{
    margin: 15%;
    width: 60%;
    height: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .imagem{
    max-width: 120%;
    max-height: 120%;
  }
</style>
