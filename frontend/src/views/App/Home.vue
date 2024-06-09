<template>
  <div class="home">
    <TheHeader />
    <h1>Home</h1>
  </div>
</template>

<script>
// @ is an alias to /src
import TheHeader from "@/components/AppComponents/TheHeader.vue";

export default {
  name: "Home",
  components: {
    TheHeader,
  },
};
</script>
