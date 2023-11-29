<template>
  <nav class="nav-sidebar">
    <!-- Main Content -->
    <div class="nav-sidebar-content" v-if="profileData">
      <!-- Profile Card -->
      <NavProfileCard :profile-data="profileData" />

      <!-- Nav Link List -->
      <ul class="nav-links">
        <!-- Nav Link -->
        <li
          v-for="section in data.getSections()"
          :class="_getNavItemClassList(section)"
        >
          <button class="nav-link" @click="_onLinkClicked(section)">
            <i :class="section['faIcon']" /> {{ data.getString(section["id"]) }}
          </button>
        </li>
      </ul>

      <ul class="nav-links">
        <li class="nav-item">
          <button class="nav-link" @click="router.push('/')">
            <i class="fa-solid fa-magnifying-glass"></i> Search
          </button>
        </li>
        <li class="nav-item" v-if="checkSession()">
          <button class="nav-link" @click="router.push('/edit')">
            <i class="fa-solid fa-pen-to-square"></i> Edit Resume
          </button>
        </li>
      </ul>
    </div>

    <!-- Footer -->
    <div class="nav-sidebar-footer" v-if="profileData">
      <v-col>
        <v-btn
          v-if="checkSession()"
          variant="flat"
          @click="logout"
          color="#9716f1"
          >Logout</v-btn
        >
        <v-btn
          v-if="!checkSession()"
          variant="flat"
          @click="router.push('/login')"
          color="#9716f1"
          >Login</v-btn
        >
      </v-col>
    </div>
  </nav>
</template>

<script setup>
import NavProfileCard from "../partials/NavProfileCard.vue";
import { useData } from "../../../composables/data.js";
import { useNavigation } from "../../../composables/navigation.js";
import { useRouter } from "vue-router";
import { watchEffect, ref, defineEmits, onBeforeUpdate } from "vue";

const emit = defineEmits(["linkClicked"]);
const data = useData();
const navigation = useNavigation();
const router = useRouter();
const errorMessage = ref("");
const profileData = ref(null);

onBeforeUpdate(() => {
  if (router.currentRoute.value.query["query"]) {
    // If the user has specified a query
    fetchProfileData();
  } 
  else{
    router.push('/login');
  }
});

// Fetch the profile data when component is mounted
watchEffect(async () => {
  await fetchProfileData();
});

async function fetchProfileData() {
  let userEmail = "";

  if (router.currentRoute.value.query["query"]) {
    // If the user has specified a query
    userEmail = router.currentRoute.value.query["query"];
  } else {
    // If the user has logged in
    try {
      const response = await fetch("http://127.0.0.1:3033/loadUser", {
        method: "GET",
        headers: {
          "Content-type": "application/json; charset=UTF-8",
          Authorization: `Bearer ` + sessionStorage.getItem("access_token"),
        },
      });
      const json = await response.json();
      if (json.status === 200) {
        userEmail = json.logged_in_as;
      }
    } catch (error) {
      console.error("Error fetching user data:", error);
    }
  }


  // Update resume to show current user's
  try {
    const response = await fetch("http://127.0.0.1:3033/updateResume", {
      method: "POST",
      headers: {
        "Content-type": "application/json; charset=UTF-8",
      },
      body: JSON.stringify({
        email: userEmail,
      }),
    });
    const json = await response.json();
    if (json.status !== 200) {
      console.error("Error fetching user resume: ", json.message);
    }
  } catch {
    console.error("Error fetching user resume: ", error);
  }
  let profile = data.getProfile();
  profile.profilePictureUrl = `/images/pictures/${userEmail}.png`;
  profileData.value = profile; // Update the ref after fetching data
}

/**
 * @param {Object} section
 * @private
 */
const _getNavItemClassList = (section) => {
  let classList = "nav-item";
  if (navigation.isSectionActive(section["id"])) {
    classList += " nav-item-selected";
  }

  return classList;
};

/**
 * @param {Object} section
 * @private
 */
const _onLinkClicked = (section) => {
  emit("linkClicked", section["id"]);
};

const checkSession = () => {
  return sessionStorage.getItem("access_token") ? true : false;
};

const logout = () => {
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
        router.push("/");
      } else {
        errorMessage.value = json.message || "Logout failed. Please try again.";
      }
    })
    .catch((error) => {
      console.error("Logout error:", error);
      errorMessage.value =
        error.message || "An error occurred. Please try again.";
    });
};
</script>

<style lang="scss" scoped>
@import "/src/scss/_theming.scss";

.nav-sidebar {
  position: fixed;
  display: flex;
  flex-direction: column;

  height: 100vh;
  width: $nav-sidebar-column-size;
  overflow: auto;

  background-color: $nav-background-color;
}

.nav-sidebar-content {
  width: 100%;
  margin: auto 0;
}

ul.nav-links {
  position: relative;
  padding: 0;
  list-style: none;

  @media screen and (min-height: 780px) {
    padding-top: 1rem;
  }
}

li.nav-item {
  display: inline-flex;
  justify-content: left;
  align-items: center;

  padding: 0 2.7rem 0 2.7rem;
  width: 100%;
  min-height: clamp(2rem, calc(100vh / 40) * 2, 2.7rem);

  .nav-link {
    cursor: pointer;
    font-size: clamp(0.9rem, calc(100vh / 50), 1rem);

    font-family: $headings-font-family;
    text-transform: uppercase;
    text-align: center;

    color: $light-1;

    i {
      min-width: 35px;
      color: $nav-item-grayed-out-color;
      transition: color 0.2s;
    }

    &:hover {
      color: $nav-item-lighten-color;
      i {
        color: $nav-item-lighten-strong-color;
      }
    }
  }

  &.nav-item-selected {
    .nav-link {
      color: $nav-item-lighten-color;
      i {
        color: $nav-item-lighten-strong-color;
      }
    }
  }
}

.nav-sidebar-footer {
  text-align: center;
  padding: 0 0 1.5rem 0;
  color: $white;

  .nav-sidebar-footer-credits {
    font-family: $custom-subheadings-font-family;
    color: $light-4;
  }
}
</style>
