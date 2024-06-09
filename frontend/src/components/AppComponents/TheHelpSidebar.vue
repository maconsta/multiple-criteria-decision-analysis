<template>
  <div class="help-sidebar help-sidebar--open">
    <div class="information mt-15">
      <h2>Help</h2>
      <div class="line mt-10 mb-10"></div>
      <h3 class="mt-20">{{ helpText.heading }}</h3>
      <p class="mt-10">{{ helpText.text }}</p>
    </div>
    <div class="toggle-sidebar-btn help mb-15" @click="toggleSidebar()"></div>
  </div>
</template>

<script>
import { helpText } from "@/store/store";

export default {
  name: "TheHelpSidebar",
  methods: {
    openSidebar() {
      const sidebar = document.getElementsByClassName("help-sidebar")[0];
      sidebar.classList.remove("help-sidebar--closed");
      sidebar.classList.add("help-sidebar--open");

      const information = document.getElementsByClassName("information")[0];
      information.classList.remove("information--inactive");
    },
    closeSidebar() {
      const sidebar = document.getElementsByClassName("help-sidebar")[0];
      sidebar.classList.remove("help-sidebar--open");
      sidebar.classList.add("help-sidebar--closed");

      const information = document.getElementsByClassName("information")[0];
      information.classList.add("information--inactive");
    },
    toggleSidebar() {
      const sidebar = document.getElementsByClassName("help-sidebar")[0];
      if (sidebar.classList.contains("help-sidebar--open")) {
        this.closeSidebar();
      } else {
        this.openSidebar();
      }
    },
  },
  data() {
    return {
      helpText,
    };
  },
};
</script>

<style scoped lang="scss">
.help-sidebar {
  height: 100%;
  padding: 0 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  flex-shrink: 0;
  box-shadow: 2px 6px 10px $charcoal;
  transition: 0.2s ease-in-out;
  overflow: hidden;

  &--open {
    width: 300px;
  }

  &--closed {
    width: 65px;
  }
}

.information {
  width: 100%;

  h2 {
    font-weight: 500;
    font-size: 1.25rem;
    text-align: center;
  }

  h3 {
    font-weight: 400;
    font-style: italic;
  }

  p {
    font-size: 0.875rem;
  }

  &--inactive {
    visibility: hidden;
  }
}

.toggle-sidebar-btn {
  height: 45px;
  width: 45px;
  border-radius: 8px;
  align-self: flex-start;
  transition: 0.2s ease-in-out;
  cursor: pointer;

  &:hover {
    background-color: $main-blue-20;
  }
}
</style>
