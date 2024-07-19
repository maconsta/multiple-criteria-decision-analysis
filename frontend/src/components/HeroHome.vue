<template>
  <!-- Hero Section -->
  <section class="hero" id="home">
    <div class="container hero-content row">
      <div class="col row">
        <div>
          <h1>Welcome to SynthetIQ Decider</h1>
          <p>Your new advisor!</p>
        </div>
      </div>
      <div class="col row">
        <div>
          <img src="../assets/images/heroLogo.png" alt="" />
        </div>
      </div>
    </div>
  </section>
  <!-- End Hero Section -->

  <section class="wave">
    <div>
      <h1>Welcome to SynthetIQ Decider</h1>
      <p>Your new advisor!</p>
    </div>
    <div class="col row">
      <div>
<!--        <img src="../assets/images/heroImg3.png" alt="" />-->
      </div>
    </div>
  </section>
  <!-- End Hero Section -->

  <section class="wave">
    <div></div>
  </section>

  <!-- Resources -->
  <section class="resource" id="resource">
    <div class="container feature-content row">
      <div class="col column">
        <div class="icon">
          <Icon icon="flowbite:brain-solid" style="font-size: 50px" />
        </div>
        <h3>Method AHP</h3>
        <p>AHP is one of the most popular MCDM Methods</p>
      </div>
      <div class="col column">
        <div class="icon">
          <Icon icon="flowbite:brain-solid" style="font-size: 50px" />
        </div>
        <h3>Method TOPSIS</h3>
        <p>TOPSIS is one of the most popular MCDM Methods</p>
      </div>
      <div class="col column">
        <div class="icon">
          <Icon icon="flowbite:brain-solid" style="font-size: 50px" />
        </div>
        <h3>Method ELECTRE I</h3>
        <p>ELECTRE I is one of the most popular MCDM Methods</p>
      </div>
    </div>
  </section>
  <!--End Resources -->

  <!-- About Us -->
  <section class="about" id="about">
    <div class="container about-content column">
      <h3>About Information</h3>
      <p>We are the biggest company that sells MCDM software products.</p>
      <div>
        <img src="../assets/images/about.png" alt="" />
      </div>
      <a href="#" class="btn">Read More</a>
    </div>
  </section>
  <!-- End About Us -->

  <!-- Footer -->
  <footer class="footer" id="contact">
    <div class="container">
      <a href="#" class="logo">
        <h1>SynthetIQ</h1>
      </a>
      <div class="footer-content row">
        <div class="col column">
          <h2>Address</h2>
          <p>Bulgaria, Sofia 1000</p>
        </div>
        <div class="col column">
          <h2>Social Link</h2>
          <ul class="row">
            <li>
              <a href="#" class="facebook-icon">
                <Icon icon="fe:facebook" style="font-size: 30px" />
              </a>
            </li>
            <li>
              <a href="#" class="instagram-icon">
                <Icon icon="mdi:instagram" style="font-size: 30px" />
              </a>
            </li>
            <li>
              <a href="#" class="x-icon">
                <Icon
                  icon="fa6-brands:square-x-twitter"
                  style="font-size: 30px"
                />
              </a>
            </li>
          </ul>
        </div>
      </div>
      <div class="reserved">
        <h4>© SynthetIQ Decider. All rights reserved</h4>
      </div>
    </div>
  </footer>
  <!-- End Footer -->
</template>

<script>
import { Icon } from "@iconify/vue";

