import {createRouter, createWebHistory} from "vue-router";

import { getAuthStatus } from "@/pages/Login/authRequiredService.js";

const routes = [
    {
        path: '',
        name: 'home',
        component: () => import('@/pages/Home/Home.vue')
    },
    {
        path: '/register',
        name: 'register',
        component: () => import('@/pages/Register/Register.vue')
    },
    {
        path: '/login',
        name: 'login',
        component: () => import('@/pages/Login/Login.vue')
    },
    {
        path: '/logged',
        name: 'logged',
        component: () => import('@/pages/Login/Logged.vue')
    },
    {
        path: '/dashboard',
        name: 'dashboard',
        component: () => import('@/pages/Main/Main.vue'),
        meta: { requiresAuth: true },
        children: [
            {
                path: 'about',
                name: 'about',
                component: () => import('@/components/Main/About/About.vue'),
                meta: { requiresAuth: true },
            },
            {
                path: 'tasks',
                name: 'tasks',
                component: () => import('@/components/Main/Tasks/Tasks.vue'),
                meta: { requiresAuth: true },
            },
            {
                path: 'edit',
                name: 'edit',
                component: () => import('@/components/Main/Tasks/EditTask.vue'),
                meta: { requiresAuth: true },
            },
        ],
    }
    // {
    //     path: '/about',
    //     name: 'about',
    //     component: () => import('@/components/Main/About/About.vue'),
    //     meta: { requiresAuth: true },
    // }
]

const router = createRouter({
    routes,
    history: createWebHistory(),
})

router.beforeEach(async (to, from, next) => {
    if (to.meta.requiresAuth) {
        // If the route requires authentication, fetch the list of users
        // Check if a user is logged in based on your logic
        // const userIsLoggedIn = idkhowtogetthis
        const userIsLoggedIn = getAuthStatus()
        if (!userIsLoggedIn) {
            // If the user is not logged in, redirect to the login page
            next("/login"); // Replace '/login' with your actual login route
        } else {
            // If the user is logged in, proceed to the route
            next();
        }
    } else {
        // If no authentication is required, proceed to the route
        next();
    }
});

export default router