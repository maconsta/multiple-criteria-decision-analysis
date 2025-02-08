<template>
  <body>
    <div>
      <div class="container" id="container" :class="{ active: isActive }">
        <div class="form-container sign-up">
          <form @submit.prevent="validateSignUp">
            <h1>Create Account</h1>
            <div class="social-icons">
              <a href="#" class="google-icon" aria-label="Google">
                <Icon icon="mdi:google-plus" style="font-size: 20px" />
              </a>
              <a href="#" class="facebook-icon" aria-label="Facebook">
                <Icon icon="fe:facebook" style="font-size: 20px" />
              </a>
              <a href="#" class="git-icon" aria-label="GitHub">
                <Icon icon="mdi:github" style="font-size: 20px" />
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
          <form @submit.prevent="validateSignIn">
            <h1>Sign In</h1>
            <div class="social-icons">
              <a href="#" class="google-icon" aria-label="Google">
                <Icon icon="mdi:google-plus" style="font-size: 20px" />
              </a>
              <a href="#" class="facebook-icon" aria-label="Facebook">
                <Icon icon="fe:facebook" style="font-size: 20px" />
              </a>
              <a href="#" class="git-icon" aria-label="GitHub">
                <Icon icon="mdi:github" style="font-size: 20px" />
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
import { Icon } from "@iconify/vue";
import axios from "axios";
import { redirectToSubdomain } from "@/router";

export default {
  name: "Login",
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
    activateContainer() {
      this.isActive = true;
    },
    deactivateContainer() {
      this.isActive = false;
    },
    validateSignUp() {
      const { firstName, lastName, email, password } = this.signUpData;
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
      const { email, password } = this.signInData;
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
      const { firstName, lastName, email, password } = this.signUpData;
      const path = "register-user";
      axios
        .post(
          path,
          {
            firstName,
            lastName,
            email,
            password,
          },
          { withCredentials: true }
        )
        .then((response) => {
          if (response.data.success === true) {
            localStorage.setItem("csrfToken", response.data.csrfToken);
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
      const { email, password } = this.signInData;
      const path = "sign-in";
      axios
        .post(
          path,
          {
            email,
            password,
          },
          { withCredentials: true }
        )
        .then((response) => {
          if (response.data.success === true) {
            localStorage.setItem("csrfToken", response.data.csrfToken); // Store the token
            this.$router.push({
              name: "homeApp",
            });
          } else {
            this.signInError = response.data.result; // Show the error message if login fails
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
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  width: 100%;
}

.container {
  background-color: #fff;
  border-radius: 30px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.35);
  position: relative;
  overflow: hidden;
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
</style>
