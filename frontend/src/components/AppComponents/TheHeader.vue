<template>
  <header>
    <nav>
      <router-link :to="{ name: 'home' }" class="link">
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
  </header>
</template>

<script>
export default {
  name: "TheHeader",
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
header {
  background-color: $main-blue;
  border-bottom: 1px solid $light-gray;
  padding: 20px;
  height: 75px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

nav {
  display: flex;
  align-items: center;
  column-gap: 10px;

  .text {
    padding-top: 4px;
  }
}

.home-btn {
  display: flex;
  align-items: center;
  justify-content: center;

  &__img {
    background: url("../../assets/images/home.svg");
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
    background-image: url("../../assets/images/folder.svg");
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

.router-link-exact-active {
  //background-color: $main-green;
}
</style>
