<script setup>
defineProps({
  name: String,
  link: String
})
</script>

<template>
  <li class="mb-2">
    <router-link :to="link" class="cursor-pointer link" aria-current="page">{{ name }}</router-link>
  </li>
</template>

<style>
.link {
  font-size: 18px;
  transition: 0.3s;
  font-weight: 500;
}
.link:hover {
  color: blueviolet;
}

</style>