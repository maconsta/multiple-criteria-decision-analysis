<template>
  <div class="main">
    <TheHeader />
    <div class="sideways">
      <TheSidebar />
      <router-view></router-view>
      <TheHelpSidebar />
    </div>
  </div>
</template>

<script>
import TheHeader from "@/components/AppComponents/TheHeader.vue";
import TheSidebar from "@/components/AppComponents/TheSidebar.vue";
import TheHelpSidebar from "@/components/AppComponents/TheHelpSidebar.vue";

export default {
  name: "TaskEdit",
  components: {
    TheHelpSidebar,
    TheSidebar,
    TheHeader,
  },
};
</script>

<style scoped lang="scss">
.sideways {
  display: flex;
  flex-direction: row;
  column-gap: 35px;
  width: 100%;
  height: 100%;
}
</style>
