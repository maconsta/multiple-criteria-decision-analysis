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

  html, body {
  width: 100%;
  overflow-x: hidden;
}

.container {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    background-color: #2753ff;
  }

.header {
  width: 100%;
  max-width: 100%;
  background-color: #2753ff;
  padding: 1rem 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.nav {
  display: flex;
  flex-wrap: wrap; 
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 1200px; 
  margin: 0 auto;
  padding: 0 10px;
}


  .nav-link {
  text-decoration: none;
  color: #fff;
  font-weight: 500;
  padding: 0.5rem 0.8rem;
  border-radius: 5px;
  transition: background-color 0.3s;
  white-space: nowrap; 
}

  .nav-link:hover {
    background-color: #5375ff;
  }

  .logo {
    width: auto;
    height: auto;
    margin-left: -430px;
    background: url("../assets/images/logo.png");
    font-weight: bold;
    font-size: 1.5rem;
  }

.logo img {
  max-width: 180px; 
  height: auto;
}

.nav-links {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  align-items: center;
}

  .sign-in-wrapper {
    margin-right: 40px; 
  }

  .sign-in-wrapper {
    border: none;
    color: white;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  @media (max-width: 768px) {
  .nav {
    flex-direction: column;
    align-items: center;
    padding: 0;
  }

  .nav-links {
    flex-direction: column;
    width: 100%;
    align-items: center;
    margin-left: 0; 
  }

  .logo img {
    max-width: 150px; 
  }

  .sign-in-wrapper {
    margin-right: 0; 
    text-align: center;
  }
}
  </style>
