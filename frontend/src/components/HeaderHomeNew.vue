<template>
    <!-- Navigation -->
    <header :class="{'small-header': isScrolled}">
        <div class="container header row">
            <a href="#" class="logo">
                <h1>Synthet<span>IQ</span></h1>
            </a>
            <div class="toggleMenu" v-on:click="toggleMenu"></div>
            <nav class="navigation row">
                <ul class="row">
                    <li><a href="#home">Home</a></li>
                    <li><a href="#solution">Solutions</a></li>
                    <li><a href="#resource">Resources</a></li>
                    <li><a href="#about">About Us</a></li>
                    <a href= "/signIn">Sign In</a>
                </ul>
            </nav>
        </div>
    </header>
</template>

<script>
/* Custum Function */
function toggleMenu() {
  const toggleMenu = document.querySelector(".toggleMenu");
  const navigation = document.querySelector(".navigation");
  toggleMenu.classList.toggle("active");
  navigation.classList.toggle("active");
}

export default {
  name: "HeaderHomeNew",
  data() {
    return {
      isScrolled: false,
    };
  },
  methods: {
    handleScroll() {
      this.isScrolled = window.scrollY > 50;
    },
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.handleScroll);
  },
};
</script>

<style scoped>
*,
*::before,
*::after {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: "Montserrat", sans-serif;
  margin: 0;
}

img {
  max-width: 100%;
}

.container {
  max-width: 90%;
  margin: 0 auto;
}

.row {
  display: flex;
}

.column {
  display: grid;
}

a {
  text-decoration: none;
}

ul {
  list-style: none;
}

:is(h1, h2, h3, p) {
  margin: 0;
}

/* Navigation */
header {
  background-color: #2c64ff;
}

header {
  position: fixed;
  width: 100%;
  transition: all 0.3s ease;
  padding: 10px 0;
}

.small-header {
  font-size: 1em;
  padding: 8px 0;
}

.small-header .logo h1,
.small-header nav ul li a {
  transition: all 0.3s ease;
  font-size: 1em;
}

.small-header a {
  font-size: 1em;
}

.header {
  justify-content: space-between;
  align-items: center;
}

.logo h1 {
  font-weight: 900;
  font-size: clamp(30px, 4vw, 60px);
  color: #fff;
}

.logo span {
  color: #2cffc7;
}

nav ul {
  gap: 2.5em;
}

nav a {
    font-weight: 500;
    font-size: 18px;
    color: #fff;
}

nav a:hover {
  opacity: 1.5;
  color: #2cffc7;
}

.navigation {
  transition: transform 0.3s ease-in-out;
  -webkit-transition: transform 0.3s ease-in-out;
  -moz-transition: transform 0.3s ease-in-out;
  -ms-transition: transform 0.3s ease-in-out;
  -o-transition: transform 0.3s ease-in-out;
}

/* End Navigation */

@media screen and (max-width: 1010px) {
  .toggleMenu {
    position: absolute;
    right: 15px;
    background-image: url("../assets/images/toggleMenu.png");
    background-position: center;
    background-repeat: no-repeat;
    background-size: 30px;
    width: 30px;
    height: 30px;
    padding: 2em;
    z-index: 1000;
  }
  .toggleMenu.active {
    position: fixed;
    background-size: 25px;
  }

  .navigation {
    justify-content: center;
    flex-direction: column;
    transform: scale(1, 0);
    -webkit-transform: scale(1, 0);
    -moz-transform: scale(1, 0);
    -ms-transform: scale(1, 0);
    -o-transform: scale(1, 0);
    transform-origin: top;
    max-height: 0;
    opacity: 0;
  }

  .navigation.active {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    transform: scale(1, 0);
    -webkit-transform: scale(1, 0);
    -moz-transform: scale(1, 0);
    -ms-transform: scale(1, 0);
    -o-transform: scale(1, 0);
    max-height: 100%;
    opacity: 1;
    z-index: 999;
    background-color: #2c64ff;
  }
  .navigation ul {
    flex-direction: column;
    text-align: center;
  }
}
</style>
