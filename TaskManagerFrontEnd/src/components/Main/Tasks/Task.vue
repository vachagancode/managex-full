<script setup>
import axios from 'axios';
import { inject, provide, ref } from 'vue';
import { exportEditValue, editValue } from './services/exportEditValue'

const props = defineProps({
    title: String,
    description: String,
    id: Number,
    isDone: Boolean
})

const isDoneValue = ref(false)
const markDone = async () => {
  try {
    isDoneValue.value = !isDoneValue.value
    console.log(isDoneValue.value)
    localStorage.setItem(`isDone_${props.id}`, isDoneValue.value)
  } catch (error) {
    console.error(error)
  }
}

const deleteTask = async () => {
  try {
    await axios.delete(`http://127.0.0.1:8000/api/users/tasks/delete_tasks/${props.id}/`)
    location.reload()
  }
  catch(error) {
      console.error(error)
  }
}

isDoneValue.value = localStorage.getItem(`isDone_${props.id}`) === 'true'
</script>

<template>
<div :class="[{'task-card': !isDoneValue}, 'mr-5', {'is-done': isDoneValue}]">
    <h2>{{ props.title }}</h2>
    <p>{{ props.description }}</p>
    <div class="button-container">
        <button @click="() => markDone()" class="done">Done</button>
        <button @click="() => deleteTask()" class="delete">Delete</button>
    </div>
</div>
</template>

<style scooped>
.is-done {
  text-wrap: pretty;
  width: 300px;
  padding: 20px;
  border-radius: 10px;
  background: linear-gradient(to right, rgba(0, 255, 136, 0.701), #00f2ffa3);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  color: #fff;
  position: relative;
  overflow: hidden;
  transition: margin-top 0.3s ease;
  margin-top: 40px;
  word-wrap: break-word;
}

.task-card {
  word-wrap: break-word;
  width: 300px;
  padding: 20px;
  border-radius: 10px;
  background: linear-gradient(to right, #667eea, #764ba2);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  color: #fff;
  position: relative;
  overflow: hidden;
  transition: transform 0.3s ease; 
  margin-top: 40px;
}
.task-card:hover {
  transform: translateY(-5px);
} 

h2 {
  margin-top: 0;
  color: #fff;
  font-size: 1.5rem;
}

p {
  margin-bottom: 15px;
  color: #eee;
}

button {
  padding: 8px 35px;
  border: none;
  border-radius: 8px;
  margin-right: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
  font-size: 1rem;
  font-weight: bold;
}

button.edit {
  background-color: #45aaf2;
  color: #fff;
}

button.done {
  background-color: #2ecc71;
  color: #fff;
}

button.delete {
  background-color: #e74c3c;
  color: #fff;
}

button:hover {
  background-color: #34495e;
  transform: scale(1.1);
}

.button-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 15px;
}
</style>