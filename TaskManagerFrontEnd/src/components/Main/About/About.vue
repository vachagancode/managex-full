<script setup>
import {ref} from 'vue'
const text = ref(false)

const dontClick = () => {
  text.value = !text.value
}
</script>

<template>
  <div class="container mx-auto py-12">

    <h1 class="text-8xl font-bold mb-8">About Us</h1>

    <p class="mb-4 text-6xl">
      This Web App was developed by <a href="https://github.com/vachagancode" class="text-purple-500">Vach Karapetyan</a>
    </p>
    <p class="mb-4 text-6xl">
      After Learning Vue.js for 2-3 weeks, I decided to create this "Simple" Web App
    </p>
    <p class="mb-4 text-6xl">
      Give A Start To This Project :)
    </p>
    <p class="mb-4 text-6xl">
      Technologies Used:
    </p>
    <p class="mb-4 text-5xl mt-4 ml-4">
      <a target="_blank" href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" class="text-purple-500 hover:text-yellow-400 transition mt-5">JavaScript</a>, <br />
      <a target="_blank" href="https://vuejs.org/" class="text-purple-500 hover:text-green-400 transition mt-5">Vue.js</a>, <br />
      <a target="_blank" href="https://tailwindcss.com/" class="text-purple-500 hover:text-blue-400 transition mt-5">Tailwind</a>, <br />
      <a target="_blank" href="https://www.python.org/" class="text-purple-500 hover:text-green-500 transition mt-5">Python</a> <br />
      <a target="_blank" href="https://www.djangoproject.com/" class="text-purple-500 hover:text-red-500 transition mt-5">Django</a> <br />
    </p>
    <button @click="() => dontClick()">Don't Click</button>
    <p v-if="text" class="mb-4 text-xl">
      By The Way, There Is A Stupid Style Bug In This Project, It Is Because Of I Use Not Standart Way Of Text Gradient
    </p>
    <p class="text-4xl">- Vachagan Karapetyan</p>
  </div>
</template>

<style>

button {
  padding: 8px 35px;
  border: none;
  border-radius: 8px;
  margin-right: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
  font-size: 1rem;
  font-weight: bold;
  background-color: blueviolet;
}

</style>