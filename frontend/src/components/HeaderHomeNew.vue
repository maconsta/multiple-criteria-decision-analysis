<template>
  <!-- Navigation -->
  <header :class="{ 'small-header': isScrolled }">
    <div class="container header">
      <a href="#" class="logo">
        <h1>Synthet<span>IQ</span></h1>
      </a>
      <div class="toggleMenu" @click="toggleMenu">
        <span></span>
        <span></span>
        <span></span>
      </div>
      <nav class="navigation" :class="{ active: isMenuOpen }">
        <ul>
          <li><a href="#home" @click="closeMenu">Home</a></li>
          <li><a href="#solution" @click="closeMenu">Solutions</a></li>
          <li><a href="#resource" @click="closeMenu">Resources</a></li>
          <li><a href="#about" @click="closeMenu">About Us</a></li>
          <li><a href="/signIn" @click="closeMenu">Sign In</a></li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script>
export default {
  name: "HeaderHomeNew",
  data() {
    return {
      isScrolled: false,
      isMenuOpen: false, // Controls the visibility of the mobile menu
    };
  },
  methods: {
    handleScroll() {
      this.isScrolled = window.scrollY > 50;
    },
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen; // Toggle the menu state
    },
    closeMenu() {
      this.isMenuOpen = false; // Close the menu when a link is clicked
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
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: "Montserrat", sans-serif;
  width: 100%;
  overflow-x: hidden; /* Prevent horizontal scrolling */
}

img {
  max-width: 100%;
  height: auto; /* Ensure images are responsive */
}

.hero {
  width: 100%; /* Full width */
  min-height: 400px; /* Adjust height as needed */
  background-color: #f0f4f8; /* Example background color */
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 60px 20px; /* Adjust padding for smaller screens */
  margin-top: 60px; /* Account for the fixed header height */
}

.hero h1 {
  font-size: clamp(32px, 6vw, 48px); /* Responsive font size */
  color: #2c64ff;
  margin-bottom: 20px;
}

.hero p {
  font-size: clamp(18px, 3vw, 24px); /* Responsive font size */
  color: #333;
  margin-bottom: 30px;
}

.hero .cta-button {
  font-size: clamp(16px, 3vw, 20px); /* Responsive font size */
  padding: 10px 20px;
  background-color: #2c64ff;
  color: #fff;
  border-radius: 5px;
  text-decoration: none;
  transition: background-color 0.3s ease;
}

.hero .cta-button:hover {
  background-color: #1e4fd1;
}

.container {
  max-width: 100%; /* Ensure the container doesn't exceed the viewport */
  width: 100%;
  margin: 0 auto;
  padding: 0 20px; /* Add padding for smaller screens */
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
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
  position: fixed;
  width: 100%;
  transition: all 0.3s ease;
  padding: 10px 0;
  z-index: 1000; /* Ensure the header is above other content */
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

.logo h1 {
  font-weight: 900;
  font-size: clamp(30px, 4vw, 60px);
  color: #fff;
}

.logo span {
  color: #2cffc7;
}

nav ul {
  display: flex;
  gap: 2.5em;
  align-items: center;
}

nav a {
  font-weight: 500;
  font-size: 18px;
  color: #fff;
}

nav a:hover {
  color: #2cffc7;
}

/* Toggle Menu Icon */
.toggleMenu {
  display: none; /* Hidden by default */
  flex-direction: column;
  justify-content: space-around;
  width: 30px;
  height: 24px;
  cursor: pointer;
}

.toggleMenu span {
  width: 100%;
  height: 3px;
  background-color: #fff;
  transition: all 0.3s ease;
}

/* Mobile Navigation */
@media screen and (max-width: 1300px) {
  .toggleMenu {
    display: flex; /* Show toggle menu icon on smaller screens */
  }

  .navigation {
    position: fixed; /* Change to fixed positioning */
    top: 60px; /* Position below the header */
    right: 0;
    width: 250px; /* Smaller dropdown menu */
    height: calc(100vh - 60px); /* Full height minus header */
    background-color: #2c64ff;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    transform: translateX(100%); /* Hide the menu off-screen by default */
    transition: transform 0.3s ease-in-out;
    z-index: 999;
    padding: 20px 0;
    box-shadow: -2px 2px 5px rgba(0, 0, 0, 0.2);
    overflow-y: auto; /* Add scroll if content overflows */
  }

  .navigation.active {
    transform: translateX(0); /* Slide the menu into view */
  }

  .navigation ul {
    flex-direction: column;
    gap: 1.5em;
    text-align: left;
    padding-left: 20px;
  }

  .navigation ul li a {
    font-size: 18px; /* Normal text size for dropdown */
  }
}

/* Fix blank white space issues */
@media screen and (max-width: 1400px) {
  .container {
    padding: 0 15px; /* Adjust padding for medium screens */
  }
}

@media screen and (max-width: 1050px) {
  .container {
    padding: 0 10px; /* Adjust padding for smaller screens */
  }
}

@media screen and (max-width: 650px) {
  .container {
    padding: 0 5px; /* Adjust padding for very small screens */
  }

  .logo h1 {
    font-size: clamp(24px, 6vw, 30px); /* Adjust logo size for small screens */
  }

  .navigation {
    width: 200px; /* Smaller dropdown menu for very small screens */
  }
}

@media screen and (max-width: 768px) {
  .hero {
    min-height: 300px; /* Adjust height for smaller screens */
    padding: 40px 15px; /* Adjust padding for smaller screens */
    margin-top: 50px; /* Adjust for smaller header height */
  }

  .hero h1 {
    font-size: 28px; /* Smaller font size for mobile */
  }

  .hero p {
    font-size: 16px; /* Smaller font size for mobile */
  }

  .hero .cta-button {
    font-size: 14px; /* Smaller font size for mobile */
    padding: 8px 16px;
  }
}

@media screen and (max-width: 480px) {
  .hero {
    min-height: 250px; /* Adjust height for very small screens */
    padding: 30px 10px; /* Adjust padding for very small screens */
    margin-top: 40px; /* Adjust for very small header height */
  }

  .hero h1 {
    font-size: 24px; /* Smaller font size for very small screens */
  }

  .hero p {
    font-size: 14px; /* Smaller font size for very small screens */
  }

  .hero .cta-button {
    font-size: 12px; /* Smaller font size for very small screens */
    padding: 6px 12px;
  }

}
</style>