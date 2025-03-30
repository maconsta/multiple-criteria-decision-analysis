<script>
import axiosExtended from "@/router/axiosExtended";
import {useRoute} from "vue-router";
import Swal from "sweetalert2";

export default {
  name: "TaskEditMethod",
  created() {
    this.route = useRoute();
    this.getTradeOffByTaskId();
  },
  data() {
    return {
      route: null,
    };
  },
  methods: {
    getTradeOffByTaskId() {
      const axiosPromise = axiosExtended.post("/get-trade-off-by-task-id", {
        taskID: this.route.params.taskID,
      });

      axiosPromise
          .then((response) => {
            document.getElementById("decision-method").value = response.data.decisionMethod;
            document.getElementById("normalization-method").value = response.data.normalizationMethod;
          })
          .catch(() => {
          });
    },
    handleDropdownChange() {
      const decisionMethod = document.getElementById("decision-method").value;
      const normalizationMethod = document.getElementById("normalization-method").value;
      const taskID = this.route.params.taskID;

      const axiosPromise = axiosExtended.post("/save-method-to-db", {
        decisionMethod: decisionMethod,
        normalizationMethod: normalizationMethod,
        taskID: taskID,
      });

      const router = this.$router;
      axiosPromise
          .then((result) => {
            Swal.fire({
              position: "top-end",
              toast: true,
              icon: "success",
              title: "Method has been saved",
              showConfirmButton: false,
              timer: 3000,
            });
          })
          .catch(() => {
            console.log(
                "Error when creating a new trade-off. Please try again..."
            );
          });
    }
  },
};
</script>

<template>
  <div class="w-100 mt-30">
    <div class="topbar w-100">
      <h2>Decision Method</h2>
    </div>
    <div class="methods mt-30">
      <label for="decision-method">Decision Methods (Required)</label>
      <select
          id="decision-method"
          name="decision-method"
          class="methods__dropdown"
          @change="handleDropdownChange"
      >
        <option value="topsis">Topsis</option>
        <option value="ahp">AHP</option>
        <option value="electre">Electre</option>
        <option value="wsm">Weighted Sum</option>
        <option value="prometheeii">PROMETHEE II</option>
      </select>
      <label for="normalization-method" class="mt-15"
      >Normalization Method (Required)</label
      >
      <select
          id="normalization-method"
          name="normalization-method"
          class="methods__dropdown"
          @change="handleDropdownChange"
      >
        <option value="linear">Linear Normalization</option>
        <option value="l1">L1 Normalization</option>
        <option value="l2">L2 Normalization</option>
      </select>
    </div>
  </div>
</template>

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

.trade-off {
  width: 100%;
  height: 60px;
  border: 1px solid $light-gray;
  border-radius: 8px;
  padding: 20px 16px;
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
  cursor: pointer;
  transition: 0.2s ease-in-out;

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

.add-trade-off-btn {
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

.delete-trade-off-btn {
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

h2 {
  font-weight: 600;
  font-size: 1.25rem;
}

.container {
  width: 100%;
}

.methods {
  display: flex;
  flex-direction: column;
  gap: 5px;

  &__dropdown {
    border: 1px solid #e7e7e9;
    border-radius: 8px;
    padding: 8px;
    //appearance: auto;
    //-webkit-appearance: auto;
    background: url("@/assets/images/chevron-down.svg");
    background-repeat: no-repeat;
    background-size: 25px;
    background-position: center right 2px;

    &:focus {
      outline: 2px solid $main-blue-20;
      //background-image: url("@/assets/images/chevron-up.svg");
    }
  }

  label {
    width: fit-content;
    font-size: 0.875rem;
    font-weight: 300;
    font-style: italic;
  }
}

.criterion {
  display: flex;
  flex-direction: column;
  gap: 5px;

  input {
    border: 1px solid #e7e7e9;
    border-radius: 8px;
    padding: 8px;
  }
}

.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.back-btn {
  display: flex;
  align-items: center;
  width: fit-content;

  &:hover {
    color: $dark-gray;
  }

  &__text {
    padding-top: 1px;
    padding-left: 5px;
    cursor: pointer;
    transition: 0.1s ease-in-out;
  }

  @media screen and (max-width: 440px) {
    &__text {
      display: none;
    }
  }
}

.save-trade-off-btn {
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
}

.slider-container {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  row-gap: 5px;
  border-radius: 8px;
  border: 1px solid $light-gray;
  padding: 8px;

  .top-bar {
    display: flex;
    flex: 100%;
    justify-content: space-between;
    align-items: center;
  }

  .slider {
    width: 100%;
    opacity: 0.7;
    appearance: auto;
  }
}
</style>
