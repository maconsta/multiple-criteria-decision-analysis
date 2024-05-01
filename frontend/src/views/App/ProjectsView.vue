<template>
  <div class="main">
    <Header />
    <div class="projects">
      <nav class="dashboard">
        <div class="dashboard__top mt-45">
          <h3 class="dashboard__heading">Start a new project</h3>
          <div class="dashboard__icons">
            <div class="chevron chevron--left" @click="handlePrev"></div>
            <div class="chevron chevron--right" @click="handleNext"></div>
          </div>
        </div>
        <div class="dashboard__bot">
          <CardFolder
            @click="openNewProjectModal"
            size="folder--small"
            backgroundColor="folder--gray"
            :havePlus="true"
            :bottomText="{ show: true, text: 'Blank' }"
          />
          <div class="vertical-spacer"></div>
          <swiper-container loop="true" slidesPerView="5" spaceBetween="30">
            <swiper-slide>
              <CardFolder
                size="folder--small"
                backgroundColor="folder--gray"
                :bottomText="{ show: true, text: 'Public Template 1' }"
                :description="{ title: 'World Geography' }"
              />
            </swiper-slide>
            <swiper-slide>
              <CardFolder
                size="folder--small"
                backgroundColor="folder--gray"
                :bottomText="{ show: true, text: 'Public Template 2' }"
                :description="{ title: 'Real Estate' }"
              />
            </swiper-slide>
            <swiper-slide>
              <CardFolder
                size="folder--small"
                backgroundColor="folder--gray"
                :bottomText="{ show: true, text: 'Public Template 3' }"
                :description="{ title: 'Best Economy Vehicle' }"
              />
            </swiper-slide>
            <swiper-slide>
              <CardFolder
                size="folder--small"
                backgroundColor="folder--gray"
                :bottomText="{ show: true, text: 'Public Template 4' }"
                :description="{ title: 'Social Media Marketing' }"
              />
            </swiper-slide>
            <swiper-slide>
              <CardFolder
                size="folder--small"
                backgroundColor="folder--gray"
                :bottomText="{ show: true, text: 'Public Template 5' }"
                :description="{ title: 'New House' }"
              />
            </swiper-slide>
            <swiper-slide>
              <CardFolder
                size="folder--small"
                backgroundColor="folder--gray"
                :bottomText="{ show: true, text: 'Public Template 6' }"
                :description="{ title: 'Popular Trends' }"
              />
            </swiper-slide>
          </swiper-container>
        </div>
      </nav>
      <nav class="dashboard">
        <div class="dashboard__top mt-45">
          <h3 class="dashboard__heading">Recent Projects</h3>
          <div class="dashboard__icons">
            <div class="grid-icon grid-icon--active"></div>
            <div class="list-icon"></div>
          </div>
        </div>
        <div class="dashboard__bot dashboard__bot--wrap">
          <CardFolder
            size="folder--large"
            backgroundColor="folder--darkblue"
            :description="{
              title: 'World Geography',
              more: 'true',
              author: 'Martin Konstantinov',
              visibility: 'public',
            }"
          />
          <CardFolder
            size="folder--large"
            backgroundColor="folder--lightblue"
            :description="{
              title: 'Real Estate',
              more: 'true',
              author: 'John Doe',
              visibility: 'public',
            }"
          />
          <CardFolder
            size="folder--large"
            backgroundColor="folder--green"
            :description="{
              title: 'Social Media',
              more: 'true',
              author: 'Foo Bar',
              visibility: 'public',
            }"
          />
          <CardFolder
            size="folder--large"
            backgroundColor="folder--lightorange"
            :description="{
              title: 'University Location',
              more: 'true',
              author: 'Jane Roe',
              visibility: 'public',
            }"
          />
          <CardFolder
            size="folder--large"
            backgroundColor="folder--yellow"
            :description="{
              title: 'Electric Car Manufacturing',
              more: 'true',
              author: 'Flag Foe',
              visibility: 'public',
            }"
          />
          <CardFolder
            size="folder--large"
            backgroundColor="folder--darkorange"
            :description="{
              title: 'Popular Instagram Profiles',
              more: 'true',
              author: 'Jane Doe',
              visibility: 'public',
            }"
          />
        </div>
      </nav>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import Header from "@/components/Header.vue";
