<template>
    <div class="button" >
        <van-button type="primary" @click="backup">点击备份</van-button>
    </div>

    <div class="backup_list">
        <h3>备份数据信息</h3>
        <van-list>
            <van-cell v-for="i in list" :key="i.filename" :title="i.filename" :value="i.file_size" :label="i.create_time"></van-cell>
        </van-list>
    </div>
    <div v-if="list.length===0" class="list">
        <van-empty description="暂无备份数据" />
    </div>
</template>

<script setup>
import { showToast } from 'vant'
import { ref, onMounted } from "vue";
import request from "../utils/request.js";
const list = ref([]); //备份列表数据
const getList = async () => {
    try{
        const res = await request.get("/api/backups");
        list.value = res.data;
        // console.log(res);
    }catch(err){
        console.log(err);
        list.value = [];
    }
};

async function backup(){
    try{
        const res=await request.post("/api/backup/database");
        // console.log(res)
        if(res.status===200){
            showToast('备份成功');
            getList();
        }else{
            showToast('备份失败');
        }
    }catch(err){
        console.log(err);
    }
}

onMounted(() => {
    getList();
});
</script>

<style>
.button {
    display: flex;
    justify-content: flex-end;
    padding: 10px;
}
</style>