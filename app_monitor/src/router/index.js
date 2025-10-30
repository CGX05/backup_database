import {createRouter, createWebHashHistory} from 'vue-router';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: () => import('../views/home.vue'),
        children: [
            {
                path:"/home/backup",
                name:"Backup",
                component: () => import('../views/backup.vue'),
                meta:{
                    title:'数据备份'
                }
            },
            {
                path:"/home/process",
                name:"Process",
                component: () => import('../views/process.vue'),
                meta:{
                    title:'进程监控'
                }
            },
            {
                path:"/home/healthy",
                name:"Healthy",
                component: () => import('../views/healthy.vue'),
                meta:{
                    title:'健康监控'
                }
            }
            ]
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router