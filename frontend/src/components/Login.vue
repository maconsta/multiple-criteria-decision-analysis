<template>
  <!-- Rotate Screen Message -->
  <div class="rotate-screen-message">
    <Icon icon="mdi:rotate-3d" class="rotate-icon" />
    <p>Please rotate your device to view the content.</p>
  </div>

  <body>
    <div>
      <div class="container" id="container" :class="{ active: isActive }">
        <div class="form-container sign-up">
          <form @submit.prevent="validateSignUp" @keydown.enter="validateSignUp">
            <h1>Create Account</h1>
            <div class="social-icons">
              <a href="#" class="google-icon" aria-label="Google">
                <Icon icon="mdi:google-plus" style="font-size: 20px"/>
              </a>
              <a href="#" class="facebook-icon" aria-label="Facebook">
                <Icon icon="fe:facebook" style="font-size: 20px"/>
              </a>
              <a href="#" class="git-icon" aria-label="GitHub">
                <Icon icon="mdi:github" style="font-size: 20px"/>
              </a>
            </div>
            <span>or use your email for registration</span>
            <input
                type="text"
                id="first-name"
                placeholder="First Name"
                v-model="signUpData.firstName"
            />
            <input
                type="text"
                id="last-name"
                placeholder="Last Name"
                v-model="signUpData.lastName"
            />
            <input
                type="email"
                id="email"
                placeholder="Email"
                v-model="signUpData.email"
            />
            <input
                type="password"
                id="password"
                placeholder="Password"
                v-model="signUpData.password"
            />
            <div class="button" @click="validateSignUp">Sign Up</div>
            <p v-if="signUpError">{{ signUpError }}</p>
          </form>
        </div>
        <div class="form-container sign-in">
          <form @submit.prevent="validateSignIn" @keydown.enter="validateSignIn">
            <h1>Sign In</h1>
            <div class="social-icons">
              <a href="#" class="google-icon" aria-label="Google">
                <Icon icon="mdi:google-plus" style="font-size: 20px"/>
              </a>
              <a href="#" class="facebook-icon" aria-label="Facebook">
                <Icon icon="fe:facebook" style="font-size: 20px"/>
              </a>
              <a href="#" class="git-icon" aria-label="GitHub">
                <Icon icon="mdi:github" style="font-size: 20px"/>
              </a>
            </div>
            <span>or use your email and password</span>
            <input
                type="email"
                placeholder="Email"
                v-model="signInData.email"
            />
            <input
                type="password"
                placeholder="Password"
                v-model="signInData.password"
            />
            <a href="#">Forget your Password?</a>
            <div class="button" @click="validateSignIn">Sign In</div>
            <p v-if="signInError">{{ signInError }}</p>
          </form>
        </div>
        <div class="toggle-container">
          <div class="toggle">
            <div class="toggle-panel toggle-left">
              <h1>Welcome Back!</h1>
              <p>Enter your personal details to use all of site features</p>
              <div class="button" id="login" @click="deactivateContainer">
                Sign In
              </div>
            </div>
            <div class="toggle-panel toggle-right">
              <h1>Hello, Friend!</h1>
              <p>
                Register with your personal details to use all of site features
              </p>
              <div class="button" id="register" @click="activateContainer">
                Sign Up
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- <div v-if="signUpSuccess" class="success-message">Your account has been successfully created!</div> -->
    </div>
    </body>
</template>

<script>
import {Icon} from "@iconify/vue";
import axiosExtended from "@/router/axiosExtended";

