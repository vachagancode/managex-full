<script setup>
import {computed, onMounted, ref} from 'vue'
import axios from 'axios'
import router from "@/plugins/router.js";
import { provide } from 'vue';

import { changeAuthStatus } from "@/pages/Login/authRequiredService.js";

const users = ref([])
const email = ref('')
const password = ref('')
const isPasswordWrong = ref(false)
const isButtonDisabled = ref(true)

const rt = router
const fetchUsers = async () => {
  try {
    const { data } = await axios.get("http://127.0.0.1:8000/api/users/get_users/")
    users.value = data.map((obj) => ({
      ...obj,
    }))
    console.log(users.value)
  }
  catch (e) {
    console.log(e)
  }
  console.log("Yo")
}
const loginUser = async () => {
  try {
    for (const user of users.value) {
      if(user.email === email.value && user.password === password.value) {
        console.log("Logged Successfully")
        await rt.push("/dashboard")
        await axios.put(`http://127.0.0.1:8000/api/users/put_users/${user.id}/`, {
          "isLoggedIn": true
        });
        await changeAuthStatus()
        localStorage.setItem("email", user.email)
        break;
      }
      else {
        isPasswordWrong.value = true
        location.reload()
      }
    }
  }
  catch (e) {
    console.log(e)
  }
}

const passwordLenCheck = () => {
  if (password.value.length <= 32 && password.value.length >= 8) {
    isButtonDisabled.value = false
    console.log("Password is okay")
  }
  else {
    isButtonDisabled.value = true
  }
}
onMounted(() => fetchUsers())
</script>

<template>
  <div class="bg-black h-screen flex items-center justify-center">
    <div class="bg-black p-8 rounded-md shadow-lg w-full max-w-md">
      <form class="flex flex-col" @submit.prevent="loginUser">
        <h1 class="text-3xl font-extrabold text-white mb-6">
          Login
        </h1>
        <p class="text-white" v-if="isPasswordWrong">Password is Wrong</p>
        <div class="mb-4">
        </div>
        <div class="mb-4">
          <label
              for="email"
              class="block text-sm font-medium text-white"
          >
            Email Address
          </label>
          <input
              type="email"
              id="email"
              name="email"
              class="w-full p-2 border-2 border-purple-500 bg-black text-white rounded-md focus:outline-none focus:border-purple-700"
              placeholder="Enter your email address"
              v-model="email"
          />
        </div>
        <div class="mb-4">
          <label
              for="password"
              class="block text-sm font-medium text-white"
          >
            Password (8-32 symbols)
          </label>
          <input
              type="password"
              id="password"
              class="w-full p-2 border-2 border-purple-500 bg-black text-white rounded-md focus:outline-none focus:border-purple-700"
              placeholder="Enter your password"
              v-model="password"
              @input="() => passwordLenCheck()"
          />
        </div>

        <button
            class="disabled:bg-blue-950  bg-purple-600 text-white py-2 rounded-md hover:bg-purple-700 focus:outline-none focus:ring focus:border-purple-700"
            type="submit"
        >
          Login
        </button>
        <p class="text-sm text-white mt-4">
          Don't Have an Account <router-link to="/register" class="underline">Register here</router-link>.
        </p>
      </form>
    </div>
  </div>
</template>