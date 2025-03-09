<template>
  <!-- Rotate Screen Message -->
  <div class="rotate-screen-message">
    <Icon icon="mdi:rotate-3d" class="rotate-icon" />
    <p>Please rotate your device to view the content.</p>
  </div>

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
    <div></div>
  </section>

  <!-- Resources -->
  <section class="resource" id="resource">
    <div class="container feature-content row">
      <div class="col column">
        <div class="icon">
          <Icon icon="flowbite:brain-solid" style="font-size: 50px" />
        </div>
        <div class="tooltip">
          <h2>Method AHP</h2>
          <div class="toolcontent">
            <h3>What is AHP</h3>
            <p>
              The Analytic Hierarchy Process (AHP) is a method for organizing
              and analyzing complex decisions, using math and psychology. It was
              developed by Thomas L. Saaty in the 1970s and has been refined
              since then. It contains three parts: the ultimate goal or problem
              you’re trying to solve, all of the possible solutions, called
              alternatives, and the criteria you will judge the alternatives on.
              AHP provides a rational framework for a needed decision by
              quantifying its criteria and alternative options, and for relating
              those elements to the overall goal.
            </p>
          </div>
        </div>
      </div>
      <div class="col column">
        <div class="icon">
          <Icon icon="flowbite:brain-solid" style="font-size: 50px" />
        </div>
        <div class="tooltip">
          <h2>Method TOPSIS</h2>
          <div class="toolcontent">
            <h3>What is TOPSIS</h3>
            <p>
              The Technique for Order of Preference by Similarity to Ideal
              Solution (TOPSIS) is a multi-criteria decision analysis method,
              which was originally developed by Ching-Lai Hwang and Yoon in
              1981[1] with further developments by Yoon in 1987,[2] and Hwang,
              Lai and Liu in 1993.[3] TOPSIS is based on the concept that the
              chosen alternative should have the shortest geometric distance
              from the positive ideal solution (PIS) and the longest geometric
              distance from the negative ideal solution (NIS).
            </p>
          </div>
        </div>
      </div>
      <div class="col column">
        <div class="icon">
          <Icon icon="flowbite:brain-solid" style="font-size: 50px" />
        </div>
        <div class="tooltip">
          <h2>Method ELECTRE I</h2>
          <div class="toolcontent">
            <h3>What is ELECTRE I</h3>
            <p>
              ÉLECTRE is a family of multi-criteria decision analysis (MCDA)
              methods that originated in Europe in the mid-1960s. The acronym
              ÉLECTRE stands for: ÉLimination Et Choix Traduisant la REalité
              ("Elimination and Choice Translating Reality"). The method was
              first proposed by Bernard Roy and his colleagues at SEMA
              consultancy company. A team at SEMA was working on the concrete,
              multiple criteria, real-world problem of how firms could decide on
              new activities and had encountered problems using a weighted sum
              technique. Roy was called in as a consultant and the group devised
              the ELECTRE method.
            </p>
          </div>
        </div>
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
import axios from "axios";

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
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: "Montserrat", sans-serif;
  width: 100%;
  overflow-x: hidden;
}

img {
  max-width: 100%;
  height: auto; 
}

.navigation {
  max-width: 1200px; 
  width: 100%;
  margin: 0 auto;
  padding: 0 20px; 
}

.container {
  width: 100%;
  max-width: 1200px; 
  margin: 0 auto;
  padding: 0 20px; 
}

