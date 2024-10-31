<template>
  <div class="sidebar sidebar--open">
    <div class="sidebar-btn-container mt-15">
<!--      <SidebarButton-->
<!--        image-url="monitor.svg"-->
<!--        route-name="taskEditOverview"-->
<!--        button-text="Overview"-->
<!--        @click="openSidebar"-->
<!--      />-->
<!--      <div class="line mt-10 mb-10"></div>-->
      <SidebarButton
        image-url="square.svg"
        route-name="taskEditAlternatives"
        button-text="Alternatives"
        @click="openSidebar"
      />
      <SidebarButton
        image-url="circle.svg"
        route-name="taskEditCriteria"
        button-text="Criteria"
        @click="openSidebar"
      />
      <SidebarButton
        image-url="triangle.svg"
        route-name="taskEditMethod"
        button-text="Method"
        @click="openSidebar"
      />
      <div class="line mt-10 mb-10"></div>
      <SidebarButton
        image-url="scale2.png"
        route-name="taskEditWeights"
        button-text="Weigh & Calculate"
        @click="openSidebar"
      />
<!--      <div class="line mt-10 mb-10"></div>-->
<!--      <SidebarButton-->
<!--        image-url="cpu.svg"-->
<!--        route-name="taskEditCalculate"-->
<!--        button-text="Calculate"-->
<!--        @click="openSidebar"-->
<!--      />-->
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
};
</script>

<style scoped lang="scss">
.sidebar {
  height: 100%;
  padding: 0 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-shrink: 0;
  box-shadow: -2px 6px 10px $charcoal;
  transition: 0.2s ease-in-out;
  overflow: hidden;

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

  &:hover {
    background-color: $main-blue-20;
  }
}
</style>
