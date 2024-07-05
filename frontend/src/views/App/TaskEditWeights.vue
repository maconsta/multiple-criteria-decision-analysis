<template>
  <div class="w-100 mt-30">
    <div class="topbar w-100">
      <h2>Weights</h2>
      <div class="calculate-btn" @click="calculateTask" role="button">
        <div class="cpu-icon cpu-icon--white"></div>
        <div class="calculate-btn__text">Calculate</div>
      </div>
    </div>
    <div class="weights mt-30">
      <div v-for="(crit, index) in criteriaPairs" class="weight" :key="index">
        <div class="weight__text mb-10">
          <h3>{{ crit.rowName }}</h3>
          <h3>{{ crit.colName }}</h3>
        </div>
        <div
          class="slider w-100"
          :data-row-index="crit.rowIndex"
          :data-col-index="crit.colIndex"
        ></div>
      </div>
    </div>
  </div>
</template>

<script>
import noUiSlider from "nouislider";
import "nouislider/dist/nouislider.css";
import axios from "axios";
import { useRoute } from "vue-router";
import {
  criteria as storedCriteria,
  weights,
  alternatives as storedAlternatives,
  selectedMethod,
} from "@/store/store";
import { forwardAsync } from "@babel/core/lib/gensync-utils/async";

export default {
  name: "TaskEditWeights",
  data() {
    return {
      criteria: storedCriteria.criteria,
      criteriaPairs: [],
      route: null,
    };
  },
  methods: {
    getCriteriaByTaskID() {
      const path = "http://127.0.0.1:5000/get-criteria-by-task-id";
      const axiosPromise = axios.post(path, {
        taskID: this.route.params.taskID,
      });

      axiosPromise
        .then((response) => {
          this.criteria = response.data;
          storedCriteria.criteria = response.data;
          this.createCriteriaPairs();
        })
        .catch(() => {
          console.log("Error when querying for criteria. Please try again...");
        });
    },
    createCriteriaPairs() {
      for (let i = 0; i < this.criteria.length - 1; i++) {
        for (let j = i + 1; j < this.criteria.length; j++) {
          this.criteriaPairs.push({
            rowName: this.criteria[i].name,
            rowIndex: i,
            colName: this.criteria[j].name,
            colIndex: j,
          });
        }
      }
    },
    calculateTask(e) {
      if (!e.currentTarget.classList.contains("calculate-btn--active")) {
        return;
      }

      // for the calculate to work, you have to go through ALL buttons
      // TODO: make buttons inaccessible if the previous button hasn't been clicked

      let weightMatrix = weights.matrix;
      let criteria = this.criteria;
      let alternatives = storedAlternatives.alternatives;
      let method = selectedMethod.method;

      const path = "http://127.0.0.1:5000/calculate-results";
      const axiosPromise = axios.post(path, {
        weightMatrix: weightMatrix,
        criteria: criteria,
        alternatives: alternatives,
        method: method,
      });

      axiosPromise.then(() => {}).catch(() => {});
    },
  },
  created() {
    this.route = useRoute();

    if (!storedCriteria.criteria.length) {
      this.getCriteriaByTaskID();
    } else {
      this.createCriteriaPairs();
    }
  },
  mounted() {
    noUiSlider.cssClasses.target += " range-slider";

    let sliders = document.getElementsByClassName("slider");

    // todo: implement store for criteria and remove the timeout
    setTimeout(function () {
      for (const slider of sliders) {
        noUiSlider.create(slider, {
          range: {
            min: -9,
            max: 9,
          },
          step: 1,
          start: [0],
          pips: {
            mode: "steps",
            filter: (value) => {
              if (value % 1 === 0) {
                return 1;
              }
              return -1;
            },
          },
        });

        slider.noUiSlider.on("set", function (values) {
          const value = parseInt(values[0]);
          const rowIndex = parseInt(slider.getAttribute("data-row-index"));
          const colIndex = parseInt(slider.getAttribute("data-col-index"));

          let weightMatrix = weights.matrix;
          if (weightMatrix.length === 0) {
            weightMatrix = new Array(storedCriteria.criteria.length)
              .fill(1)
              .map(() => new Array(storedCriteria.criteria.length).fill(1));
          }

          if (value > 0) {
            weightMatrix[rowIndex][colIndex] = value;
            weightMatrix[colIndex][rowIndex] = 1 / value;
          } else if (value < 0) {
            weightMatrix[rowIndex][colIndex] = 1 / (value * -1);
            weightMatrix[colIndex][rowIndex] = value * -1;
          }
          weights.matrix = weightMatrix;

          // make calc button active if all values are set properly
          let flag = true;
          for (const s of sliders) {
            const val = parseInt(s.noUiSlider.get());
            if (val === 0) {
              flag = false;
            }
          }

          if (flag) {
            document
              .getElementsByClassName("calculate-btn")[0]
              .classList.add("calculate-btn--active");
          } else {
            document
              .getElementsByClassName("calculate-btn")[0]
              .classList.remove("calculate-btn--active");
          }
        });
      }
    }, 500);
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
}

.calculate-btn {
  display: flex;
  align-items: center;
  gap: 5px;
  background-color: gray;
  border-radius: 8px;
  width: fit-content;
  padding: 8px 12px 6px;
  cursor: pointer;
  transition: 0.2s ease-in-out;

  &__text {
    line-height: 2em;
    color: #fff;
    white-space: nowrap;
  }

  &--active {
    background-color: $plant-green;
  }
}

.weights {
  display: flex;
  flex-direction: column;
  row-gap: 15px;
}

.weight {
  width: 100%;
  padding: 16px 20px 40px;
  border-radius: 8px;
  border: 1px solid #e7e7e9;

  &__text {
    display: flex;
    justify-content: space-between;

    h3 {
      display: inline-block;
      font-weight: 500;
      font-size: 16px;
    }
  }
}
</style>
