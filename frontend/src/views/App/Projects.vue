<template>
  <div class="main">
    <TheHeader />
    <div class="full-width">
      <nav class="dashboard mt-45">
        <div class="dashboard__top">
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
            background-color="folder--gray"
            :have-plus="true"
            :bottom-text="{ show: true, text: 'Blank' }"
          />
          <div class="vertical-spacer"></div>
          <swiper-container loop="true" slidesPerView="5" spaceBetween="30">
            <swiper-slide>
              <CardFolder
                size="folder--small"
                background-color="folder--gray"
                :show-description="true"
                project-name="World Geography"
                :bottomText="{ show: true, text: 'Public Template 1' }"
              />
            </swiper-slide>
            <swiper-slide>
              <CardFolder
                size="folder--small"
                background-color="folder--gray"
                :show-description="true"
                project-name="Real Estate"
                :bottomText="{ show: true, text: 'Public Template 2' }"
              />
            </swiper-slide>
            <swiper-slide>
              <CardFolder
                size="folder--small"
                background-color="folder--gray"
                :show-description="true"
                project-name="Best Economy Vehicle"
                :bottomText="{ show: true, text: 'Public Template 3' }"
              />
            </swiper-slide>
            <swiper-slide>
              <CardFolder
                size="folder--small"
                background-color="folder--gray"
                :show-description="true"
                project-name="Social Media Marketing"
                :bottomText="{ show: true, text: 'Public Template 4' }"
              />
            </swiper-slide>
            <swiper-slide>
              <CardFolder
                size="folder--small"
                background-color="folder--gray"
                :show-description="true"
                project-name="New House"
                :bottomText="{ show: true, text: 'Public Template 5' }"
              />
            </swiper-slide>
            <swiper-slide>
              <CardFolder
                size="folder--small"
                background-color="folder--gray"
                :show-description="true"
                project-name="Popular Trends"
                :bottomText="{ show: true, text: 'Public Template 6' }"
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
          <div v-if="projects.length === 0" class="empty-placeholder">
            You don't have any projects.
          </div>
          <CardFolder
            v-for="(project, index) in projects"
            :key="index"
            size="folder--large"
            background-color="folder--yellow"
            :show-description="true"
            :project-name="project.projectName"
            :more="true"
            :owner="project.owner"
            :visibility="project.visibility"
            @click="openExistingProject(project.projectID)"
          />
        </div>
      </nav>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import TheHeader from "@/components/AppComponents/TheHeader.vue";
import CardFolder from "@/components/AppComponents/CardFolder.vue";
import { register } from "swiper/element/bundle";
import Swal from "sweetalert2/dist/sweetalert2.all.min.js";
import axios from "axios";

export default {
  name: "Projects",
  components: {
    TheHeader,
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
      // TODO: Change to a dynamic url to switch between prod/local

      const path = "http://127.0.0.1:5000/save-project-to-db";
      const axiosPromise = axios.post(
        path,
        {
          name: projectName,
        },
        {
          withCredentials: true,
          withXSRFToken: true,
        }
      );

      const router = this.$router;
      axiosPromise
        .then((response) => {
          router.push({
            name: "projectEdit",
            params: { projectID: response.data.projectID },
          });
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
    getAllProjects() {
      const path = "http://127.0.0.1:5000/get-all-projects";
      const axiosPromise = axios.get(path);

      axiosPromise
        .then((response) => {
          this.projects = response.data;
        })
        .catch(() => {
          console.log(
            "Error when querying for all projects. Please try again..."
          );
        });
    },
    openExistingProject(id) {
      const router = this.$router;
      router.push({
        name: "projectEdit",
        params: { projectID: id },
      });
    },
  },
  created() {
    register();
    this.getAllProjects();
  },
  data() {
    return {
      projects: [],
    };
  },
};
</script>

<style lang="scss">
@import url("sweetalert2/dist/sweetalert2.css");

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

.empty-placeholder {
  background-image: linear-gradient(
      rgba(255, 255, 255, 0.5),
      rgba(255, 255, 255, 0.5)
    ),
    url(http://app.localhost:8080/img/about.1f15f248.png);
  background-size: 300px;
  background-position: center right 20px;
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