export default {
  name: "Login",
  mounted() {
    this.updateOverflow();
    window.addEventListener("resize", this.updateOverflow); // Listen for screen resize
  },
  beforeUnmount() {
    document.body.style.overflow = ""; // Restore default overflow
    window.removeEventListener("resize", this.updateOverflow); // Remove event listener
  },
  components: {
    Icon,
  },
  data() {
    return {
      isActive: false,
      signUpData: {
        firstName: "",
        lastName: "",
        email: "",
        password: "",
      },
      signInData: {
        email: "",
        password: "",
      },
      signUpError: "",
      signInError: "",
      signUpSuccess: false,
    };
  },
  methods: {
    test() {
      console.log("asdasd");
    },
    updateOverflow() {
      if (window.innerWidth > 900) {
        document.body.style.overflow = "hidden"; // Prevent scrolling on large screens
      } else {
        document.body.style.overflow = "auto"; // Allow scrolling on small screens
      }
    },
    activateContainer() {
      this.isActive = true;
    },
    deactivateContainer() {
      this.isActive = false;
    },
    validateSignUp() {
      const {firstName, lastName, email, password} = this.signUpData;
      if (!firstName || !lastName || !email || !password) {
        this.signUpError = "All fields are required.";
        return;
      }
      if (!this.validateEmail(email)) {
        this.signUpError = "Invalid email format.";
        return;
      }
      if (password.length < 6) {
        this.signUpError = "Password must be at least 6 characters long.";
        return;
      }
      this.signUpError = "";
      this.registerUser();
    },
    validateSignIn() {
      const {email, password} = this.signInData;
      if (!email || !password) {
        this.signInError = "All fields are required.";
        return;
      }
      if (!this.validateEmail(email)) {
        this.signInError = "Invalid email format.";
        return;
      }
      this.signInError = "";
      this.signInUser();
    },
    validateEmail(email) {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return re.test(email);
    },
    registerUser() {
      const {firstName, lastName, email, password} = this.signUpData;
      const path = "/register-user";
      axiosExtended
          .post(
              path,
              {
                firstName,
                lastName,
                email,
                password,
              }
          )
          .then((response) => {
            if (response.data.success === true) {
              localStorage.setItem("accessToken", response.data.accessToken);

              this.signUpSuccess = true;
              this.$router.push({
                name: "homeApp",
              });
            }
          })
          .catch(() => {
            console.log("Error when creating a new account. Please try again...");
          });
    },
    signInUser() {
      const {email, password} = this.signInData;
      const path = "/sign-in";
      axiosExtended
          .post(
              path,
              {
                email,
                password,
              },
              {withCredentials: true}
          )
          .then((response) => {
            if (response.data.success === true) {
              localStorage.setItem("accessToken", response.data.accessToken);

              this.$router.push({
                name: "homeApp",
              });
            } else {
              this.signInError = response.data.result;
            }
          })
          .catch(() => {
            console.log("Error when signing in. Please try again...");
            this.signInError = "Error during sign-in. Please try again.";
          });
    },
  },
};
</script>

<style scoped>
* { 
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  overflow: hidden !important;
  height: 100%;
  width: 100%;
}


