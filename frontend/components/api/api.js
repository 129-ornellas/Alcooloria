import axios from '~/helpers/axios';

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const api = {
    login(username, password){
        const a = post('/api/login', {username: username, password: password});  
        console.log('result',a)
        return a
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
    add_todo(newtask){
        return post('/api/add_todo', {new_task: newtask});
    },
    list_todos(){
        return get('/api/list_todos');
    },
    metricas(id,height,weight,gender,exercise){
        return post('/api/metricas', {usuario: id ,height: height, weight: weight, gender: gender, exercise: exercise})
    },
    calculo(qntd_cerveja){
        return get('/api/calculo', {qntd_cerveja:qntd_cerveja})
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
