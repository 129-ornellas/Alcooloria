<template>
  <div class="asd">
    <v-form >
      <img class="imagem" src="https://images.pexels.com/photos/1089930/pexels-photo-1089930.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="">
      <v-text-field type="number" v-model="qntd_cervejas" label="Insira o número de cervejas consumidas"/>
    </v-form>
    <v-btn @click="calculaCerveja">enviar</v-btn>
    voce precisar correr {{ minutosCorridos }} minutos
  </div>
  </template>
<script>
import api from '../components/api/api';


  export default{
    data(){
      return{
        qntd_cervejas: null,
        minutosCorridos: null,
      }
    },
    methods:{
      calculaCerveja(){
        api.calculo(this.qntd_cervejas).then((result)=>{
          this.minutosCorridos = result.data
        }
        )
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