<template>
  <div class="signIn">
    <Login />
    <h1>Sign In</h1>
  </div>
</template>

<script>
// @ is an alias to /src

import Login from "@/components/Login.vue";

export default {
  name: "LoginView",
  components: {
    Login,
  },
};
</script>
