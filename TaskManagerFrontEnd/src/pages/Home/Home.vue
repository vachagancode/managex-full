<script setup>
import { onMounted } from "vue";
import router from "@/plugins/router.js";

// const checkIfIsLogged = () => {
//   if (localStorage.getItem("AuthStatus") === "true") {
//     router.push('/dashboard')
//   }
// }

// onMounted(() => checkIfIsLogged())
</script>

<template>
  <div class="h-screen w-full bg-black flex flex-col items-center">
    <div class="flex items-center flex-col info-div m-auto">
      <b class="introduction-text text-9xl">Hey!</b>
      <h2 class="info-text text-xl">Wanna control your tasks ?</h2>
      <div class="flex gap-2">
        <router-link class="link" to="register">Take a try !</router-link>
        <router-link class="link" to="login">Login</router-link>
      </div>
    </div>
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Source+Code+Pro:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

.introduction-text {
  background: linear-gradient(to right, #B33491 0%, #7500CF 100%);
  -webkit-background-clip: text;
  color: transparent;
  font-family: 'Poppins', sans-serif;
  margin-bottom: 5px;
  -webkit-text-fill-color: transparent;
}



.info-text {
  background: #7500CF;
  background: linear-gradient(to right, #7500CF 0%, #B33491 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
}

.link {
  color: #fff;
  font-weight: 700;
  height: 40px;
  width: 120px;
  background: linear-gradient(to right, #7500CF 0%, #B33491 100%);
  font-size: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 16px;
  transition: 0.3s;
  margin-top: 5px;
}

.link:hover {
  transform: scale(1.05);
}

</style>