import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import App from './App.vue'
import Index from './components/Index.vue'
import Accounts from './components/Accounts.vue'
import Transactions from './components/Transactions.vue'
import Categories from './components/Categories.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/', component: Index},
        {path: '/accounts', component: Accounts},
        {path: '/transactions', component: Transactions}, 
        {path: '/categories', component: Categories},
    ]
});

const app = createApp(App);
app.config.globalProperties.$hostname = 'http://192.168.0.102:8000';
app.use(router);



app.mount('#app');

