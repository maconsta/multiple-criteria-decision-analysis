<template>
  <router-link :to="{ name: routeName }" class="sidebar-btn">
    <img :src="require('@/assets/images/' + imageUrl)">
    <span>{{ buttonText }}</span>
  </router-link>
</template>

<script>
export default {
  name: "SidebarButton",
  props: {
    routeName: String,
    buttonText: String,
    imageUrl: String
  },
};
</script>

<style scoped lang="scss">
.sidebar-btn {
  padding: 10px 12px;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.875rem;
  display: flex;
  align-items: center;
  column-gap: 5px;
  height: 45px;

  &--small {
    width: 45px;
    height: 45px;
    justify-content: center;

    span {
      display: none;
    }
  }

  &:hover {
    background-color: $main-blue-20;
  }

  &.router-link-exact-active {
    color: $main-blue;
  }
}

</style>
