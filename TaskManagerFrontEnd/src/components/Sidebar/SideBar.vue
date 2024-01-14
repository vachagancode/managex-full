<script setup>
import SideBarLink from './SideBarLink.vue';
import router from '@/plugins/router';

const LogOut = () => {
  localStorage.setItem('AuthStatus', 'false')
  router.push('/')
}
</script>

<template>
    <div class="flex h-screen" style="color: #e6e6e6;">
      <div class="flex-none w-64 bg-black p-6">
        <h2 class="font-bold text-6xl">Manage<span class="text-purple-500">X</span></h2>
        <nav class="mt-10">
          <ul>
            <SideBarLink name="Tasks" link="/dashboard/tasks" />
            <SideBarLink name="About" link="/dashboard/about" />
            <a class="cursor-pointer link" @click="() => LogOut()">Log Out</a>
          </ul>
        </nav>
      </div>
    </div>
</template>