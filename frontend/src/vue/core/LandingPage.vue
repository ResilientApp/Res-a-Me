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
      id = "userNameDisplay"
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
          src="../../../public/images/icons/Res-A-Me.png"
        ></v-img>

        <v-autocomplete
          v-model="friends"
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
          >
            Res-A-Me Search
          </v-btn>
          <v-btn
            variant="flat"
            color="#ededf0"
            style="text-transform: none; letter-spacing: 0px"
          >
            I'm Feeling Lucky
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
                <v-avatar
                  icon="mdi-account"
                  color="black"
                  variant="tonal"
                  class="mb-2"
                ></v-avatar>

                <div class="text-caption text-truncate">My Resume</div>
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
  mounted() {
    document.getElementById("signinButton").style.display = "none";
    document.getElementById("profileShortcut").style.display = "none";
    document.getElementById("logoutButton").style.display = "none";
    document.getElementById("userNameDisplay").style.display = "none";

    fetch("http://127.0.0.1:3033/loadUser", {
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
          console.log("User has logged in");
          console.log("Logged in user's email: ", json.logged_in_as);
          this.userName = json.logged_in_as;
          document.getElementById("profileShortcut").style.display = "block";
          document.getElementById("logoutButton").style.display = "block";
          document.getElementById("userNameDisplay").style.display = "block";
        } else {
          this.errorMessage = "User are not logged in";
          console.log("User are not logged in");
          document.getElementById("signinButton").style.display = "block";
        }
      })
      .catch((error) => {
        console.error("There was an error!", error);
        this.errorMessage =
          error.message || "An error occurred. Please try again.";
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
          console.log(json);
          // Handle successful logout
          // Redirect user to landing page
          if (json.message === "Logout successful") {
            console.log(json.message);
            sessionStorage.clear();
            document.getElementById("logoutButton").style.display = "none";
            document.getElementById("signinButton").style.display = "block";
            document.getElementById("profileShortcut").style.display = "none";
            alert("Logout successful");
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
  },
  data() {
    const srcs = {
      1: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
      2: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
      3: "https://cdn.vuetifyjs.com/images/lists/3.jpg",
      4: "https://cdn.vuetifyjs.com/images/lists/4.jpg",
      5: "https://cdn.vuetifyjs.com/images/lists/5.jpg",
    };

    return {
      userName: "User",
      autoUpdate: true,
      isUpdating: false,
      name: "Midnight Crew",
      friends: [],
      people: [
        // TODO: https://github.com/vuetifyjs/vuetify/issues/15721
        // { header: 'Group 1' },
        { name: "Sandra Adams", group: "Group 1", avatar: srcs[1] },
        { name: "Ali Connors", group: "Group 1", avatar: srcs[2] },
        { name: "Trevor Hansen", group: "Group 1", avatar: srcs[3] },
        { name: "Tucker Smith", group: "Group 1", avatar: srcs[2] },
        // { divider: true },
        // { header: 'Group 2' },
        { name: "Britta Holt", group: "Group 2", avatar: srcs[4] },
        { name: "Jane Smith ", group: "Group 2", avatar: srcs[5] },
        { name: "John Smith", group: "Group 2", avatar: srcs[1] },
        { name: "Sandra Williams", group: "Group 2", avatar: srcs[3] },
      ],
      title: "The summer breeze",
      timeout: null,
    };
  },
};
</script>

<style>
body {
  background-color: #fcfcfc !important;
  font: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu,
    Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif !important;
  -webkit-font-smoothing: antialiased !important;
  -moz-osx-font-smoothing: grayscale !important;
}
</style>
