<template>
  <div class="card">
    <div class="card__body">
      <div class="card__name">
        <span class="file-icon file-icon--charcoal"></span>
        <span class="task-name">{{ taskName }}</span>
      </div>
      <span class="trash-icon trash-icon--black" data-folder-action="delete"></span>
      <span class="last-access">Last Opened: 29.10.2024 </span>
    </div>
  </div>
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
  width: 250px;
  height: 200px;
  border-radius: 6px 8px 6px 6px;
  border: 2px solid $light-gray;
  padding: 12px 14px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 500;
  //box-shadow: 1px 1px 5px $light-gray;
  transition: 0.3s ease-in-out;
  position: relative;
  background: transparent;

  &:hover {
    border-color: $dark-gray;
  }

  &__body {
    display: flex;
    justify-content: space-between;
    align-content: space-between;
    flex-wrap: wrap;
    height: 100%;
  }

  &__name {
    display: flex;
    align-items: center;
    column-gap: 5px;
  }

  .task-name {
    padding-top: 1px;
    line-height: 20px;
  }

  .last-access {
    font-weight: 300;
    line-height: 20px;
    font-size: 0.875rem;
  }
}
</style>
