<template>
  <div>
    <van-card
      v-for="process in data"
      :key="process.name"
      :title="process.name"                   
      :desc="`进程描述: ${process.description}`"    
      :num="`日志路径:${process.logfile}`"  
      style="background-color:#f6f8fb; border-radius: 12px; border-left: 12px solid #1989fa"  
    >
    <template #tags>
    <van-tag plain type="primary">{{ process.statename }}</van-tag>
    </template>
    </van-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import request from '../utils/request.js';

const data = ref([]);

const processInfo = async () => {
  try {
    const res = await request.get('/api/supervisord/processes');
    // console.log('API 返回:', res);

    if (Array.isArray(res.data)) {
      data.value = res.data;
    } else if (res.data?.processes) {
      data.value = res.data.processes;
    } else {
      data.value = [res.data];
    }
  } catch (err) {
    console.error('获取进程信息失败:', err);
  }
};

onMounted(() => {
  processInfo();
});
</script>