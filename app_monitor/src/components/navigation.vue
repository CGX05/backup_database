<script setup>
import { ref } from 'vue';
const active = ref(0);
</script>

<template>
    <div class="nav">
        <van-nav-bar title="应用监控" />
        <van-notice-bar scrollable text="人 机"/>
    </div>
    <van-tabbar v-model="active">
        <van-tabbar-item icon="star" replace to="/">主页</van-tabbar-item>
        <van-tabbar-item icon="smile" replace to="/home/backup">数据备份</van-tabbar-item>
        <van-tabbar-item icon="warning" replace to="/home/process">进程状态</van-tabbar-item>
        <van-tabbar-item icon="checked" replace to="/home/healthy">系统监控</van-tabbar-item>
    </van-tabbar>

</template><van-icon name="smile" />