import Vue from 'vue'

var logged_user = null;

function mockasync (data) {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve({data: data}), 600)
  })
}

const api = {
    login(username, password){
        if(password){
            logged_user = {
                username: username,
                first_name: 'Mark',
                last_name: 'Zuckerberg',
                email: 'zuck@facebook.com',
                notifications_enabled: true,
                permissions:{
                    ADMIN: username == 'admin',
                    STAFF: username == 'admin',
                }
            };
        }
        return mockasync(logged_user);
    },
    calculo(qntd_cervejas){
        if (qntd_cervejas){
            return mockasync(10 * qntd_cervejas)
        }
    },
    logout(){
        logged_user = null;
        return mockasync({});
    },
    whoami(){
        return mockasync(logged_user ? {
            authenticated: true,
            user: logged_user,
        } : {authenticated: false});
    },
    add_cervejada(newCervejada, tempoCorrida){
        return mockasync({qntd_cervejas: newCervejada, tempo_corrida: tempoCorrida ,done: false});
    },
    list_cervejadas(){
        return mockasync({
            cervejadas: [
                {qntd_cervejas: 2, tempo_corrida: 19, done: true},
                {qntd_cervejas: 4, tempo_corrida: 38, done: false}
            ]
        });
    }
};

export default api;
