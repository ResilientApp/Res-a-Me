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
      "
    >
      Sign in
    </v-btn>

    <v-card
      theme="light"
      class="pa-8 d-flex justify-center align-center flex-wrap"
      style="width: 100%; height: 100%"
    >
      <v-responsive max-width="550">
        <v-img
          class="mx-auto mt-12 mb-16"
          max-height="140"
          max-width="240"
          src="https://cdn.vuetifyjs.com/docs/images/logos/vuetify-logo-light-text.svg"
        ></v-img>

        <v-autocomplete
          :items="items"
          append-inner-icon="mdi-microphone"
          auto-select-first
          class="flex-full-width"
          density="comfortable"
          item-props
          menu-icon=""
          placeholder="Search People"
          prepend-inner-icon="mdi-magnify"
          rounded
          theme="light"
          variant="outlined"
        ></v-autocomplete>

        <v-container class="text-center">
          <v-row justify="center" dense>
            <v-col v-for="(shortcut, i) in shortcuts" :key="i" cols="auto">
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
                  color="white"
                  variant="tonal"
                  class="mb-2"
                ></v-avatar>

                <div
                  class="text-caption text-truncate"
                  v-text="shortcut.title"
                ></div>
              </v-card>
            </v-col>

            <v-col cols="auto">
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
            </v-col>
          </v-row>
        </v-container>
      </v-responsive>
    </v-card>
  </v-app>
</template>

<script setup></script>

<style lang="scss">
body {
  background-color: #fcfcfc;
}
</style>
