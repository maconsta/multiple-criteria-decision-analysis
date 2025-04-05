<template>
  <div class="w-100 mt-30 pb-20" id="loader-container">
    <div class="topbar w-100">
      <h2>Criteria</h2>
      <div class="btn-container">
        <div class="add-criteria-btn" @click="addNewCriterion" role="button">
          <div class="plus-icon plus-icon--white"></div>
          <div class="add-criteria-btn__text">Add Criterion</div>
        </div>
        <div
            class="delete-criteria-btn"
            @click="deleteSelectedCriteria"
            role="button"
        >
          <div class="trash-icon trash-icon--white"></div>
          <div class="add-criteria-btn__text">Delete</div>
        </div>
        <div
            class="edit-criterion-btn"
            @click="editCriterion"
            role="button"
        >
          <span class="edit-icon edit-icon--white edit"></span>
          <div class="edit-criterion-btn__text">Edit</div>
        </div>
      </div>
    </div>
    <div class="criteria mt-30">
      <div
          v-for="(criterion, index) in criteria"
          class="criterion"
          :key="index"
          @click="selectCriterion"
          :data-criterion-id="criterion.criterionID"
      >
        <span class="checkbox"></span>
        <span class="text">{{ criterion.name }}</span>
        <!--suppress VueUnrecognizedDirective -->
        <span
            class="help"
            v-tooltip="{
            content:
              '<b>Description</b>: ' +
              criterion.description +
              '</br><b>Beneficiality</b>: ' +
              criterion.beneficiality,
            html: true,
          }"
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
  name: "TaskEditCriteria",
  methods: {
    addNewCriterion() {
      this.$router.push({
        name: "taskEditNewCriterion",
      });
    },
    editCriterion() {
      if (this.numberOfSelectedCrit === 1) {
        const criterionID = document.querySelector(".criterion[data-selected='true']").dataset.criterionId;
        this.$router.push({
          name: "taskEditNewCriterion",
          params: {criterionID: criterionID},
        });
      }
    },
    getCriteriaByTaskID() {
      let loader = this.$loading.show({
        container: document.getElementById("loader-container"),
      });

      const axiosPromise = axiosExtended.post("/get-criteria-by-task-id", {
        taskID: this.route.params.taskID,
      });

      axiosPromise
          .then((response) => {
            this.criteria = response.data;
            for (const crit of this.criteria) {
              crit.beneficiality =
                  crit.beneficiality === "max" ? "Beneficial" : "Non-beneficial";
            }
          })
          .catch(() => {
            console.log("Error when querying for criteria. Please try again...");
          })
          .finally(() => {
            loader.hide();
          });
    },
    selectCriterion(event) {
      const checkbox = event.currentTarget.querySelector(".checkbox");
      checkbox.classList.toggle("checkbox--selected");

      if (checkbox.classList.contains("checkbox--selected")) {
        event.currentTarget.dataset.selected = "true";
        this.numberOfSelectedCrit++;
      } else {
        event.currentTarget.dataset.selected = "false";
        this.numberOfSelectedCrit--;
      }

      this.updateDeleteButtonVisibility();
      this.updateEditButtonVisibility();

      // helpText.text = "Test Criteria";

      // Todo: add help text to the help panel (description from the DB/criterion)
    },
    updateDeleteButtonVisibility() {
      const deleteButton = document.querySelector(".delete-criteria-btn");
      if (this.numberOfSelectedCrit > 0) {
        deleteButton.classList.add("delete-criteria-btn--active");
      } else {
        deleteButton.classList.remove("delete-criteria-btn--active");
      }
    },
    updateEditButtonVisibility() {
      const editButton = document.querySelector(".edit-criterion-btn");
      if (this.numberOfSelectedCrit === 1) {
        editButton.classList.add("edit-criterion-btn--active");
      } else {
        editButton.classList.remove("edit-criterion-btn--active");
      }
    },
    deleteSelectedCriteria() {
      if (this.numberOfSelectedCrit === 0) {
        return;
      }

      const criteria = document.querySelectorAll(".criterion");
      let selectedCriteriaIDs = [];

      for (const crit of criteria) {
        if (crit.dataset.selected === "true") {
          selectedCriteriaIDs.push(parseInt(crit.dataset.criterionId));
        }
      }

      const axiosPromise = axiosExtended.post("/delete-criteria-by-id", {
        criteriaIDs: selectedCriteriaIDs,
        taskID: this.route.params.taskID,
      });

      axiosPromise
          .then(() => {
            Swal.fire({
              position: "top-end",
              toast: true,
              icon: "success",
              title: "Criteria have been deleted",
              showConfirmButton: false,
              timer: 3000,
            });

            this.criteria = this.criteria.filter(
                (crit) => !selectedCriteriaIDs.includes(crit.criterionID)
            );

            this.deselectAllCriteria();
          })
          .catch(() => {
            console.log("Error when deleting criteria. Please try again...");
          });

      this.numberOfSelectedCrit--;
      this.updateDeleteButtonVisibility();
      this.updateEditButtonVisibility();
    },
    deselectAllCriteria() {
      const checkboxes = document.getElementsByClassName("checkbox");
      const criteria = document.getElementsByClassName("criterion");

      for (const crit of criteria) {
        crit.dataset.seleted = "false";
      }

      for (const checkbox of checkboxes) {
        checkbox.classList.remove("checkbox--selected");
      }

      this.numberOfSelectedCrit = 0;
    },
  },
  created() {
    this.route = useRoute();
  },
  mounted() {
    this.getCriteriaByTaskID();
  },
  data() {
    return {
      criteria: [],
      route: null,
      numberOfSelectedCrit: 0,
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

.add-criteria-btn {
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

.delete-criteria-btn {
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
  }
}

.criteria {
  display: flex;
  flex-direction: column;
  row-gap: 10px;
}

.criterion {
  width: 100%;
  height: 60px;
  border: 1px solid $light-gray;
  border-radius: 8px;
  padding: 8px 16px 8px 8px;
  display: flex;
  align-items: center;
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
    background-color: $main-blue-20;
  }
}

.edit-criterion-btn {
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
  }
}
</style>
