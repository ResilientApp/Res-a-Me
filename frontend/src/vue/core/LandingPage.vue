<template>
  <v-app style="width: 100%; height: 100%">
    <p
      style="
        position: fixed;
        z-index: 999;
        color: black;
        left: 30px;
        top: 27px;
        text-transform: none;
        letter-spacing: 0px;
      "
      id="userNameDisplay"
    >
      Hi, {{ userName }}
    </p>

    <v-btn
      variant="flat"
      color="#1a73e8"
      style="
        position: fixed;
        z-index: 999;
        color: white;
        right: 40px;
        top: 20px;
        text-transform: none;
      "
      id="signinButton"
      @click="this.$router.push('/login')"
    >
      Sign in
    </v-btn>

    <v-btn
      variant="flat"
      color="#1a73e8"
      style="
        position: fixed;
        z-index: 999;
        color: white;
        right: 40px;
        top: 20px;
        text-transform: none;
      "
      id="logoutButton"
      @click="logout()"
    >
      Logout
    </v-btn>

    <v-card
      theme="light"
      class="d-flex justify-center align-center flex-wrap"
      style="width: 100%; height: 100%"
    >
      <v-responsive max-width="550">
        <v-img
          class="mx-auto mt-12 mb-16"
          max-width="340"
          src="/images/icons/Res-A-Me.png"
        ></v-img>

        <v-autocomplete
          v-model="query"
          :disabled="isUpdating"
          :items="people"
          chips
          color="blue-grey-lighten-2"
          item-title="name"
          item-value="name"
          label="Search People"
          prepend-inner-icon="mdi-magnify"
          density="comfortable"
          auto-select-first
          return-object
          rounded
          theme="light"
          variant="outlined"
        >
          <template v-slot:chip="{ props, item }">
            <v-chip
              v-bind="props"
              :prepend-avatar="item.raw.avatar"
              :text="item.raw.name"
            ></v-chip>
          </template>

          <template v-slot:item="{ props, item }">
            <v-list-item
              v-bind="props"
              :prepend-avatar="item?.raw?.avatar"
              :title="item?.raw?.name"
              :subtitle="item?.raw?.group"
            ></v-list-item>
          </template>
        </v-autocomplete>

        <v-row dense justify="center" class="pt-5 pb-5">
          <v-btn
            variant="flat"
            color="#ededf0"
            style="text-transform: none; letter-spacing: 0px"
            class="mr-5"
            @click="search()"
          >
            Res-A-Me Search
          </v-btn>
          <v-btn
            variant="flat"
            color="#ededf0"
            style="text-transform: none; letter-spacing: 0px"
            @click="makeConntections()"
          >
            Make Connections
          </v-btn>
        </v-row>

        <v-container class="text-center pt-15" id="profileShortcut">
          <v-row justify="center" dense>
            <v-col cols="auto">
              <v-card
                class="pa-4"
                flat
                rel="noopener noreferer"
                target="_blank"
                width="112"
                @click="this.$router.push('/home')"
              >
                <v-avatar variant="tonal" class="mb-2" size="60">
                  <v-img :src="shortCutIcon"></v-img>
                </v-avatar>

                <div class="text-caption text-truncate">My Res-A-Me</div>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-responsive>
    </v-card>
  </v-app>
</template>

<script>
export default {
  async mounted() {
    document.getElementById("signinButton").style.display = "none";
    document.getElementById("profileShortcut").style.display = "none";
    document.getElementById("logoutButton").style.display = "none";
    document.getElementById("userNameDisplay").style.display = "none";

    await fetch("http://127.0.0.1:3033/loadUser", {
      // Check if user is logged in
      method: "GET",
      headers: {
        "Content-type": "application/json; charset=UTF-8",
        Authorization: `Bearer ` + sessionStorage.getItem("access_token"),
      },
    })
      .then((response) => response.json())
      .then((json) => {
        if (json.status === 200) {
          // User is logged in
          this.userEmail = json.logged_in_as;
          fetch(`/images/pictures/${this.userEmail}.png`)
            .then(response => {
              if(response.ok) {
                  this.shortCutIcon = `/images/pictures/${this.userEmail}.png`;
              } else {
                  this.shortCutIcon = `/images/pictures/avatar.png`;
              }
            });
          document.getElementById("profileShortcut").style.display = "block";
          document.getElementById("logoutButton").style.display = "block";
        } else {
          this.errorMessage = "User are not logged in";
          document.getElementById("signinButton").style.display = "block";
        }
      })
      .catch((error) => {
        console.error("There was an error!", error);
        this.errorMessage =
          error.message || "An error occurred. Please try again.";
      });

    fetch("http://127.0.0.1:3033/userList", {
      // Get the user list for the search bar
      method: "GET",
      headers: {
        "Content-type": "application/json; charset=UTF-8",
      },
    })
      .then((response) => response.json())
      .then((json) => {
        for (let index in json.user_list) {
          if (json.user_list[index].email === this.userEmail) {
            this.userName = json.user_list[index].name;
            document.getElementById("userNameDisplay").style.display = "block";
          }
          var avatar = "";
          fetch(`/images/pictures/${json.user_list[index].email}.png`)
            .then(response => {
              if(response.ok) {
                  avatar = `/images/pictures/${json.user_list[index].email}.png`;
              } else {
                  avatar = `/images/pictures/avatar.png`;
              }
            })
            .then(() => {
              const person = {
                name: json.user_list[index].name,
                group: json.user_list[index].position,
                avatar: avatar,
                email: json.user_list[index].email,
              };
              this.people.push(person);
            });
        }
      });
  },
  methods: {
    logout() {
      const errorMessage = "";
      fetch("http://127.0.0.1:3033/logout", {
        method: "GET",
        headers: {
          "Content-type": "application/json; charset=UTF-8",
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((json) => {
          // Handle successful logout
          // Redirect user to landing page
          if (json.message === "Logout successful") {
            sessionStorage.clear();
            document.getElementById("logoutButton").style.display = "none";
            document.getElementById("signinButton").style.display = "block";
            document.getElementById("profileShortcut").style.display = "none";
            document.getElementById("userNameDisplay").style.display = "none";
            alert("Logout Successful");
          } else {
            errorMessage.value =
              json.message || "Logout failed. Please try again.";
          }
        })
        .catch((error) => {
          console.error("Logout error:", error);
          errorMessage.value =
            error.message || "An error occurred. Please try again.";
        });
    },
    search() {
      // Route to resume page
      if (this.query.email) {
        this.$router.push({
          path: "/home",
          query: { query: this.query.email },
        });
      }
    },
    makeConntections() {
      // Randomly select a person in the user list and route to resume page
      const randomPerson =
        this.people[Math.floor(Math.random() * this.people.length)];
      this.$router.push({
        path: "/home",
        query: { query: randomPerson.email },
      });
    },
  },
  data() {
    return {
      userName: "",
      userEmail: "",
      shortCutIcon: "",
      autoUpdate: true,
      isUpdating: false,
      name: "Midnight Crew",
      query: [],
      people: [],
      title: "The summer breeze",
      timeout: null,
    };
  },
};
</script>

<style>
body {
  background-color: #f0f3f6 !important;
  font: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu,
    Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif !important;
  -webkit-font-smoothing: antialiased !important;
  -moz-osx-font-smoothing: grayscale !important;
}
</style>
