<script setup>
defineProps({
    taskFunction: Function,
    taskAction: String
})
</script>

<template>
    <div class="edit-a-task flex flex-col items-center">
        <h1 class="text-5xl font-bold">{{ taskAction }}</h1>
        <form class="flex flex-col items-center" @submit.prevent="() => taskFunction()">
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
</template>