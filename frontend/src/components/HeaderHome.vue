<template>
  <header class="header">
    <nav class="nav">
      <div class="logo"></div>
      <img v-bind:src="logoImage" style="width: 250px; height: 150px" />
      <div class="nav-links">
        <router-link to="/" class="nav-link">Home</router-link>
        <router-link :to="{ name: 'solutions' }" class="nav-link"
          >Solutions</router-link
        >
        <router-link to="/resources" class="nav-link">Resources</router-link>
        <router-link to="/about" class="nav-link">About Us</router-link>
      </div>
      <div class="sign-in-wrapper">
        <router-link to="/signIn" class="nav-link">Sign in</router-link>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: "HeaderHome",
  data() {
    return {
      logoImage: require("../assets/images/logo.png"),
    };
  },
};
</script>

<style scoped>
*,
*::before,
*::after {
  box-sizing: border-box;
}

.container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background-color: #2753ff;
}

.header {
  background-color: #2753ff;
  padding: 1rem 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.nav {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.nav-links {
  margin-left: -140px;
}

.nav-link {
  text-decoration: none;
  color: #fff;
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.nav-link:hover {
  background-color: #5375ff;
}

.nav {
  display: flex;
  justify-content: space-between;
  align-items: center; /* Ensure vertical centering */
  gap: 20px;
  width: 100%; /* Use the full width of the header */
  padding: 0 20px; /* Add some padding on the sides */
}

.logo {
  width: auto;
  height: auto;
  margin-left: -430px;
  background: url("../assets/images/logo.png");
  font-weight: bold;
  font-size: 1.5rem;
}

.nav-links {
  display: flex;
  gap: 20px;
  justify-content: center;
  align-items: center;
}

.sign-in-wrapper {
  margin-right: 40px; /* Adjust this value as needed */
}

.sign-in-wrapper {
  border: none;
  color: white;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}
</style>
