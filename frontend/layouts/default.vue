<template>
  <v-app class="grey" id="inspire">
    <toolbar :state="layout"/>
    <v-content>
      <v-container fluid>
        <nuxt></nuxt>
      </v-container>
    </v-content>
    <v-snackbar
      :timeout="snack.timeout"
      :color="snack.color"
      bottom
      v-model="snack.visible"
    >
      {{snack.text}}
      <v-btn dark flat @click.native="snack.visible = false">Close</v-btn>
    </v-snackbar>
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