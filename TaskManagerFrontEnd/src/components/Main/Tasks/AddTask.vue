<template>
    <div class="add-task">
        <svg class="plus-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24">
            <path d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm6 13h-5v5h-2v-5h-5v-2h5v-5h2v5h5v2z"/>
        </svg>
    </div>
</template>

<style>
.add-task {
  margin-top: 15px;
  width: 35px;
  height: 35px;
  border-radius: 10px;
  background: linear-gradient(to right, #764ba2, #667eea);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  color: #fff;
  position: relative;
  overflow: hidden;
  transition: transform 0.3s ease;
  display: flex;
  justify-content: center;
  align-items: center;
}

.add-task:hover {
    transform: translateY(-5px);
    cursor: pointer;
}
</style>