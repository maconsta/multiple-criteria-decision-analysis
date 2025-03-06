<template>
  <div class="container">
    <HeaderHomeNew />
    <HeroHome />
    <!--<div class="hero">
      <div class="hero-second-img"></div>
    </div>
    <div class="features">Test1</div>
  --></div>
</template>

<script>
import HeaderHomeNew from "@/components/HeaderHomeNew.vue";
import HeroHome from "@/components/HeroHome.vue";
import axiosExtended from "@/router/axiosExtended";

export default {
  name: "HomeView",
  components: {
    HeaderHomeNew,
    HeroHome,
  },
  beforeCreate() {
    const axiosPromise = axiosExtended.get("/is-logged-in");

    axiosPromise
      .then((result) => {
        if (result.data.success === true) {
          this.$router.push({
            name: "homeApp",
          });
        }
      })
      .catch((result) => {});
  },
};
</script>

<style scoped lang="scss">
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html,
body {
  width: 100%;
  overflow-x: hidden; 
}

.container {
  width: 100%;
  max-width: 100vw;
  margin: 0 auto;
  padding: 0;
  overflow-x: hidden; 
}

/* Hero Section Fix */
.hero {
  width: 100%;
  height: 600px;
  background-image: url("../../assets/images/hero-1-bg.png");
  background-color: #1b48fa;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: relative;
  overflow-x: hidden; 
}

/* Ensure second hero image is properly aligned */
.hero-second-img {
  width: 100%;
  height: 200px;
  position: absolute;
  bottom: 0;
  background-image: url("../../assets/images/hero-1-bottom-shape.png");
  background-color: #1b48fa;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  overflow-x: hidden;
}

/* Navigation Fix */
nav {
  width: 100%;
  max-width: 100vw; 
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  padding: 10px 15px;
  box-sizing: border-box;
}

/* Remove any unwanted margin in navigation */
.nav-links {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  margin-left: 0 !important; 
}

/* Make sure all elements fit within the screen */
@media (max-width: 768px) {
  .nav {
    flex-direction: column;
    align-items: center;
    width: 100%;
  }

  .nav-links {
    flex-direction: column;
    align-items: center;
    width: 100%;
  }

  .hero {
    height: auto;
    padding: 50px 0;
  }

  .hero-second-img {
    height: 150px;
  }
}

</style>