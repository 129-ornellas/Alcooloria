<template>
  <v-app  id="inspire">
    <toolbar :state="layout"/>
      <pagInicial class="centralizar d-flex justify-center align-self-center"/>
  </v-app>
</template>

<script>
  import toolbar from '~/components/toolbar.vue'
  import pagInicial from '../components/pag-inicial.vue';
  export default {
    components: {
      toolbar,
      pagInicial
    },
    data: () => ({
      layout: {
        drawer: true,
      },
    }),
    computed: {
      snack () {
        return this.$store.getters.snack
      }
    }
  }
</script>
<style>
.centralizar{
  margin-top: 12%;
  width: 60%;
}
</style>