export default {
  name: "HeaderHome",
  components: {
    Icon,
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
  background-color: #fff;
}

img {
  width: 900px;
  height: 300px;
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

/* Hero Section */
.hero {
  background-color: #2c64ff;
  padding-top: 10em;
}

.hero-content > * {
  flex-basis: 100%;
}

.hero-content .col {
  justify-content: center;
  align-items: center;
}

.hero-content .col img {
  margin-left: 140px;
  max-width: 300px;
}

.hero-content h1 {
  font-weight: 900;
  font-size: 3.2em;
  padding-bottom: 0.5em;
  color: #fff;
}

.hero-content p {
  font-weight: 500;
  font-size: 1.3em;
  color: #fff;
}

/* End Hero Section */

/* Wave */

.wave {
  background-color: #2c64ff;
  background-image: url("../assets/images/hero-1-bottom-shape.png");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  padding: 11em 0;
  color: #fff;
}

/* Resources */
/*
.resource {
    background-color: #4169e1;
    background-image: url("../assets/images/hero-1-bottom-shape.png");
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    padding: 15em 0;
    color: #fff;
}
*/

.resource {
  padding-top: 50px;
  /* Adjust the value as needed */
  align-items: center;
}

.resource-content > * {
  flex-basis: 100%;
}

.resource-content {
  padding-top: 15em;
  gap: 2.5em;
  align-items: center;
}

.resource-content .col {
  text-align: center;
  gap: 2em;
}

.icon {
  position: relative;
  padding: 2em 0;
}

.row {
  display: flex;
  justify-content: center;
  width: 100%;
}

.column {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  gap: 2em;
}

.icon::after {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100px;
  /* Adjust if needed */
  height: 100px;
  /* Adjust if needed */
  content: "";
  border: solid 2px black;
  transform: translate(-50%, -50%) rotate(45deg);
  transition: transform 0.3s ease-in-out;
}

.resource .col:hover .icon::after {
  transform: translate(-50%, -50%) rotate(90deg);
  /* Or any degree you prefer */
  transition: transform 0.3s ease-in-out;
  /* Smooth transition */
}

.resource-content col h3 {
  font-weight: 500;
  font-size: 2em;
  align-items: center;
}

.resource-content p {
  font-weight: 300;
  font-size: 1em;
  text-align: center;
}

/* About us */
.about-content {
  text-align: center;
  grid-gap: 3em;
  padding: 5em 0;
  background-color: #fff;
}

.about-content h3 {
  font-weight: 500;
  font-size: 2.5em;
}

.about-content p {
  font-weight: 300;
  font-size: 1.5em;
  max-width: 1100px;
  margin: 0 auto;
}

.about-content img {
  height: 350px;
  max-width: 500px;
}

.btn {
  font-weight: 900;
  font-size: 1.5em;
  background-color: #2c64ff;
  padding: 0.7em 0;
  width: 200px;
  margin: 0 auto;
  color: #fff;
  border-radius: 10px;
  -webkit-border-radius: 10px;
  -moz-border-radius: 10px;
  -ms-border-radius: 10px;
  -o-border-radius: 10px;
  transition: 0.3s ease-in-out;
  -webkit-transition: 0.3s ease-in-out;
  -moz-transition: 0.3s ease-in-out;
  -ms-transition: 0.3s ease-in-out;
  -o-transition: 0.3s ease-in-out;
}

.btn:hover {
  opacity: 1;
  color: #2cffc7;
}

/* End About */

/* Footer */

.footer {
  background-color: #2c64ff;
  padding: 0.1em 0;
}

.footer h1 {
  text-align: center;
  color: #fff;
  padding: 0.2em;
  font-size: 2em;
}

.footer-content {
  padding: 0.6em 0;
  gap: 60em;
}

.footer-content > * {
  flex-basis: 100%;
}

.footer-content .col {
  gap: 1em;
  color: #fff;
}

.footer-content h2 {
  text-align: center;
  font-weight: 900;
  font-size: 1em;
}

.footer-content p {
  font-weight: 500;
  font-size: 1em;
}

.footer-content ul {
  padding: 0;
  align-items: center;
  gap: 2em;
}

.footer h4 {
  color: #2cffc7;
  font-size: 0.7em;
  font-weight: 600;
  text-align: center;
}

.facebook-icon:hover {
  color: #5d93ff;
}

.instagram-icon:hover {
  color: #bc318f;
}

.x-icon:hover {
  color: black;
  /* This will apply only to the Facebook icon */
}

@media screen and (max-width: 1100px) {
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

@media screen and (max-width: 900px) {
  .hero {
    padding-bottom: 4em;
  }

  .hero-content {
    flex-wrap: wrap;
    gap: 3em;
  }

  .hero-content h1 {
    text-align: center;
  }

  .resource {
    background-image: unset;
  }

  .resource-content {
    flex-wrap: wrap;
    padding-top: unset;
  }

  .about-content img {
    max-width: 100%;
  }

  .about-content {
    flex-wrap: wrap;
  }
}

@media (max-width: 768px) {
  .resource {
    margin-top: 20px;
  }
}
</style>
