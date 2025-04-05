<template>
  <div class="w-100 mt-30 pb-20" id="loader-container">
    <div class="topbar w-100">
      <h2>Alternatives</h2>
      <div class="btn-container">
        <div
            class="add-alternative-btn"
            @click="addNewAlternative"
            role="button"
        >
          <div class="plus-icon plus-icon--white"></div>
          <div class="add-alternative-btn__text">Add Alternative</div>
        </div>
        <div
            class="delete-alternatives-btn"
            @click="deleteSelectedAlternatives"
            role="button"
        >
          <div class="trash-icon trash-icon--white"></div>
          <div class="delete-alternatives-btn__text">Delete</div>
        </div>
      </div>
    </div>
    <div class="alternatives mt-30">
      <div
          v-for="(alternative, index) in alternatives"
          class="alternative"
          :key="index"
          @click="toggleAlternative"
          :data-alternative-id="alternative.alternativeID"
      >
        <span class="checkbox"></span>
        <span class="text">{{ alternative.name }}</span>
        <!--        suppress VueUnrecognizedDirective-->
        <span
            class="help"
            v-tooltip="{
            content: '<b>Description</b>: ' + alternative.description,
            html: true,
          }"
          @click="showTooltip($event, alternative.description)"
        ></span>
      </div>
    </div>
  </div>
</template>

<script>
import axiosExtended from "@/router/axiosExtended";
import {useRoute} from "vue-router";
import Swal from "sweetalert2";

export default {
  name: "TaskEditAlternatives",
  methods: {
    addNewAlternative() {
      this.$router.push({
        name: "taskEditNewAlternative",
      });
    },
    showTooltip(event, description) {
      event.stopPropagation(); // Prevents checkbox selection

      if (this.isTouchDevice()) {
        Swal.fire({
          title: "Description",
          html: `<b>Description</b>: ${description}`,
          icon: "info",
          confirmButtonText: "OK",
        });
      }
    },
    isTouchDevice() {
      return "ontouchstart" in window || navigator.maxTouchPoints > 0;
    },
    getAlternativesByTaskID() {
      let loader = this.$loading.show({
        container: document.getElementById("loader-container"),
      });
      const axiosPromise = axiosExtended.post("/get-alternatives-by-task-id", {
        taskID: this.route.params.taskID,
        projectID: this.route.params.projectID,
      });

      axiosPromise
          .then((response) => {
            this.alternatives = response.data;
          })
          .catch(() => {
            console.log(
                "Error when querying for alternatives. Please try again..."
            );
          })
          .finally(() => {
            loader.hide();
          });
    },
    deselectAllAlternatives() {
      const checkboxes = document.getElementsByClassName("checkbox");
      const alts = document.getElementsByClassName("alternative");

      for (const alt of alts) {
        alt.dataset.seleted = "false";
      }

      for (const checkbox of checkboxes) {
        checkbox.classList.remove("checkbox--selected");
      }

      this.numberOfSelectedAlternatives = 0;
    },
    toggleAlternative(event) {
      const checkbox = event.currentTarget.querySelector(".checkbox");
      checkbox.classList.toggle("checkbox--selected");

      if (checkbox.classList.contains("checkbox--selected")) {
        event.currentTarget.dataset.selected = "true";
        this.numberOfSelectedAlternatives++;
      } else {
        event.currentTarget.dataset.selected = "false";
        this.numberOfSelectedAlternatives--;
      }

      this.updateDeleteButtonVisibility();
      // Todo: add help text to the help panel (description from the DB/criterion)
    },
    updateDeleteButtonVisibility() {
      const deleteButton = document.querySelector(".delete-alternatives-btn");
      if (this.numberOfSelectedAlternatives > 0) {
        deleteButton.classList.add("delete-alternatives-btn--active");
      } else {
        deleteButton.classList.remove("delete-alternatives-btn--active");
      }
    },
    deleteSelectedAlternatives() {
      if (this.numberOfSelectedAlternatives === 0) {
        return;
      }

      const alternatives = document.querySelectorAll(".alternative");
      let selectedAlternativesIDs = [];

      for (const alt of alternatives) {
        if (alt.dataset.selected === "true") {
          selectedAlternativesIDs.push(parseInt(alt.dataset.alternativeId));
        }
      }

      const axiosPromise = axiosExtended.post("/delete-alternatives-by-id", {
        alternativesIDs: selectedAlternativesIDs,
        taskID: this.route.params.taskID,
      });

      axiosPromise
          .then(() => {
            Swal.fire({
              position: "top-end",
              toast: true,
              icon: "success",
              title: "Alternatives have been deleted",
              showConfirmButton: false,
              timer: 3000,
            });

            this.alternatives = this.alternatives.filter(
                (alt) => !selectedAlternativesIDs.includes(alt.alternativeID)
            );

            this.deselectAllAlternatives();
          })
          .catch(() => {
            console.log("Error when deleting alternatives. Please try again...");
          });
    },
  },
  created() {
    this.route = useRoute();
  },
  mounted() {
    this.getAlternativesByTaskID();
  },
  data() {
    return {
      alternatives: [],
      route: null,
      numberOfSelectedAlternatives: 0,
    };
  },
};
</script>

<style scoped lang="scss">
.topbar {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;

  h2 {
    font-weight: 600;
    font-size: 1.25rem;
  }

  @media screen and (max-width: 440px) {
    flex-direction: column;
    align-items: center;
    row-gap: 10px;
  }
}

.btn-container {
  display: flex;
  gap: 10px;
}

.add-alternative-btn {
  display: flex;
  align-items: center;
  gap: 5px;
  background-color: $plant-green;
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

  @media screen and (max-width: 700px) {
    &__text {
      display: none;
    }
  }
}

.delete-alternatives-btn {
  display: flex;
  align-items: center;
  gap: 5px;
  background-color: $gray;
  border-radius: 8px;
  width: fit-content;
  padding: 8px 12px 6px;
  cursor: not-allowed;
  min-width: 54px;

  .plus-icon {
    background-size: 24px;
  }

  &--active {
    cursor: pointer;
    background-color: $dark-gray;
  }

  &__text {
    line-height: 2em;
    color: #fff;
    white-space: nowrap;
  }

  @media screen and (max-width: 700px) {
    justify-content: center;

    &__text {
      display: none;
    }
  }
}

.alternatives {
  display: flex;
  flex-direction: column;
  row-gap: 10px;
}

.alternative {
  width: 100%;
  height: 60px;
  border: 1px solid $light-gray;
  border-radius: 8px;
  padding: 20px 16px;
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 10px;
  cursor: pointer;
  transition: 0.2s ease-in-out;

  .checkbox {
    height: 20px;
    width: 20px;
    background-image: url("@/assets/images/square.svg");
    background-position: center;
    background-repeat: no-repeat;
    background-size: 17px;

    &--selected {
      background-image: url("@/assets/images/check-square.svg");
    }
  }

  .text {
    align-self: center;
    flex: 1;
    font-weight: 500;
    font-size: 15px;
  }

  &:hover {
    border-color: $main-blue-20;
    //background-color: $main-blue-20;
  }

  //&--open {
  //  height: auto;
  //
  //  table {
  //    display: table;
  //  }
  //}
}
</style>
