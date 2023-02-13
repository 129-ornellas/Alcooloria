<template>
  <div class="asd">
    <v-form >
      <img class="imagem" src="https://images.pexels.com/photos/1089930/pexels-photo-1089930.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="">
      <v-text-field type="number" v-model="qntd_cervejas" label="Insira o número de cervejas consumidas"/>
    </v-form>
    <v-btn @click="calculaCerveja">enviar</v-btn>
    <!-- <v-btn @click="cadastraCerveja">enviar</v-btn> -->
    voce precisar correr {{ minutosCorridos }} minutos
    <!-- <PopupCadastraCerveja v-model="visible" ref="popup-cadastra-cerveja"/> -->
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
        
      }
    },
    components:{
      PopupCadastraCerveja
    },
    methods:{
      calculaCerveja(){
        AppApi.calculo(this.qntd_cervejas).then((result)=>{
          console.log('bateu na mock')
          this.minutosCorridos = result.data
        })
      },
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