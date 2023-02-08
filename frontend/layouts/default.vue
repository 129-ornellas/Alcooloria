<template>
  <v-app  id="inspire">
    <toolbar :state="layout"/>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
  import toolbar from '~/components/toolbar.vue'
  export default {
    components: {
      toolbar,
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