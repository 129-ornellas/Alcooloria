import axios from '~/helpers/axios';

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const api = {
    login(username, password){
        return post('/api/login', {username: username, password: password});  
    },
    cadastro(username,email,senha){
        return post('/api/cadastro', {username: username, email: email, senha: senha})
    },
    logout(){
        return post('/api/logout');
    },
    whoami(){
        return get('/api/whoami');
    },
    add_cervejada(new_cervejada, tempo_corrida){
        return post('/api/add_cervejada', {qntd_cerveja: new_cervejada, tempo_corrida: tempo_corrida});
    },
    delete_cervejada(id){
        return post('/api/delete_cervejada', {id: id})
    },
    list_cervejadas(){
        return get('/api/list_cervejadas');
    },
    metricas(id,height,weight,gender,exercise){
        return post('/api/metricas', {usuario: id ,height: height, weight: weight, gender: gender, exercise: exercise})
    },
    calculo(qntd_cerveja){
        const teste = get('/api/calculo', {qntd_cerveja:qntd_cerveja})
        console.log(teste)
        return teste
    },
    cadastraCerveja(marca,mls,valorCalorico){
        return post('/api/cadastra_cerveja',{marca:marca,mls:mls,valor_calorico:valorCalorico})
    }
}
export default api;

function get(url, params){
    return axios.get(url, {params: params});
}

function post(url, params){
    var fd = new FormData();
    params = params || {}
    Object.keys(params).map((k) => {
        fd.append(k, params[k]);
    })
    return axios.post(url, fd);
}
