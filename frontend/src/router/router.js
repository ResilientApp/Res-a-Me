import { useData } from "../composables/data.js"
import RouterView from "../vue/core/RouterView.vue"
import LoginView from "../vue/core/LoginView.vue"
import EditView from "../vue/core/Editview.vue"
import LandingPage from "../vue/core/LandingPage.vue"
import { createRouter, createWebHistory } from "vue-router"

export function createAppRouter() {
    const data = useData();
    const sections = data.getSections();
    const homeSection = sections[0] || { id: 'home' };

    /** Create Home **/
    const routeList = [
        {
            path: '/',
            name: "LandingPage",
            component: LandingPage
        },
        {
            path: '/login',
            name: "login",
            component: LoginView
        },
        {
            path: '/home',
            name: homeSection['id'],
            component: RouterView
        },
        {
            path: '/edit',
            name: "edit",
            component: EditView
        },]

    for (let i = 1; i < sections.length; i++) {
        let sectionId = sections[i].id
        routeList.push({
            path: '/' + sectionId,
            name: sectionId,
            component: RouterView
        })
    }

    routeList.push({
        path: '/:pathMatch(.*)*',
        redirect: '/'
    })

    // Create the router instance
    const router = createRouter({
        history: createWebHistory(import.meta.env.BASE_URL),
        routes: routeList
    });

    // Add a global beforeEach guard to validate user is logged in or not
    router.beforeEach(async (to, from, next) => {
        let isAuthenticated = false

        try {
            const response = await fetch("http://127.0.0.1:3033/loadUser", {
                method: "GET",
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    "Access-Control-Allow-Origin": "*",
                    "Authorization": `Bearer ` + sessionStorage.getItem('access_token'),
                }
            });

            const json = await response.json();

            if (json.status === 200) {
                isAuthenticated = true;
            } else if (json.msg === "Token has expired") {
                const refreshResponse = await fetch("http://127.0.0.1:3033/refresh", {
                    method: "POST",
                    headers: {
                        "Content-type": "application/json; charset=UTF-8",
                        "Access-Control-Allow-Origin": "*",
                        "Authorization": `Bearer ` + sessionStorage.getItem('refresh_token'),
                    }
                });

                const refreshJson = await refreshResponse.json();
                if (refreshJson.status === 200) {
                    // update new access token with refresh token
                    sessionStorage.setItem("access_token", refreshJson['access_token']);
                    isAuthenticated = true;
                }
                else {
                    throw new Error('Refresh Token Expired!!! Please Log In Again')
                }
            }
        } catch (error) {
            console.error('There was an error!', error);
        }

        console.log("isAuthenticated = ", isAuthenticated)

        if (to.name === 'login' && isAuthenticated) {
            next({ name: homeSection['id'] }); // Redirect to home if trying to access login while authenticated
        } else {
            next(); // Otherwise, proceed as normal
        }
    });

    return router;
}