<script>

import TheHeader from "@/components/AppComponents/TheHeader.vue";

export default {
  name: "PageNotFound",
  components: {TheHeader},
}

</script>

<template>
  <div class="main">
    <TheHeader/>
    <h1 class="full-width page-not-found mt-45"></h1>
  </div>
</template>

<style scoped lang="scss">
.page-not-found {
  background-image: linear-gradient(
          rgba(255, 255, 255, 0.5),
          rgba(255, 255, 255, 0.5)
  ),
  url("@/assets/images/page_not_found.png");
  background-size: 300px;
  background-position: center;
  background-repeat: no-repeat;
  height: 340px;
  width: 100%;
  padding: 20px;
  border-radius: 8px;

  display: flex;
  align-items: center;
  justify-content: center;

  font-size: 1.5rem;
  font-weight: 600;
  color: $dark-gray;
}
</style>