/* Hero Section */
.hero {
  background-color: #2c64ff;
  padding: 100px 0;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
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


/* Wave Section */
.wave {
  background-color: #2c64ff;
  background-image: url("../assets/images/hero-1-bottom-shape.png");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  padding: 11em 0;
  color: #fff;
}

/* Resources Section */

.resource {
  padding-top: 100px;
  align-items: center;
  justify-content: center;
  margin-left: 47px;
}

.resource .feature-content {
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
  gap: 20px;
  width: 100%; 
  margin-right: 11%;
}

.resource .col {
  flex: 1;
  text-align: center;
  position: relative;
}

.resource-content > * {
  flex-basis: 100%;
}

.resource-content {
  padding-top: 15em;
  gap: 2.5em;
  align-items: center;
  justify-content: center;
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
  align-items: center;
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
  height: 100px;
  content: "";
  border: solid 2px black;
  transform: translate(-50%, -50%) rotate(45deg);
  transition: transform 0.7s ease-in-out;
}

.resource .col:hover .icon::after {
  transform: translate(-50%, -50%) rotate(90deg);
  border: solid 2px #2cffc7;
  transition: transform 0.7s ease-in-out;
}

/* Change icon color on hover */
.resource .col:hover .icon {
  filter: invert(60%) sepia(110%) saturate(510%) hue-rotate(190deg);
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

.tooltip {
  position: relative;
}

h2 {
  color: #2c64ff;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 3px;
  margin: 30px;
  cursor: pointer;
  transition: 0.3s;
}

h2:hover {
  opacity: 0.7;
}

.toolcontent {
  width: 162%;
  max-width: 600px;
  background-color: #2cffc7;
  padding: 10px;
  position: absolute;
  bottom: -100%;
  margin-right: 5px;
  border-radius: 5px;
  visibility: hidden;
  opacity: 0;
  transition: opacity 0.7s ease, visibility 0.3s ease;
  transition-delay: 0.7s; 
  z-index: 2;
}

.toolcontent h3 {
  text-transform: uppercase;
  font-weight: 900;
  margin-bottom: 15px;
}

.toolcontent p {
  line-height: 1.4;
}

.column:hover .toolcontent {
  visibility: visible;
  opacity: 1;
}

.feature-content {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
  width: 100%;
}

.feature-content .col {
  flex: 1 1 300px;
  text-align: center;
}


/* About Us Section */
.about {
  padding: 100px 0;
  text-align: center;
}

.about-content {
  text-align: center;
  grid-gap: 3em;
  padding: 100px 0;
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

/* Footer Section */
.footer {
  background-color: #2c64ff;
  padding: 10px 0;
  bottom: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  height: auto;
}


.footer h1 {
  text-align: center;
  color: #fff;
  padding: 0.2em;
  font-size: 2em;
}

.footer-content {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 10px;
  padding: 0 20px;
}

.footer-content .col {
  flex: 1 1 200px; 
  text-align: center;
  color: #fff;
}


.footer-content h2 {
  font-weight: 900;
  font-size: 1em; 
  margin-bottom: 5px;
}

.footer-content p {
  font-weight: 500;
  font-size: 0.9em;
  margin-bottom: 5px;
}

.footer-content ul {
  display: flex;
  justify-content: center;
  gap: 10px; 
  padding: 0;
  list-style: none;
}

.footer-content ul li {
  display: inline-block;
}

.footer-content ul li a {
  color: #fff;
  transition: color 0.3s ease;
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
}

.reserved {
  margin-top: 20px;
}

.reserved h4 {
  color: #2cffc7;
  font-size: 0.7em;
  font-weight: 600;
}

/* Rotate Screen Message */
.rotate-screen-message {
  display: none; 
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #2c64ff;
  color: #fff;
  font-size: 1.5em;
  text-align: center;
  padding-top: 30%; 
  z-index: 10000; 
}

.rotate-icon {
  font-size: 4em; 
  margin-bottom: 20px; 
  animation: rotate 2s infinite linear;
}

@keyframes rotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(-360deg);
  }
}

/* Hide all content on small screens */
@media (max-width: 768px) and (orientation: portrait) {
  .rotate-screen-message {
    display: block;
  }

  .hero,
  .wave,
  .resource,
  .about,
  .footer {
    display: none;
  }
}

/* Responsive Adjustments */
@media (max-width: 768px) {

  .toggleMenu {
    display: flex;
  }

  .navigation {
    position: absolute;
    top: 100%;
    right: 0;
    height: 10px;
    width: 100%; 
    background-color: #2c64ff;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    transform: translateX(100%);
    transition: transform 0.3s ease-in-out;
    z-index: 999;
    padding: 10px 0;
    box-shadow: -2px 2px 5px rgba(0, 0, 0, 0.2);
    overflow-y: auto;
    max-height: 20px;
  }

  .navigation.active {
    transform: translateX(0);
  }

  .navigation ul {
    flex-direction: column;
    gap: 0.5em; 
    text-align: left;
    padding-left: 10px;
    width: 100%;
  }

  .navigation ul li a {
    font-size: 14px; 
    padding: 8px 0; 
    display: block; 
  
  }

  .hero-content {
    flex-direction: column;
    text-align: center;
  }

  .hero-content .col img {
    margin-left: 0;
  }


  .feature-content {
    flex-direction: column;
  }

  .footer {
    padding: 5px 0; 
  }

  .footer h1 {
    font-size: 1.2em; 
  }

  .footer-content {
    flex-direction: column; 
    align-items: center;
    gap: 5px; 
  }

  .footer-content .col {
    flex: 1 1 100%; 
  }

  .footer-content h2 {
    font-size: 0.9em; 
  }

  .footer-content p {
    font-size: 0.8em; 
  }

  .footer-content ul {
    gap: 5px;
  }

  .reserved h4 {
    font-size: 0.6em; 
  }
}
</style>
