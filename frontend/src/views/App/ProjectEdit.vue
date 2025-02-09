<template>
  <div class="main">
    <TheHeader />
    <div class="full-width">
      <div class="navbar mt-45">
        <router-link :to="{ name: 'projects' }" class="back-btn">
          <div class="chevron chevron--left"></div>
          <div class="back-btn__text">Back to projects</div>
        </router-link>
        <div class="btn-container">
          <div class="new-task-btn" @click="openNewProjectModal">
            <div class="plus-icon plus-icon--white"></div>
            <div class="new-task-btn__text">New Task</div>
          </div>
          <div class="share-btn" @click="openShareProjectModal">
            <div class="share-icon share-icon--charcoal"></div>
            <div class="share-btn__text">Share</div>
          </div>
        </div>
      </div>
      <div class="tasks mt-30">
        <div class="project-name" @click="showInputFieldAndHideName()">
          <h3 class="edit">{{ projectName }}</h3>
          <span class="edit-icon edit-icon--charcoal edit"></span>
          <input
            type="text"
            :placeholder="projectName"
            id="change-name"
            class="hidden"
          />
        </div>
        <div v-if="tasks.length === 0" class="tasks__empty-placeholder mt-30">
          You don't have any tasks yet.
        </div>
        <div v-else class="card-container mt-20">
          <TaskCard
            v-for="(task, index) in tasks"
            :key="index"
            :task-name="task.taskName"
            :bottom-text="task.createdAt"
            @click="handleClickOnTask(task.taskID, $event)"
          />
        </div>
      </div>
      <div class="line mt-30"></div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { useRoute } from "vue-router";
import TheHeader from "@/components/AppComponents/TheHeader.vue";
import Swal from "sweetalert2";
import axiosExtended from "@/router/axiosExtended";
import TaskCard from "@/components/AppComponents/TaskCard.vue";

export default defineComponent({
  name: "ProjectEdit",
  components: { TheHeader, TaskCard },
  methods: {
    async fetchProjects() {
      try {
        const response = await axiosExtended.get("/projects");
        this.projects = response.data;
      } catch (error) {
        console.error(
          "Error fetching projects:",
          error.response?.data?.error || error.message
        );
      }
    },
    async openShareProjectModal() {
      Swal.fire({
        title: "Share project",
        input: "email",
        inputLabel: "Add collaborators",
        inputPlaceholder: "Enter email...",
        confirmButtonText: "Invite",
        cancelButtonText: "Close",
        showCancelButton: true,
        buttonsStyling: false,
        customClass: {
          confirmButton: "swal-btn swal-btn__confirm",
          cancelButton: "swal-btn swal-btn__cancel",
          input: "swal-input swal-input__text",
        },
        inputValidator: (value) => {
          if (!value || !value.includes("@")) {
            return "Please enter a valid email address!";
          }
        },
        preConfirm: async (email) => {
          try {
            const response = await axiosExtended.post("/share-project", {
              email: email,
              project_id: this.route.params.projectID,
            });
            Swal.fire("Success", response.data.message, "success");
          } catch (error) {
            Swal.fire(
              "Error",
              error.response?.data?.error || "An unexpected error occurred.",
              "error"
            );
          }
        },
      });
    },
    getProjectName() {
      const route = useRoute();
      axiosExtended
        .get(`/get-project-name-by-id/${route.params.projectID}`)
        .then((response) => {
          this.projectName = response.data;
        })
        .catch(() => {
          console.log("Error when querying a project. Please try again...");
        });
    },
    openNewProjectModal() {
      const swalPromise = Swal.fire({
        title: "New Task",
        input: "text",
        inputLabel: "Enter new Task name",
        inputPlaceholder: "Enter name",
        confirmButtonText: "Create",
        showCancelButton: true,
        buttonsStyling: false,
        customClass: {
          confirmButton: "swal-btn swal-btn__confirm",
          cancelButton: "swal-btn swal-btn__cancel",
          input: "swal-input swal-input__text",
        },
        inputValidator: (value) => {
          if (!value) {
            return "Task name cannot be empty!";
          }
        },
      });

      swalPromise.then((swalResult) => {
        if (swalResult.isConfirmed && swalResult.value) {
          this.saveTaskToDatabase(swalResult.value);
        }
      });
    },
    saveTaskToDatabase(taskName) {
      axiosExtended
        .post("save-task-to-db", {
          name: taskName,
          projectID: this.route.params.projectID,
        })
        .then(() => {
          this.getTasksByProjectID();
        })
        .catch(() => {
          console.log("Error when creating a new task. Please try again...");
        });
    },
    getTasksByProjectID() {
      axiosExtended
        .post("get-tasks-by-project-id", {
          projectID: this.route.params.projectID,
        })
        .then((response) => {
          this.tasks = response.data;
        })
        .catch(() => {
          console.log("Error when querying for all tasks. Please try again...");
        });
    },
    handleClickOnTask(id, event) {
      const attribute = event.target.getAttribute("data-folder-action");
      if (attribute == "delete") {
        this.deleteTask(id);
      } else {
        this.openExistingTask(id);
      }
    },
    deleteTask(id) {
      axiosExtended
        .post("delete-task-by-id", {
          taskID: id,
          projectID: this.route.params.projectID,
        })
        .then(() => {
          this.getTasksByProjectID();
        })
        .catch(() => {
          console.log("Error when deleting project.");
        });
    },
    openExistingTask(id) {
      const router = this.$router;
      router.push({
        name: "taskEditAlternatives",
        params: { taskID: id },
      });
    },
    showInputFieldAndHideName() {
      document.querySelectorAll(".edit").forEach((element) => {
        element.classList.add("hidden");
      });

      const input = document.getElementById("change-name");
      input.classList.remove("hidden");

      input.focus();
    },
    showNameAndHideInputField() {
      document.querySelectorAll(".edit").forEach((element) => {
        element.classList.remove("hidden");
      });

      const input = document.getElementById("change-name");
      input.classList.add("hidden");
    },
    changeProjectName(name) {
      const axiosPromise = axiosExtended.post("change-project-name", {
        name: name,
        projectID: this.route.params.projectID,
      });

      axiosPromise
        .then((response) => {
          this.projectName = name;
        })
        .catch(() => {
          console.log("Error when changing name. Please try again...");
        });
    },
  },
  created() {
    this.getProjectName();
    this.route = useRoute();
    this.getTasksByProjectID();
    this.fetchProjects();
  },
  mounted() {
    const input = document.getElementById("change-name");
    input.addEventListener("focusout", (event) => {
      this.changeProjectName(input.value);
      this.showNameAndHideInputField();
    });

    input.addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        this.changeProjectName(input.value);
        this.showNameAndHideInputField();
      }
    });
  },
  data() {
    return {
      projectName: "",
      route: null,
      tasks: [],
    };
  },
});
</script>

