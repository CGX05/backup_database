<template>
    <div>
    <van-card
      v-for="item in healthData"
      :key="item.system_name"
      :title="item.system_name"                   
      :desc="`状态: ${item.message}`" 
      style="background-color:#f6f8fb; border-radius: 12px; border-left: 12px solid #1989fa"
    >
    <template #tags>
    <van-tag plain type="primary">{{ item.is_healthy ? '健康' : '不健康' }}</van-tag>
    </template>
</van-card>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import request from '../utils/request.js';

const healthData = ref([]);
const fetchHealthData = async () => {
  try {
    const res = await request.get('/api/health');
    // console.log('健康状态数据:', res.data);

    if (res.data && res.data.health) {
      healthData.value = [res.data.health];
    } else {
      healthData.value = [];
    }
  } catch (err) {
    console.error('获取健康状态失败:', err);
  }
};
onMounted(() => {
  fetchHealthData();
});
</script>