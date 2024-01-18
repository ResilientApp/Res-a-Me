<template>
    <v-app class="background-image">
        <div class="container-fluid h-100">
            <div class="row h-25"></div>
            <div class="row h-50 justify-content-center align-items-center">
                <div class="col-4">
                    <v-img class="my-image" src="images/background/icon.png"></v-img>
                </div>
                <div class="col-6">
                    <v-card class="elevation-12 card">
                        <v-toolbar class="toolbar-banner">
                            <v-toolbar-title class="toolbar-title">{{ isRegister ? stateObj.register.name + ' for ' :
                                stateObj.login.name + ' to ' }} Res-a-Me</v-toolbar-title>
                        </v-toolbar>
                        <v-card-text>
                            <transition :name="isRegister ? 'slide-down' : 'slide-up'" mode="out-in">
                                <form v-if="isRegister" ref="form" @submit.prevent="register()" key="register-form">
                                    <!-- Register form fields -->
                                    <v-text-field v-model="email" rounded variant="solo-filled" :rules="[rules.emailRules]" label="Email"
                                        required></v-text-field>

                                    <v-text-field v-model="password" rounded variant="solo-filled" label="Password" type="password"
                                        required></v-text-field>

                                    <v-text-field v-if="isRegister" v-model="confirmPassword" rounded variant="solo-filled" label="Confirm Password"
                                        type="password" required></v-text-field>

                                    <div class="red--text">{{ errorMessage }}</div>

                                    <v-btn type="submit" class="btn" block>{{ isRegister ? 'Register' : 'Login' }}</v-btn>

                                    <v-row justify="center">
                                        <v-col cols="12" class="text-center">
                                            <div class="grey--text mt-4 yellow-text" @click="isRegister = !isRegister;">{{
                                                toggleMessage }}</div>
                                        </v-col>
                                    </v-row>
                                </form>
                                <form v-else ref="form" @submit.prevent="login()" key="login-form">
                                    <!-- Login form fields -->
                                    <v-text-field v-model="email" rounded variant="solo-filled" :rules="[rules.emailRules]" label="Email"
                                        required></v-text-field>

                                    <v-text-field v-model="password" rounded variant="solo-filled" label="Password" type="password"
                                        required></v-text-field>

                                    <div class="red--text">{{ errorMessage }}</div>

                                    <v-btn type="submit" class="btn" block>{{ isRegister ? 'Register' : 'Login' }}</v-btn>

                                    <v-row justify="center">
                                        <v-col cols="12" class="text-center">
                                            <div class="grey--text mt-4 yellow-text" @click="isRegister = !isRegister;">{{
                                                toggleMessage }}</div>
                                        </v-col>
                                    </v-row>
                                </form>
                            </transition>
                        </v-card-text>
                    </v-card>
                </div>
            </div>
            <div class="row h-25"></div>
        </div>
    </v-app>
</template>



