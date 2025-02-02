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
          <Flicking
            :options="{
              circular: true,
              align: 'prev',
              circularFallback: 'bound',
            }"
            ref="flicking"
          >
            <CardFolder
              size="folder--small"
              background-color="folder--gray"
              :show-description="true"
              project-name="World Geography"
              :bottomText="{ show: true, text: 'Public Template 1' }"
              :key="0"
            />
            <CardFolder
              size="folder--small"
              background-color="folder--gray"
              :show-description="true"
              project-name="Real Estate"
              :bottomText="{ show: true, text: 'Public Template 2' }"
              :key="1"
            />
            <CardFolder
              size="folder--small"
              background-color="folder--gray"
              :show-description="true"
              project-name="Best Economy Vehicle"
              :bottomText="{ show: true, text: 'Public Template 3' }"
              :key="2"
            />
            <CardFolder
              size="folder--small"
              background-color="folder--gray"
              :show-description="true"
              project-name="Social Media Marketing"
              :bottomText="{ show: true, text: 'Public Template 4' }"
              :key="3"
            />
            <CardFolder
              size="folder--small"
              background-color="folder--gray"
              :show-description="true"
              project-name="New House"
              :bottomText="{ show: true, text: 'Public Template 5' }"
              :key="4"
            />
            <CardFolder
              size="folder--small"
              background-color="folder--gray"
              :show-description="true"
              project-name="Popular Trends"
              :bottomText="{ show: true, text: 'Public Template 6' }"
              :key="5"
            />
            <CardFolder
              size="folder--small"
              background-color="folder--gray"
              :show-description="true"
              project-name="Lorem Ipsum"
              :bottomText="{ show: true, text: 'Public Template 7' }"
              :key="6"
            />
          </Flicking>
        </div>
      </nav>
      <nav class="dashboard">
        <div class="dashboard__top mt-45">
          <h3 class="dashboard__heading">All Projects</h3>
          <div class="dashboard__icons">
            <div
              class="grid-icon grid-icon--active"
              @click="changeDashboardMode('grid')"
            ></div>
            <div class="list-icon" @click="changeDashboardMode('list')"></div>
          </div>
        </div>
        <div class="dashboard__bot dashboard__bot--wrap">
          <div v-if="projects.length === 0" class="empty-placeholder">
            You don't have any projects.
          </div>
          <CardFolder
            v-else-if="dashboardMode === 'grid'"
            v-for="(project, index) in projects"
            :key="index"
            size="folder--large"
            background-color="folder--yellow"
            :show-description="true"
            :project-name="project.projectName"
            :trash="true"
            :owner="project.owner"
            :visibility="project.visibility"
            @click="handleClickOnFolder(project.projectID, $event)"
          />
          <table
            v-else-if="dashboardMode === 'list'"
            class="data-table"
            ref="dataTable"
          >
            <thead>
              <tr>
                <th>Project</th>
                <th>Owner</th>
                <th>Delete</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(project, index) in projects" :key="index">
                <td @click="handleClickOnFolder(project.projectID, $event)">
                  {{ project.projectName }}
                </td>
                <td>{{ project.owner }}</td>
                <td class="align-right">
                  <span
                    class="trash-icon trash-icon--black"
                    data-folder-action="delete"
                    @click="handleClickOnFolder(project.projectID, $event)"
                  ></span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </nav>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import TheHeader from "@/components/AppComponents/TheHeader.vue";
import CardFolder from "@/components/AppComponents/CardFolder.vue";
import Swal from "sweetalert2/dist/sweetalert2.all.min.js";
import axiosExtended from "@/router/axiosExtended";
import Flicking from "@egjs/vue3-flicking";
import DataTable from "datatables.net/js/dataTables";
import "datatables.net-dt/css/dataTables.dataTables.css";

