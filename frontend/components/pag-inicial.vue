<template>
    <div class="alinha">
        <div class="desceimagem">
            <img src="https://diageo.vtexassets.com/arquivos/new-home-newsletter-banner-desk.png" alt="">
        </div>
        <v-card
          :loading="loading"
          class="mx-auto my-12"
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
        <login-dialog ref="login_dialog"/>
        <cadastro-user ref="cadastro_user"/>
        <!-- <v-content>
          <v-container fluid>
            <nuxt></nuxt>
          </v-container>
        </v-content> -->

    </div>

</template>
<script>
  import toolbar from '~/components/toolbar.vue'
  import pagInicial from '../components/pag-inicial.vue';
  import loginDialog from '~/components/login-dialog.vue'
  import cadastroUser from './cadastro-user.vue'
  export default {
    components: {
      toolbar,
      pagInicial,
      loginDialog,
      cadastroUser
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
        this.$refs.login_dialog.open();
        evt.stopPropagation();
      },
      open_cadastro_user (evt) {
        this.$refs.cadastro_user.open();
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
    /* .centraliza{
        padding-top: 10%;
        width: 100%;
        height: 50%;
        text-align: center;

    } */
    .desceimagem{
        margin-top: 3%;
    }
    .alinha{
        justify-content: center;
        align-items: center;
    }
</style>