<script>
export default {
    name: "App",
    data() {
        return {
            email: "",
            password: "",
            confirmPassword: "",
            isRegister: false,
            errorMessage: "",
            stateObj: {
                register: {
                    name: 'Register',
                    message: 'Already have an Account? Login.'
                },
                login: {
                    name: 'Login',
                    message: 'Register'
                }
            },
            rules: {
                emailRules: [
                    value => !!value || 'E-mail is required',
                    value => /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/i.test(value) || 'Must be a valid e-mail'
                ]
            }
        };
    },
    methods: {
        validateEmailFormat() {
            for (let rule of this.rules.emailRules) {
                const result = rule(this.email);
                if (result !== true) {
                    this.errorMessage = result;
                    return false;
                }
            }
            return true;
        },
        login() {
            const userData = {
                email: this.email,
                password: this.password
            };

            if (!this.validateEmailFormat()) {
                return
            }

            fetch("http://127.0.0.1:3033/login", {
                method: "POST",
                body: JSON.stringify(userData),
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    "Access-Control-Allow-Origin": "*"
                },
                credentials: 'include'
            })
                .then((response) => response.json())
                .then(async (json) => {
                    if (json.status === 200) {
                        console.log("Login successful")
                        console.log(json)
                        sessionStorage.setItem("access_token", json['access_token']);
                        sessionStorage.setItem("refresh_token", json['refresh_token']);
                        try {
                            const updateResponse = await fetch("http://127.0.0.1:3033/updateResume", {
                                method: "POST",
                                headers: {
                                    "Content-type": "application/json; charset=UTF-8",
                                },
                                body: JSON.stringify({
                                    email: this.email,
                                }),
                            });
                            const json = await updateResponse.json();
                            if (json.status !== 200) {
                                console.error("Error fetching user resume: ", json.message);
                            }
                            this.$router.push({
                                path: "/home"
                            })
                                .then(() => window.location.reload(true))
                        }
                        catch (error) {
                            console.error("Error fetching user resume: ", error);
                        }
                    }
                    else {
                        this.errorMessage = "Login failed. Please try again.";
                    }
                })
                .catch(error => {
                    console.error('There was an error!', error);
                    this.errorMessage = error.message || "An error occurred. Please try again.";
                });
        },
        register() {
            if (this.password === this.confirmPassword) {
                const userData = {
                    email: this.email,
                    password: this.password
                };

                fetch("http://127.0.0.1:3033/register", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json; charset=UTF-8"
                    },
                    body: JSON.stringify(userData)
                })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
                        return response.json();
                    })
                    .then(json => {
                        if (json.message === "Register successful") {
                            console.log("Registration successful");
                            // Handle successful registration (e.g., redirect to login page)
                            sessionStorage.setItem("access_token", json['access_token']);
                            sessionStorage.setItem("refresh_token", json['refresh_token']);
                            this.$router.push('/edit');
                        } else {
                            // Handle registration error (e.g., show error message)
                            this.errorMessage = json.message || "Registration failed. Please try again.";
                        }
                    })
                    .catch(error => {
                        console.error('Registration error:', error);
                        this.errorMessage = error.message || "An error occurred during registration.";
                    });

                this.isRegister = false;
                this.$refs.form.reset();
            } else {
                this.errorMessage = "Passwords did not match";
            }
        }
    },
    computed: {
        toggleMessage: function () {
            return this.isRegister ? this.stateObj.register.message : this.stateObj.login.message
        }
    }
};
</script>

<style scoped>
.h-100 {
    height: 100vh;
    /* Full height of the viewport */
}

.h-25 {
    height: 25%;
    /* 25% of the viewport height */
}

.h-50 {
    height: 50%;
    /* 50% of the viewport height */
}

.card {
    border-radius: 13px;
    width: 80%;
    height: 85%;
    max-width: 400px;
    max-height: 450px;
    margin: auto;
}

/* Slide down */
.slide-down-enter-active, .slide-down-leave-active {
    transition: all 0.3s ease;
}

.slide-down-enter, .slide-down-leave-to {
    opacity: 0;
    transform: translateY(-100%);
}

/* Slide up */
.slide-up-enter-active, .slide-up-leave-active {
    transition: all 0.3s ease;
}

.slide-up-enter, .slide-up-leave-to {
    opacity: 0;
    transform: translateY(100%);
}

.toolbar-title {
    flex: 1;
    display: flex;
    justify-content: center;
    color: white;
}

.toolbar-banner {
    background-color: rgb(var(--v-theme-primary)) !important
}

.background-image {
    background-image: url('/images/background/background.png');
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
}

.btn {
    border-radius: 50px;
    color: white;
    background-color: rgb(var(--v-theme-primary)) !important
}

.yellow-text:hover {
    color: #FF4500
}

.my-image {
    width: auto;
    /* or any specific pixel value */
    height: auto;
    /* maintain the aspect ratio */
    max-width: auto;
    /* or any specific pixel value */
}
</style>
