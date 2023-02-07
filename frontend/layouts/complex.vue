<template>
  <v-app class="grey">
    <toolbar :state="layout"/>
    <v-content>
      <v-container fluid>
        <nuxt></nuxt>
      </v-container>
    </v-content>
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
        drawerRight: true,
        right: null,
        left: null
      },
    })
  }
</script>