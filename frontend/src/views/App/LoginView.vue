<template>
  <div class="signIn">
    <Login />
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
