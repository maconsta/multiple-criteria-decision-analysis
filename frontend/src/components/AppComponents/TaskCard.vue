<template>
  <div class="card">{{ taskName }}</div>
</template>

<script>
export default {
  name: "TaskCard",
  props: {
    taskName: String,
  },
};
</script>

<style scoped lang="scss">
.card {
  width: 150px;
  height: 150px;
  border-radius: 8px;
  padding: 12px 14px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 500;
  box-shadow: 1px 1px 5px $light-gray;
  position: relative;
  background: transparent;

  &::before {
    position: absolute;
    content: "";
    inset: 0;
    background: rgb(44, 100, 255);
    background: linear-gradient(
      20deg,
      rgba(44, 100, 255, 0.5) 0%,
      rgba(44, 100, 255, 0.1) 50%,
      rgba(255, 255, 255, 1) 100%
    );
    z-index: -1;
    opacity: 0;
    border-radius: 8px;
    transition: opacity 0.3s ease-in-out;
  }

  &:hover::before {
    opacity: 1;
  }
}
</style>
