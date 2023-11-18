<template>
    <v-app class="background-image">
        <v-main>
            <v-container fill-height>
                <v-row v-for="row in 11" :key="'row-' + row" justify="center" align="center">
                    <v-col v-for="n in 3" :key="n" justify="center" align="center"></v-col>
                </v-row>

                <v-row justify="center" align="center">
                    <v-col justify="center" align="center"></v-col>
                    <v-col cols="12" sm="8" md="4">
                        <v-card class="elevation-12">
                            <v-toolbar class="toolbar-banner">
                                <v-toolbar-title class="toolbar-title">{{isRegister ? stateObj.register.name + ' for ' : stateObj.login.name + ' to '}} Res-a-Me</v-toolbar-title>
                            </v-toolbar>
                            <v-card-text>
                                <form ref="form" @submit.prevent="isRegister ? register() : login()">
                                    <v-text-field v-model="email" label="email" required></v-text-field>
                                    <v-text-field v-model="password" label="Password" type="password" required></v-text-field>
                                    <v-text-field v-if="isRegister" v-model="confirmPassword" label="Confirm Password" type="password" required></v-text-field>
                                    <div class="red--text">{{errorMessage}}</div>
                                    <v-btn type="submit" class="mt-4 toolbar-banner" block style="color: white">{{isRegister ? stateObj.register.name : stateObj.login.name}}</v-btn>
                                    <v-row justify="center">
                                        <v-col cols="12" class="text-center">
                                            <div class="grey--text mt-4 yellow-text" @click="isRegister = !isRegister;">
                                                {{ toggleMessage }}
                                            </div>
                                        </v-col>
                                    </v-row>
                                </form>
                            </v-card-text>
                        </v-card>
                    </v-col>
                    <v-col justify="center" align="center"></v-col>
                </v-row>
            </v-container>
        </v-main>
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
                    message: 'Aleady have an Acoount? Login.'
                },
                login: {
                    name: 'Login',
                    message: 'Register'
                }
            }
        };
    },
    methods: {
        login() {
            const userData = {
                email: this.email,
                password: this.password
            };

            fetch("http://127.0.0.1:3033/login", {
                    method: "POST",
                    body: JSON.stringify(userData),
                    headers: {
                        "Content-type": "application/json; charset=UTF-8",
                    }
                })
                .then((response) => response.json())
                .then((json) => {
                    console.log(json)
                    if (json.message === "Login successful") {
                        console.log("Login successful")
                        this.$router.push('/home');
                    } else {
                        this.errorMessage = "Login failed. Please try again.";
                    }
                })
                .catch(error => {
                    console.error('There was an error!', error);
                    this.errorMessage = error.message || "An error occurred. Please try again.";
                });
        },
        register() {
            if (this.password == this.confirmPassword) {
                this.isRegister = false;
                this.errorMessage = "";
                this.$refs.form.reset();
            } else {
                this.errorMessage = "password did not match"
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
    background-image: url('/images/background/login-background.jpg');
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
}

.yellow-text:hover {
    color: #FF4500
}
</style>
