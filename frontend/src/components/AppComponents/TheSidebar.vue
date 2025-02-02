<template>
  <div class="sidebar sidebar--open">
    <div class="sidebar-btn-container mt-15">
      <SidebarButton
        :image-url="alt_image"
        route-name="taskEditAlternatives"
        button-text="Alternatives"
        @click="openSidebar"
      />
      <SidebarButton
        :image-url="crit_image"
        route-name="taskEditCriteria"
        button-text="Criteria"
        @click="openSidebar"
      />
      <SidebarButton
        :image-url="trade_offs_image"
        route-name="taskEditTradeOffs"
        button-text="Trade-Offs"
        @click="openSidebar"
      />
      <div class="line mt-10 mb-10"></div>
      <SidebarButton
        image-url="cpu.svg"
        route-name="result"
        button-text="Calculate"
        @click="openSidebar"
      />
    </div>

    <div
      class="toggle-sidebar-btn chevron chevron--left mb-15"
      @click="toggleSidebar"
    ></div>
  </div>
</template>

<script>
import SidebarButton from "@/components/AppComponents/SidebarButton.vue";

export default {
  name: "TheSidebar",
  components: {
    SidebarButton,
  },
  methods: {
    openSidebar() {
      const sidebar = document.getElementsByClassName("sidebar")[0];
      sidebar.classList.remove("sidebar--closed");
      sidebar.classList.add("sidebar--open");

      const buttons = document.getElementsByClassName("sidebar-btn");
      for (const button of buttons) {
        button.classList.remove("sidebar-btn--small");
      }

      const chevron = document.getElementsByClassName("chevron")[0];
      chevron.classList.add("chevron--left");
      chevron.classList.remove("chevron--right");
    },
    closeSidebar() {
      const sidebar = document.getElementsByClassName("sidebar")[0];
      sidebar.classList.remove("sidebar--open");
      sidebar.classList.add("sidebar--closed");

      const buttons = document.getElementsByClassName("sidebar-btn");
      for (const button of buttons) {
        button.classList.add("sidebar-btn--small");
      }

      const chevron = document.getElementsByClassName("chevron")[0];
      chevron.classList.add("chevron--right");
      chevron.classList.remove("chevron--left");
    },
    toggleSidebar() {
      const sidebar = document.getElementsByClassName("sidebar")[0];
      if (sidebar.classList.contains("sidebar--open")) {
        this.closeSidebar();
      } else {
        this.openSidebar();
      }
    },
  },
  data() {
    return {
      alt_image: "square.svg",
      crit_image: "square.svg",
      trade_offs_image: "square.svg",
    };
  },
};
</script>

<style scoped lang="scss">
.sidebar {
  min-height: calc(100vh - 75px);
  padding: 0 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-shrink: 0;
  box-shadow: -2px 6px 10px $charcoal;
  transition: 0.2s ease-in-out;
  overflow: hidden;
  position: relative;

  &--open {
    width: 220px;
  }

  &--closed {
    width: 65px;
  }
}

.sidebar-btn-container {
  display: flex;
  flex-direction: column;
}

.toggle-sidebar-btn {
  height: 45px;
  width: 45px;
  border-radius: 8px;
  align-self: flex-end;
  transition: 0.2s ease-in-out;
  position: fixed;
  bottom: 0;

  &:hover {
    background-color: $main-blue-20;
  }
}
</style>
