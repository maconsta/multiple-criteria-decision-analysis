<template>
  <div class="home">
    <TheHeader />
    <h1 @click="callTestApi">Home</h1>
  </div>
</template>

<script>
// @ is an alias to /src
import TheHeader from "@/components/AppComponents/TheHeader.vue";
import axiosExtended from "@/router/axiosExtended";

export default {
  name: "HomeApp",
  components: {
    TheHeader,
  },
  methods: {
    callTestApi() {
      const axiosPromise = axiosExtended.post("test-api", {});

      axiosPromise.then((result) => {
        console.log(result);
      });
    },
  },
};
</script>