body {
  background-color: #2c64ff;
  background: linear-gradient(to right, #ffffff, #2c64ff);
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  margin: 0;
}

#app {
  height: 100vh; /* Ensure full viewport height */
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.container {
  overflow: hidden !important;
  background-color: #fff;
  border-radius: 30px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.35);
  position: relative;
  width: 768px;
  max-width: 100%;
  min-height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.container p {
  font-size: 14px;
  line-height: 20px;
  letter-spacing: 0.3px;
  margin: 20px 0;
}

.container span {
  font-size: 12px;
}

.container a {
  color: #333;
  font-size: 13px;
  text-decoration: none;
  margin: 15px 0 10px;
}

.container .button {
  background-color: #2c64ff;
  color: #fff;
  font-size: 12px;
  padding: 10px 45px;
  border: 1px solid white;
  border-radius: 8px;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-top: 10px;
  cursor: pointer;
}

.container .button p {
  color: red;
}

.container .button.hidden {
  background-color: transparent;
  border-color: #fff;
}

.container form {
  background-color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 40px;
  height: 100%;
}

.container input {
  background-color: #eee;
  border: none;
  margin: 8px 0;
  padding: 10px 15px;
  font-size: 13px;
  border-radius: 8px;
  width: 100%;
  outline: none;
}

.form-container {
  position: absolute;
  top: 0;
  height: 100%;
  transition: all 0.6s ease-in-out;
}

.sign-in {
  left: 0;
  width: 50%;
  z-index: 2;
}

.sign-in h1 {
  font-size: 30px;
  font-weight: 700;
}

.sign-up h1 {
  font-size: 30px;
  font-weight: 700;
}

.container.active .sign-in {
  transform: translateX(100%);
}

.sign-up {
  left: 0;
  width: 50%;
  opacity: 0;
  z-index: 1;
}

.container.active .sign-up {
  transform: translateX(100%);
  opacity: 1;
  z-index: 5;
  animation: move 0.6s;
}

@keyframes move {
  0%,
  49.99% {
    opacity: 0;
    z-index: 1;
  }
  50%,
  100% {
    opacity: 1;
    z-index: 5;
  }
}

.social-icons {
  margin: 20px 0;
}

.social-icons a {
  border: 1px solid #ccc;
  border-radius: 50%;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  margin: 0 3px;
  width: 40px;
  height: 40px;
}

.toggle-container {
  position: absolute;
  top: 0;
  left: 50%;
  width: 50%;
  height: 100%;
  overflow: hidden;
  transition: all 0.6s ease-in-out;
  border-radius: 150px 0 0 100px;
  z-index: 1000;
}

.container.active .toggle-container {
  transform: translateX(-100%);
  border-radius: 0 150px 100px 0;
}

.toggle {
  background-color: #2c64ff;
  height: 100%;
  background: linear-gradient(to right, #4a7aff, #2c64ff);
  color: #fff;
  position: relative;
  left: -100%;
  height: 100%;
  width: 200%;
  transform: translateX(0);
  transition: all 0.6s ease-in-out;
}

.container.active .toggle {
  transform: translateX(50%);
}

.toggle-panel {
  position: absolute;
  width: 50%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 30px;
  text-align: center;
  top: 0;
  transform: translateX(0);
  transition: all 0.6s ease-in-out;
}

.toggle-left {
  transform: translateX(-200%);
}

.toggle-left h1 {
  font-size: 30px;
  font-weight: 700;
}

.container.active .toggle-left {
  transform: translateX(0);
}

.toggle-right {
  right: 0;
  transform: translateX(0);
}

.toggle-right h1 {
  font-size: 30px;
  font-weight: 700;
}

.toggle-right register {
  background-color: #fff;
}

.container.active .toggle-right {
  transform: translateX(200%);
}

.success-message {
  color: green;
  text-align: center;
  margin-top: 20px;
  font-size: 18px;
  font-weight: bold;
}

.form-container .button + p {
  color: red;
  margin-top: 10px;
  font-size: 14px;
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

@media (max-width: 1024px) and (orientation: landscape) {
  .container {
    width: 55vw; /* Take almost the full width of the viewport */
    max-width: 1100px; /* Allow more space */
    min-height: 380px; /* Reduce height */
    margin: 0  auto;
    padding: 20px;
  }

  .container h1 {
    font-size: 16px;
  }

  .container input {
    font-size: 10px;
    padding: 5px;
  }

  .container .button {
    font-size: 10px;
    padding: 5px 12px;
  }
}

@media (max-width: 768px) and (orientation: landscape) {
  .container {
    width: 50vw; /* Use 90% of the viewport width */
    max-width: 1000px;
    min-height: 90px; /* Reduce height to keep it looking good */
    margin: 0  auto;
    padding: 15px;
  }

  .container h1 {
    font-size: 24px;
  }

  .container input {
    font-size: 14px;
    padding: 8px;
  }

  .container .button {
    font-size: 14px;
    padding: 8px 20px;
  }
}

@media (max-width: 667px) and (orientation: landscape) {
  .container {
    width: 50vw; /* Almost full-screen width */
    max-width: 900px;
    min-height: 90px;
    margin: 0  auto;
    padding: 12px;
  }

  .container h1 {
    font-size: 22px;
  }

  .container input {
    font-size: 13px;
    padding: 7px;
  }

  .container .button {
    font-size: 13px;
    padding: 7px 18px;
  }
}

@media (max-width: 480px) and (orientation: landscape) {
  .container {
    width: 50vw; /* Increase width even more */
    max-width: 850px;
    min-height: 90px;
    margin: 0  auto;
    padding: 10px;
  }

  .container h1 {
    font-size: 20px;
  }

  .container input {
    font-size: 12px;
    padding: 6px;
  }

  .container .button {
    font-size: 12px;
    padding: 6px 16px;
  }
}


/*
@media (max-width: 1366px) and (max-height: 1024px) {
  .container {
    width: 55vw; 
    max-width: 850px;
    min-height: 520px;
    margin: 0 auto;
    margin-bottom: 300px;
    margin-right: 200px;
  }
}

@media (max-width: 1024px) and (max-height: 1366px) {
  .container {
    width: 55vw; 
    max-width: 850px;
    min-height: 470px;
    margin: 0 auto;
    margin-bottom: 600px;
    margin-right: 20px;
  }
}

/*

@media (max-width: 667px) and (max-height: 375px) {
  .container {
    width: 55vw;
    max-width: 850px;
    min-height: 300px;
    margin: 0 auto;
    margin-top: 5px;
    margin-right: 20px;
  }

  .container h1 {
    font-size: 10px;
  }

  .container input {
    font-size: 8px;
    padding: 5px;
  }

  .container .button {
    font-size: 8px;
    padding: 5px 10px;
  }

  .social-icons {
  margin: 10px 0;
}

.social-icons a {
  border: 1px solid #ccc;
  border-radius: 20%;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  margin: 0 3px;
  width: 20px;
  height: 20px;
}

.form-container sign-in a {
  font-size: 3px;
}
}
 */

</style>