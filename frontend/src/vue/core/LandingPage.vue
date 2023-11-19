<template>
  <v-app style="width: 100%; height: 100%">
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
      @click="signin">
      Sign in
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

        <v-container class="text-center pt-15">
          <v-row justify="center" dense>
            <!-- <v-col v-for="(shortcut, i) in shortcuts" :key="i" cols="auto">
              <v-card
                :href="shortcut.href"
                class="pa-4"
                flat
                rel="noopener noreferer"
                target="_blank"
                width="112"
              >
                <v-avatar
                  :icon="shortcut.icon"
                  color="black"
                  variant="tonal"
                  class="mb-2"
                ></v-avatar>

                <div
                  class="text-caption text-truncate"
                  v-text="shortcut.title"
                ></div>
              </v-card>
            </v-col> -->

            <!-- <v-col cols="auto">
              <v-dialog v-model="dialog" max-width="500">
                <template v-slot:activator="{ props }">
                  <v-card flat width="112" v-bind="props" class="pa-4">
                    <v-avatar
                      icon="mdi-plus"
                      color="black"
                      variant="tonal"
                      class="mb-2"
                    ></v-avatar>

                    <div class="text-caption text-truncate">Add shortcut</div>
                  </v-card>
                </template>

                <v-card title="Add shortcut" rounded="lg">
                  <template v-slot:text>
                    <v-label class="text-caption">Name</v-label>
                    <v-text-field
                      density="compact"
                      variant="solo-filled"
                      flat
                    ></v-text-field>

                    <v-label class="text-caption">URL</v-label>

                    <v-text-field
                      density="compact"
                      variant="solo-filled"
                      flat
                    ></v-text-field>
                  </template>

                  <div class="py-4 px-5 text-end">
                    <v-btn
                      border
                      class="text-none me-2"
                      color="blue"
                      text="Cancel"
                      variant="text"
                      @click="dialog = false"
                    ></v-btn>

                    <v-btn
                      class="text-none"
                      color="blue"
                      text="Done"
                      variant="flat"
                      @click="dialog = false"
                    ></v-btn>
                  </div>
                </v-card>
              </v-dialog>
            </v-col> -->
          </v-row>
        </v-container>
      </v-responsive>
    </v-card>
  </v-app>
</template>

<script>
export default {
  mounted() {
    fetch("http://127.0.0.1:3033/loadUser", {
        method: "GET",
        headers: {
          "Content-type": "application/json; charset=UTF-8",
          "Authorization": `Bearer ` + sessionStorage.getItem('access_token'),
        }
    })
    .then((response) => response.json())
    .then((json) => {
        if (json.status === 200) {
            console.log("User has logged in")
            console.log("Logged in user's email: ", json.logged_in_as)
        }
        else {
            this.errorMessage = "User are not logged in";
        }
    })
    .catch(error => {
        console.error('There was an error!', error);
        this.errorMessage = error.message || "An error occurred. Please try again.";
    });
  },
  methods:{
    signin(){
      this.$router.push('/login')
    }
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
      shortcuts: [
        {
          icon: "mdi-github",
          title: "Master",
          href: "https://github.com/vuetifyjs/vuetify",
          color: "white",
        },
        {
          icon: "mdi-github",
          title: "Dev",
          href: "https://github.com/vuetifyjs/vuetify/tree/dev",
        },
        {
          icon: "mdi-github",
          title: "Stable",
          href: "https://github.com/vuetifyjs/vuetify/tree/v2-stable",
        },
        {
          icon: "mdi-github",
          title: "My Pull Requests",
          href: "https://github.com/vuetifyjs/vuetify/pulls/johnleider",
        },
      ],
      title: "The summer breeze",
      timeout: null,
    };
  }
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