<style scoped lang="scss">
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.back-btn {
  display: flex;
  align-items: center;
  width: fit-content;
  color: #808080;
  filter: grayscale(100%) brightness(50%);

  &:hover {
    color: $dark-gray;
  }

  &__text {
    padding-top: 1px;
    padding-left: 5px;
    cursor: pointer;
    transition: 0.1s ease-in-out;
  }
}

.btn-container {
  display: flex;
  gap: 10px;
}

.new-task-btn {
  display: flex;
  align-items: center;
  gap: 5px;
  background-color: #72bf6a;
  border-radius: 8px;
  width: fit-content;
  padding: 8px 12px 6px;
  cursor: pointer;

  .plus-icon {
    background-size: 24px;
  }

  &__text {
    line-height: 2em;
    color: #fff;
    white-space: nowrap;
  }
}

.share-btn {
  display: flex;
  align-items: center;
  gap: 7px;
  background-color: #fff;
  border: 1px solid #72bf6a;
  border-radius: 8px;
  width: fit-content;
  padding: 8px 12px 6px;
  cursor: pointer;

  .share-icon {
    background-size: 20px;
    width: 20px;
    height: 20px;
  }

  &__text {
    line-height: 2em;
    font-size: 0.875rem;
    font-weight: 600;
    white-space: nowrap;
  }
}

.tasks {
  .project-name {
    display: flex;
    align-items: flex-end;
    column-gap: 5px;
    cursor: pointer;
    width: fit-content;
    height: 25px;

    h3 {
      font-size: 1.25rem;
      line-height: 1.25rem;
      font-weight: 600;
      color: #808080;
    }

    input {
      border: 1px solid $light-gray;
      border-radius: 8px;
      padding: 8px;
      height: 25px;
      font-size: 0.875rem;

      &:focus {
        outline: 2px solid $main-blue-20;
      }
    }
  }

  &__empty-placeholder {
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

  .card-container {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
  }
}
</style>