import CardFolder from "@/components/CardFolder.vue";
import { register } from "swiper/element/bundle";
import Swal from "sweetalert2/dist/sweetalert2.all.min.js";
import axios from "axios";

register();

export default {
  name: "ProjectsView",
  components: {
    Header,
    CardFolder,
  },
  methods: {
    handleNext() {
      const swiperElement = document.querySelector("swiper-container");
      swiperElement.swiper.slideNext();
    },
    handlePrev() {
      const swiperElement = document.querySelector("swiper-container");
      swiperElement.swiper.slidePrev();
    },
    saveProjectToDatabase(projectName) {
      const path = "http://127.0.0.1:5000/save-project-to-db";
      const axiosPromise = axios.post(path, {
        name: projectName,
      });

      const router = this.$router;
      axiosPromise
        .then(() => {
          router.push({ name: "projectEdit" });
        })
        .catch(() => {
          console.log("Error when creating a new project. Please try again...");
        });
    },
    openNewProjectModal() {
      const swalPromise = Swal.fire({
        title: "Blank Project",
        input: "text",
        inputLabel: "Enter new project name",
        inputPlaceholder: "Enter name",
        confirmButtonText: "Create",
        confirmButtonAriaLabel: "Create",
        cancelButtonAriaLabel: "Cancel",
        showCancelButton: true,
        customClass: {
          confirmButton: "swal-btn swal-btn__confirm",
          cancelButton: "swal-btn swal-btn__cancel",
          input: "swal-input swal-input__text",
        },
        buttonsStyling: false,
        inputValidator: (value) => {
          if (!value) {
            return "Project name cannot be empty!";
          }
        },
      });

      swalPromise.then((swalResult) => {
        if (swalResult.isConfirmed && swalResult.value) {
          this.saveProjectToDatabase(swalResult.value);
        }
      });
    },
  },
};
</script>

<style lang="scss">
@import url("sweetalert2/dist/sweetalert2.css");

.swal-btn {
  border-radius: 10px;
  padding: 10px;
  color: #fff;

  &__confirm {
    background-color: $main-blue;
  }

  &__cancel {
    background-color: $dark-gray;
  }
}

.swal2-actions {
  gap: 10px;
}

.swal-input {
  &:focus {
    box-shadow: none !important;
    border-color: $main-blue !important;
    outline: 2px solid $main-blue !important;
  }
}

.main {
  display: flex;
  width: 100%;
  flex-direction: column;
  align-items: center;
}

.projects {
  max-width: 1260px;
  width: 100%;
}

.dashboard {
  padding-bottom: 30px;
  border-bottom: 1px solid $light-gray;
  width: 100%;

  &__top {
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  &__bot {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    gap: 20px;
    width: 100%;

    &--wrap {
      flex-wrap: wrap;
    }
  }
}

.vertical-spacer {
  border-left: 1px solid $light-gray;
}

swiper-container {
  width: 100%;
  max-width: 100%;
  max-height: 100vh;
  min-height: 0;
  min-width: 0;
}

.swiper-button-prev,
.swiper-button-next {
  opacity: 0 !important;
}

.dashboard__icons {
  display: flex;
  align-content: center;
  justify-content: space-between;
  gap: 10px;
}

.chevron {
  width: 20px;
  height: 20px;
  background-size: 25px;
  background-position: center;
  background-repeat: no-repeat;
  cursor: pointer;

  &--left {
    background-image: url("../../assets/images/chevron-left.svg");
  }

  &--right {
    background-image: url("../../assets/images/chevron-right.svg");
  }
}

.list-icon {
  width: 20px;
  height: 20px;
  background-size: 25px;
  background-position: center;
  background-repeat: no-repeat;
  background-image: url("../../assets/images/list_inactive.svg");
  cursor: pointer;

  &--active {
    background-image: url("../../assets/images/list_active.svg");
  }
}

.grid-icon {
  width: 20px;
  height: 20px;
  background-size: 20px;
  background-position: center;
  background-repeat: no-repeat;
  background-image: url("../../assets/images/grid_inactive.svg");
  cursor: pointer;

  &--active {
    background-image: url("../../assets/images/grid_active.svg");
  }
}
</style>
