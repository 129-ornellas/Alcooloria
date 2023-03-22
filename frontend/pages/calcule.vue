<template>
  <div class="asd">
    <v-row class="text-center">
      <v-col cols="6">
        <v-form >
          <img class="imagem" src="https://images.pexels.com/photos/1089930/pexels-photo-1089930.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="">
          <v-text-field type="number" v-model="qntd_cervejas" label="Insira o número de cervejas consumidas"/>
        </v-form>
        <v-btn @click="calculaCerveja">enviar</v-btn>
        <v-btn @click="chamaCadastraCerveja($event)" > enviar </v-btn>
        <PopupCadastraCerveja ref="popup_cerveja"/>
        <p>voce precisar correr {{ minutosCorridos }} minutos</p>
      </v-col>
      <v-col cols="6">
        <v-card v-for="item in items" :key="item.title" rounded>
          <v-card-title>Cervejas: {{ item.qntd_cervejas }}</v-card-title>
          <v-card-subtitle class="mb-6 fs">Necessário: {{ item.tempo_corrida }} minutos</v-card-subtitle>
          <v-btn @click="deleteCervejada(item)">DELETE</v-btn>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>
<script>
  import AppApi from '~apijs'
  import PopupCadastraCerveja from '../components/PopupCadastraCerveja.vue'; 

  export default{
    data(){
      return{
        visible: false,
        qntd_cervejas: null,
        minutosCorridos: null,
        items: [],
      }
    },
    mounted () {
      this.loading = true
      AppApi.list_cervejadas().then(response => {
        const cervejadas = response.data.cervejadas
        this.items = cervejadas
        this.loading = false
      })
    },
    components:{
      PopupCadastraCerveja
    },
    methods:{
      calculaCerveja(){
        AppApi.calculo(this.qntd_cervejas).then((result)=>{
          console.log('bateu na mock')
          this.minutosCorridos = result.data
          AppApi.add_cervejada(this.qntd_cervejas, this.minutosCorridos).then((result)=>{
            this.items.push(result.data)
          })
        })
      },
      chamaCadastraCerveja(evt){
        this.$refs.popup_cerveja.open()
        evt.stopPropagation()
      },
      async deleteCervejada(rodada) {
        await AppApi.deleteCervejada({id: rodada.id})
        this.items = await AppApi.list_cervejadas()
      }
    }
  }
</script>
<style>
.asd{
  margin-top: 10% ;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
.imagem{
  max-width: 300px;
}
</style>