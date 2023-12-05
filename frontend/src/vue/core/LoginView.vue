<template>
    <v-app class="background-image">
        <v-main>
            <v-container fill-height>
                <!-- Main Row -->
                <v-row justify="center" align="center">

                    <!-- Image Column -->
                    <v-col cols="12" sm="8" md="4">
                        <v-row v-for="row in 11" :key="'row-' + row" justify="center" align="center">
                            <v-col v-for="n in 3" :key="n" justify="center" align="center"></v-col>
                        </v-row>
                        <v-img class="my-image" src="images/background/icon.png">
                        </v-img>
                    </v-col>

                    <v-col v-for="col in 1" :key="'col-' + col" justify="center" align="center">
                    </v-col>

                    <!-- Form Column -->
                    <v-col cols="12" sm="8" md="4">
                        <v-row v-for="row in 11" :key="'row-' + row" justify="center" align="center">
                            <v-col v-for="n in 3" :key="n" justify="center" align="center"></v-col>
                        </v-row>
                        <v-card class="elevation-12">
                            <v-toolbar class="toolbar-banner">
                                <v-toolbar-title class="toolbar-title">{{ isRegister ? stateObj.register.name + ' for ' :
                                    stateObj.login.name + ' to ' }} Res-a-Me</v-toolbar-title>
                            </v-toolbar>
                            <v-card-text>
                                <form ref="form" @submit.prevent="isRegister ? register() : login()">
                                    <v-text-field v-model="email" :rules="[rules.emailRules]" label="email"
                                        required></v-text-field>
                                    <v-text-field v-model="password" label="Password" type="password"
                                        required></v-text-field>
                                    <v-text-field v-if="isRegister" v-model="confirmPassword" label="Confirm Password"
                                        type="password" required></v-text-field>
                                    <div class="red--text">{{ errorMessage }}</div>
                                    <v-btn type="submit" class="mt-4 toolbar-banner" block style="color: white">{{
                                        isRegister ? stateObj.register.name : stateObj.login.name }}</v-btn>
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
                .then((json) => {
                    if (json.status === 200) {
                        console.log("Login successful")
                        console.log(json)
                        sessionStorage.setItem("access_token", json['access_token']);
                        sessionStorage.setItem("refresh_token", json['refresh_token']);
                        this.$router.push('/home');
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

.yellow-text:hover {
    color: #FF4500
}

.my-image {
  width: 3000%; /* or any specific pixel value */
  height: auto; /* maintain the aspect ratio */
  max-width: 500px; /* or any specific pixel value */
}
</style>
