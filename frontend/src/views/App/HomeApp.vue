<template>
  <div class="home">
    <TheHeader />
    <h1 class="full-width empty-placeholder mt-45"></h1>
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

<style scoped lang="scss">
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.empty-placeholder {
  background-image: linear-gradient(
          rgba(255, 255, 255, 0.5),
          rgba(255, 255, 255, 0.5)
  ),
  url("@/assets/images/under-construction-barrier-icon.svg");
  background-size: 300px;
  background-position: center;
  background-repeat: no-repeat;
  height: 340px;
  width: 100%;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 7px $dark-gray;

  display: flex;
  align-items: center;
  justify-content: center;

  font-size: 1.5rem;
  font-weight: 600;
  color: $dark-gray;
}
</style>