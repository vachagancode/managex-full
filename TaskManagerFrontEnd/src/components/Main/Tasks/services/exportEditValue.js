import { ref } from 'vue';

const editValue = ref(localStorage.getItem('editValue') === 'true');

const exportEditValue = () => {
    localStorage.setItem('editValue', !editValue.value);
};

const getEditValue = () => {
    return localStorage.getItem('editValue') === 'true';
};

export { exportEditValue, getEditValue, editValue };
