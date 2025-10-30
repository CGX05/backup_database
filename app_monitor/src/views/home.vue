<script setup>
import navigation from "../components/navigation.vue";

</script>

<template>
    <div class="nav">
        <navigation />
    </div>
    <div class="content">
        <router-view />
    </div>
</template>
<style scoped></style>  