import { createApp } from 'vue'
import App from './App.vue'
// 引入
import Vant from 'vant'
import 'vant/lib/index.css'
import router from './router'

const app = createApp(App)
app.use(Vant)
app.use(router)
app.mount('#app')
