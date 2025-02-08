<template>
  <div class="container">
    <HeaderHomeNew />
    <HeroHome />
    <!--<div class="hero">
      <div class="hero-second-img">

      </div>
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
}

.conteiner {
  width: 100%;
  height: 100%;
}

.hero {
  width: 100%;
  height: 600px;
  background-image: url("../../assets/images/hero-1-bg.png");
  background-color: #1b48fa;
  background-size: 1800px;
  background-position: center;
  background-repeat: no-repeat;
  position: relative;
}

.hero-second-img {
  width: 100%;
  height: 200px;
  position: absolute;
  bottom: 0;
  background-image: url("../../assets/images/hero-1-bottom-shape.png");
  background-color: #1b48fa;
  background-size: 1800px;
  background-position: center;
  background-repeat: no-repeat;
}

.features {
}
</style>
