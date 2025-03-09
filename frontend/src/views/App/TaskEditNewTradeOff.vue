<template>
  <div class="w-100 mt-30 pb-20">
    <div class="topbar w-100">
      <router-link :to="{ name: 'taskEditTradeOffs' }" class="back-btn">
        <div class="chevron chevron--left"></div>
        <div class="back-btn__text">Back to Trade-Offs</div>
      </router-link>
      <div class="save-trade-off-btn" @click="saveTradeOff">
        <div class="save-trade-off-btn__text">Save Trade-Off</div>
      </div>
    </div>
    <div class="methods mt-30">
      <label for="decision-method">Decision Methods (Required)</label>
      <select
          id="decision-method"
          name="decision-method"
          class="methods__dropdown"
      >
        <option value="topsis">Topsis</option>
        <option value="ahp">AHP</option>
        <option value="electre">Electre</option>
        <option value="wsm">Weighted Sum</option>
        <option value="prometheeii">PROMETHEE II</option>
      </select>
      <label for="normalization-method" class="mt-15"
      >Normalization Method</label
      >
      <select
          id="normalization-method"
          name="normalization-method"
          class="methods__dropdown"
      >
        <option value="linear">Linear Normalization</option>
        <option value="l1">L1 Normalization</option>
        <option value="l2">L2 Normalization</option>
      </select>
    </div>
    <div class="line mb-30 mt-30"></div>
    <div class="methods">
      <label>Add Weights (Required)</label>
      <div v-for="(pair, index) in pairwiseCriteria" class="mt-15" :key="index">
        <div class="slider-container">
          <div class="top-bar">
            <span>{{ pair[0] }}</span>
            <span>{{ pair[1] }}</span>
          </div>
          <input
              type="range"
              min="-8"
              max="8"
              value="0"
              class="slider"
              :id="'input-slider-' + index"
              @input="updateValue($event)"
              list="markers"
          />
          <datalist id="markers">
            <option value="-8"></option>
            <option value="-6"></option>
            <option value="-4"></option>
            <option value="-2"></option>
            <option value="0"></option>
            <option value="2"></option>
            <option value="4"></option>
            <option value="6"></option>
            <option value="8"></option>
          </datalist>
          <label class="value-container" :for="'input-slider-' + index"
          >Value:
            <output class="value">Equal Importance</output>
          </label>
        </div>
      </div>

      <!--      <div v-for="(criterion, index) in criteria" :key="index" class="criterion mt-15">-->
      <!--        <label for="{{ criterion.name }}">{{ criterion.name }}</label>-->
      <!--        <input id="{{ criterion.name }}" name="{{ criterion.name }}" required type="number"-->
      <!--               placeholder="Enter a value"/>-->
      <!--      </div>-->
    </div>
  </div>
</template>

<script>
import {helpText, selectedMethod} from "@/store/store";
import axiosExtended from "@/router/axiosExtended";
import {useRoute} from "vue-router";
import Swal from "sweetalert2";

export default {
  name: "TaskEditNewTradeOff",
  methods: {
    getCriteriaByTaskID() {
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

            this.fillPairwiseCriteria();
          })
          .catch(() => {
            console.log("Error when querying for criteria. Please try again...");
          });
    },
    saveTradeOff() {
      const decisionMethod = document.getElementById("decision-method").value;
      const normalizationMethod = document.getElementById(
          "normalization-method"
      ).value;
      const taskID = this.route.params.taskID;

      let pairwise = false;
      const weights = [];
      document.querySelectorAll(".slider-container input").forEach((input) => {
        let val = parseInt(input.value);
        if (val < 0) {
          val *= -1;
          val += 1;
          val = 1 / val;
        } else {
          val += 1;
        }

        weights.push(val);
      });

      pairwise = true;

      // direct weight input method; TODO add option to add weights directly for testing purposes
      // document.querySelectorAll(".criterion input").forEach(input => {
      //   weights.push(parseFloat(input.value));
      // });

      const axiosPromise = axiosExtended.post("/save-trade-off-to-db", {
        decisionMethod: decisionMethod,
        normalizationMethod: normalizationMethod,
        taskID: taskID,
        weights: weights,
        pairwise: pairwise,
      });

      const router = this.$router;
      axiosPromise
          .then((result) => {
            Swal.fire({
              position: "top-end",
              toast: true,
              icon: "success",
              title: "Trade Off has been saved",
              showConfirmButton: false,
              timer: 3000,
            });

            router.push({
              name: "taskEditTradeOffs",
            });
          })
          .catch(() => {
            console.log(
                "Error when creating a new trade-off. Please try again..."
            );
          });
    },
    fillPairwiseCriteria() {
      for (let i = 0; i < this.criteria.length - 1; i++) {
        for (let j = i + 1; j < this.criteria.length; j++) {
          this.pairwiseCriteria.push([
            this.criteria[i].name,
            this.criteria[j].name,
          ]);
        }
      }
    },
    updateValue(event) {
      const sliderID = event.target.id;

      let val = parseInt(event.target.value);
      if (val < 0) {
        val *= -1;
      }

      let text = "";
      if (val === 0) {
        text = "Equal Importance";
      } else if (val === 1) {
        text = "Marginal Importance";
      } else if (val === 2) {
        text = "Low Importance";
      } else if (val === 3) {
        text = "Moderate Importance";
      } else if (val === 4) {
        text = "Substantial Importance";
      } else if (val === 5) {
        text = "Considerable Importance";
      } else if (val === 6) {
        text = "Significant Importance";
      } else if (val === 7) {
        text = "High Importance";
      } else if (val === 8) {
        text = "Absolute Importance";
      }

      document.querySelector("label[for='" + sliderID + "'] output").innerHTML =
          text;
    },
  },
  data() {
    return {
      helpText,
      criteria: [],
      route: null,
      pairwiseCriteria: [],
    };
  },
  mounted() {
    if (selectedMethod.method) {
      document
          .querySelector("div[data-method='" + selectedMethod.method + "']")
          .click();
    }
  },
  created() {
    this.route = useRoute();
    this.getCriteriaByTaskID();
  },
};
</script>

<style scoped lang="scss">
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
