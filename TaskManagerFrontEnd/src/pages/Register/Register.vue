<script setup>
import {computed, onMounted, ref} from 'vue'
import axios from 'axios'
import router from "@/plugins/router.js";
import { provide } from "vue";


const users_get = ref([])
const users = ref([])
const user = ref({})
// const user = ref({
//   "name": "",
//   "email": "",
//   "password": ""
// })

const username = ref('')
const password = ref('')
const email = ref('')
const isRegistered = ref(false)
const isButtonDisabled = ref(true)

const rt = router

const fetchUser = async () => {
  // try {
  //   const {data} = await axios.get("http://127.0.0.1:8000/api/users/get_users/")
  // }
  // catch (e) {
  //   console.log(e)
  // }

  console.log("Yo")
}

const postUserData = async () => {
    const { data } = await axios.get("http://127.0.0.1:8000/api/users/get_users/")
    users_get.value = data.map((obj) => ({
      ...obj
    }))
    users.value = users_get.value.map((object) => ({
      ...object
    }))
    user.value = users.value.map((obj) => ({
      ...obj
    }))
    for (let i = 0; i < user.value.length; i++) {
        try {
          if (users.value[i].email !== email.value) {
            const { postData } = await axios.post("http://127.0.0.1:8000/api/users/post_users/", {
              "name": username.value,
              "email": email.value,
              "password": password.value
            })
            console.log("POSTED")
            await rt.push("/login")
          }
          else {
            console.log(users.value[i].email)
            console.log(email.value)
            isRegistered.value = !isRegistered.value
            break
          }
        }
        catch (e) {
          console.log(e)
        }
    }
}

const returnToForm = () => {
  isRegistered.value = !isRegistered.value
  location.reload()
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

const enableDisableButton = computed(() => {
  if (isButtonDisabled.value) {
    return true
  }
  else {
    return false
  }
})

provide("username", username.value)
onMounted(() => fetchUser())

</script>

<template>
  <div class="bg-black h-screen flex items-center justify-center">
    <div class="bg-black p-8 rounded-md shadow-lg w-full max-w-md">
      <div v-if="isRegistered">
        <p class="text-white" >This email is registered </p>
        <button
            @click="() => returnToForm()"
            class="w-full bg-purple-600 text-white py-2 rounded-md hover:bg-purple-700 focus:outline-none focus:ring focus:border-purple-700"
        >
          Try Again
        </button>
      </div>
      <form v-if="!isRegistered" @submit.prevent="postUserData" class="flex flex-col">
        <h1 class="text-3xl font-extrabold text-white mb-6">
          Register an Account
        </h1>
        <div class="mb-4">
          <label
              for="name"
              class="block text-sm font-medium text-white"
          >
            Name
          </label>
          <input
              id="name"
              type="text"
              name="name"
              class="w-full p-2 border-2 border-purple-500 bg-black text-white rounded-md focus:outline-none focus:border-purple-700"
              placeholder="Enter your username"
              v-model="username"
          />
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
            :disabled="enableDisableButton"
            type="submit"
            class="disabled:bg-blue-950  bg-purple-600 text-white py-2 rounded-md hover:bg-purple-700 focus:outline-none focus:ring focus:border-purple-700"
        >
          Register
        </button>
        <p class="text-sm text-white mt-4">
          Already have an account? <router-link to="/login" class="underline">Log in here</router-link>.
        </p>
      </form>
    </div>
  </div>
</template>
<script setup>
</script>