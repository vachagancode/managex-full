<script setup>
import { inject, onMounted, provide, reactive, ref, watch } from 'vue';
import Task from './Task.vue';
import AddTask from './AddTask.vue';
import EditATask from './EditTask.vue';
import TaskManagement from './TaskManagement.vue';
import axios from 'axios';
import { getEditValue } from './services/exportEditValue'

const add_a_task_screen_value = ref(false)
const edit_a_task_screen_value = ref(false)
const tasks_screen_value = ref(true)

const title = ref('')
const description = ref('')

const email = localStorage.getItem("email")
const userTasks = ref([])

const add_value = ref(false)

const addATask = async () => {
  try {
    const { data } = await axios.post("http://127.0.0.1:8000/api/users/tasks/add_tasks/", {
      "title": title.value,
      "description": description.value,
      "owner": email
    })

  } catch (error) {
    console.log(error)
  }
  finally{
    location.reload()
  }
}

const editValue = getEditValue()

const changeScreen = () => {
      tasks_screen_value.value = !tasks_screen_value.value
      add_a_task_screen_value.value = !add_a_task_screen_value.value
}

const taskIds = ref([])

const getTasks = async () => {
  try {
    const { data } = await axios.get("http://127.0.0.1:8000/api/users/tasks/get_tasks/")
    data.map((task) => {
      if (email === task.owner) {
        userTasks.value.push(task)
        taskIds.value.push(task.id)
      }
    })
  } catch (error) {
    console.log(error)
  }
}

onMounted(() => getTasks())
// watch(edit_value, () => changeScreen())
watch(add_value, () => changeScreen())
</script>

<template>
    <div v-if="add_a_task_screen_value" class="edit-a-task flex flex-col items-center">
        <h1 class="text-5xl font-bold">Add A Task</h1>
        <form class="flex flex-col items-center" @submit.prevent="() => addATask()">
            <div class="mb-4">
                <label for="title" class="block text-sm font-medium">Title (Max: 166 symbols)</label>
                <input v-model="title" required type="text" id="title" name="title" class="bg-transparent mt-1 p-2 w-22 border border-gray-700 rounded-md focus:outline-none focus:border-purple-500">
            </div>
            <div class="mb-4">
                <label for="description" class="block text-sm font-medium">Description</label>
                <textarea v-model="description" required type="text" id="description" name="description" class="bg-transparent mt-1 p-2 w-22 border border-gray-700 rounded-md focus:outline-none focus:border-purple-500 h-32 text-start"></textarea>
            </div>
            <button type="submit" class="w-121 bg-purple-500 text-white p-2 rounded-md hover:bg-purple-600 focus:outline-none focus:ring focus:border-purple-300">Add A Task</button>
        </form>
    </div>
  <div v-if="tasks_screen_value" class="flex flex-col p-10">
    <div class="flex justify-between items-center">
      <h1 class="text-5xl font-bold">My Tasks</h1>
      <AddTask @click="() => changeScreen()" />
    </div>
    <div class="flex items-center items">
      <Task v-for="task in userTasks"
      :key="task.id"
      :id="task.id"
      :title="task.title"
      :description="task.description"
      :idDone="task.isDone"
      />
    </div>
  </div>
  <!-- <div class="plus">
    <svg class="plus-icon" xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24">
      <path d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm6 13h-5v5h-2v-5h-5v-2h5v-5h2v5h5v2z"/>
    </svg>
  </div> -->
</template>

<style>
.add-a-task-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.add-a-task {
  display: flex;
  align-items: center;
}

form {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-top: 15px;
}

form input, textarea {
  background: transparent;
}

.items {
  flex-wrap: wrap;
}
</style>