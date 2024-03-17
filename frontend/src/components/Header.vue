<template>
  <header>
    <nav class="nav">
      <router-link :to="{ name: 'home' }" class="link">
        <span class="home-btn"><span class="home-btn__img"></span></span>
        <span class="nav__text">Home</span>
      </router-link>
      <router-link :to="{ name: 'projects' }" class="link">
        <span class="projects-btn"><span class="projects-btn__img"></span></span>
        <span class="nav__text">Projects</span>
      </router-link>
    </nav>
  </header>
</template>

<script>

export default {
  name: "Header",
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
header {
  background-color: $white-smoke;
  box-shadow: 0 2px 10px rgba($color: #c6c6c6, $alpha: 1.0);
  padding: 20px;
  height: 75px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.nav {
  display: flex;
  align-items: center;
  column-gap: 10px;

  &__text {
    padding-top: 4px;
  }
}

.home-btn {
  display: flex;
  align-items: center;
  justify-content: center;

  &__img {
    background: url("../assets/images/home.svg");
    background-repeat: no-repeat;
    background-size: 25px;
    width: 25px;
    height: 25px;
  }
}

.projects-btn {
  display: flex;
  align-items: center;
  justify-content: center;

  &__img {
    background: url("../assets/images/folder.svg");
    background-repeat: no-repeat;
    background-size: 25px;
    width: 25px;
    height: 25px;
  }
}

.link {
  display: flex;
  align-items: center;
  justify-content: space-between;
  column-gap: 5px;
  border-radius: 8px;
  padding: 4px;
}

.router-link-exact-active {
  background-color: $blue-lagoon-20;
}
</style>