export default {
  name: "Projects",
  components: {
    TheHeader,
    CardFolder,
    Flicking: Flicking,
  },
  methods: {
    handlePrev() {
      this.$refs.flicking.prev().catch(() => void 0);
    },
    handleNext() {
      this.$refs.flicking.next().catch(() => void 0);
    },
    saveProjectToDatabase(projectName) {
      const axiosPromise = axiosExtended.post("save-project-to-db", {
        name: projectName,
      });

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
      const axiosPromise = axiosExtended.get("get-projects-by-user-id");

      axiosPromise
        .then((response) => {
          for (const project of response.data) {
            if (project.owner.length > 20) {
              const splitString = project.owner.split(" ");
              project.owner = splitString[0][0] + ". " + splitString[1];
            }

            if (project.owner.length > 20) {
              const splitString = project.owner.split(" ");
              project.owner = splitString[0] + splitString[1][0] + ".";
            }
          }
          this.projects = response.data;

          if (this.dataTable) {
            this.dataTable.destroy();
          }

          this.$nextTick(() => {
            this.createDataTable();
          });
        })
        .catch(() => {
          console.log(
            "Error when querying for all projects. Please try again..."
          );
        });
    },
    handleClickOnFolder(id, event) {
      const attribute = event.target.getAttribute("data-folder-action");
      if (attribute == "delete") {
        this.deleteProject(id);
      } else {
        this.openExistingProject(id);
      }
    },
    deleteProject(id) {
      const axiosPromise = axiosExtended.post("delete-project-by-id", {
        projectID: id,
      });

      axiosPromise
        .then((response) => {
          this.getAllProjects();
        })
        .catch((response) => {
          console.log("Error when deleting project.");
        });
    },
    openExistingProject(id) {
      const router = this.$router;
      router.push({
        name: "projectEdit",
        params: { projectID: id },
      });
    },
    createDataTable() {
      this.dataTable = new DataTable(this.$refs.dataTable, this.tableOptions);
    },
    changeDashboardMode(mode) {
      if (this.dashboardMode === mode) {
        return;
      }

      localStorage.setItem("dashboardMode", mode);
      this.dashboardMode = mode;

      if (this.dataTable) {
        this.dataTable.destroy();
      }

      if (mode === "list") {
        this.$nextTick(() => {
          this.createDataTable();
        });
      }
    },
  },
  mounted() {
    this.getAllProjects();

    // set default dashboard mode to grid
    let mode = localStorage.getItem("dashboardMode");
    if (mode) {
      this.dashboardMode = mode;
    } else {
      this.dashboardMode = "grid";
    }
  },
  data() {
    return {
      projects: [],
      dashboardMode: null,
      dataTable: null,
      tableOptions: {
        paging: false,
        searching: false,
        ordering: true,
        responsive: true,
        info: false,
        destroy: true,
        columnDefs: [
          { targets: [0, 1], width: "40%" },
          { targets: 2, orderable: false, width: "20%" },
        ],
      },
    };
  },
};
</script>

<style lang="scss">
@import url("sweetalert2/dist/sweetalert2.css");
@import url("@egjs/vue3-flicking/dist/flicking.css");

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

    @media screen and (max-width: 660px) {
      justify-content: center;
    }
  }
}

.vertical-spacer {
  border-left: 1px solid $light-gray;
}

.flicking-camera {
  .folder-wrapper {
    margin-right: 15px;
  }
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

.dashboard__heading {
  color: #596380;
}

.dashboard__icons {
  filter: invert(31%) sepia(9%) saturate(303%) hue-rotate(177deg)
    brightness(93%) contrast(91%);
}

.dt-container {
  width: 100%;
}

.data-table {
  thead {
    th {
      color: #596389;
      font-size: 1.3rem;

      &:last-child {
        text-align: right;
      }
    }
  }

  tbody {
    td {
      color: #596389;
      vertical-align: middle;

      &:first-child {
        cursor: pointer;

        &:hover {
          text-decoration: underline;
        }
      }

      &:last-child {
        span {
          cursor: pointer;
        }
      }
    }

    tr {
      &:hover {
        background-color: $folder-yellow;
      }
    }
  }
}
</style>
