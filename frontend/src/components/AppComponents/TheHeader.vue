<template>
  <header>
    <div class="empty-container"></div>
    <nav>
      <router-link :to="{ name: 'homeApp' }" class="link">
        <span class="home-btn"><span class="home-btn__img"></span></span>
        <span class="text">Home</span>
      </router-link>
      <router-link :to="{ name: 'projects' }" class="link">
        <span class="projects-btn">
          <span class="projects-btn__img"></span>
        </span>
        <span class="text">Projects</span>
      </router-link>
    </nav>
    <nav>
      <div class="dropdown">
        <span class="profile-icon" @click="toggleDropdown">{{
          abbreviation
        }}</span>
        <div v-if="isDropdownOpen" class="dropdown-menu">
          <span @click="navigateToProfile" class="dropdown-item">Profile</span>
          <span @click="signOut" class="dropdown-item">Sign Out</span>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import axiosExtended from "@/router/axiosExtended";

export default {
  name: "TheHeader",
  data() {
    return {
      isDropdownOpen: false,
      abbreviation: "",
    };
  },
  methods: {
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen;
    },
    navigateToProfile() {
      this.$router.push({ name: "userProfile" });
      this.isDropdownOpen = false;
    },
    signOut() {
      axiosExtended
        .get("sign-out")
        .then((response) => {
          localStorage.removeItem("accessToken");
          this.$router.push({
            name: "home",
          });
        })
        .catch(() => {
          console.log("Error when signing out...");
        });
      this.isDropdownOpen = false;
    },
  },
  created() {
    axiosExtended.get("/get-user-abbreviation").then((result) => {
      this.abbreviation = result.data.abbreviation;
    });
    this.isDropdownOpen = false;
  },
};
</script>

<style scoped lang="scss">
header {
  background-color: $main-blue;
  border-bottom: 1px solid $light-gray;
  padding: 20px;
  height: 75px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

nav {
  display: flex;
  align-items: center;
  column-gap: 10px;

  .text {
    padding-top: 4px;
  }
}

.home-btn,
.projects-btn {
  display: flex;
  align-items: center;
  justify-content: center;

  &__img {
    background-repeat: no-repeat;
    background-size: 25px;
    width: 25px;
    height: 25px;
  }
}

.home-btn__img {
  background-image: url("../../assets/images/home.svg");
}

.projects-btn__img {
  background-image: url("../../assets/images/folder.svg");
}

.link {
  display: flex;
  align-items: center;
  justify-content: space-between;
  column-gap: 5px;
  border-radius: 8px;
  padding: 4px;
  color: #fff;
  font-weight: 900;

  &:hover {
    color: $main-green;

    .projects-btn__img {
      background-image: url("../../assets/images/folder_green.svg");
    }

    .home-btn__img {
      background-image: url("../../assets/images/home_green.svg");
    }
  }
}

.profile-icon {
  width: 35px;
  height: 35px;
  background-color: #ffffff;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  color: #2c64ff;
}

.dropdown {
  position: relative;
}

.dropdown-menu {
  position: absolute;
  top: 45px;
  right: 0;
  background-color: #2c64ff;
  border-radius: 8px;
  padding: 10px 0;
  min-width: 150px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
  display: flex;
  flex-direction: column;
  gap: 8px;
  animation: fadeIn 0.2s ease-in-out;
  z-index: 100;
}

.dropdown-item {
  color: #fff;
  padding: 10px 20px;
  cursor: pointer;
  transition: background-color 0.2s;

  &:hover {
    background-color: rgba(255, 255, 255, 0.1);
  }
}

.profile-icon {
  width: 35px;
  height: 35px;
  background-color: #ffffff; /* Placeholder color for profile icon */
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  color: #2c64ff;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-5px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
