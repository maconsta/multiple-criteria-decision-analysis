<template>
  <div class="w-100 mt-30">
    <div class="topbar w-100">
      <router-link :to="{ name: 'taskEditCriteria' }" class="back-btn">
        <div class="chevron chevron--left"></div>
        <div class="back-btn__text">Back to Criteria</div>
      </router-link>
      <div class="save-criterion-btn" @click="saveCriterion">
        <div class="save-criterion-btn__text">Save Criterion</div>
      </div>
    </div>
    <div class="criterion mt-20">
      <div class="criterion__name">
        <label for="name">Name (Required)</label>
        <input
            type="text"
            name="name"
            id="name"
            required
            minlength="3"
            maxlength="70"
            placeholder="Criterion Name"
        />
      </div>
      <div class="criterion__dropdown mt-15">
        <label for="beneficiality">Beneficiality (Required)</label>
        <select id="beneficiality">
          <option value="max">Beneficial</option>
          <option value="min">Non-beneficial</option>
        </select>
      </div>
      <div class="criterion__dropdown mt-15">
        <label for="type">Criterion Type (Required)</label>
        <select id="type" @change="onCritTypeChange($event)">
          <option value="section-quantitative">Quantitative</option>
          <option value="section-ranking">Ranking</option>
          <option value="section-qualitative">Qualitative</option>
          <option value="section-weighting">Weighting</option>
        </select>
      </div>
      <div class="criterion__description mt-15">
        <label for="description">Description (Required)</label>
        <textarea
            type="text"
            name="description"
            id="description"
            minlength="3"
            maxlength="80"
            placeholder="..."
            required
        />
      </div>

      <div class="line mb-30 mt-30"></div>
      <span>Alternative Values (Required)</span>

      <div id="section-quantitative" class="section">
        <div v-for="(alternative, index) in alternatives" :key="index" class="alternative mt-15">
          <label for="{{ alternative.name }}">{{ alternative.name }}</label>
          <input id="{{ alternative.name }}" name="{{ alternative.name }}" required type="number"
                 placeholder="Enter a value"/>
        </div>
      </div>

      <div id="section-ranking" class="section disabled">
        <ul id="draggable" class="mt-15">
          <li v-for="(alternative, index) in alternatives" :key="index">
            <span class="alt-name">{{ alternative.name }}</span>
            <span class="order-number">{{ index + 1 }}</span>
          </li>
        </ul>
      </div>

      <div id="section-qualitative" class="section disabled mt-15">
        <div id="radio-buttons">
          <div v-for="(alternative, index) in alternatives" :key="index" class="">
            <span class="mt-10">{{ alternative.name }}</span>
            <div class="radio-container mt-10">
              <label :for="'terrible' + index">Terrible</label>
              <input type="radio" :name="'qualitative-value-' + index" :id="'terrible' + index" value="1">
            </div>
            <div class="radio-container mt-5">
              <label :for="'very-bad-' + index">Very Bad</label>
              <input type="radio" :name="'qualitative-value-' + index" :id="'very-bad-' + index" value="2">
            </div>
            <div class="radio-container mt-5">
              <label :for="'bad-' + index">Bad</label>
              <input type="radio" :name="'qualitative-value-' + index" :id="'bad-' + index" value="3">
            </div>
            <div class="radio-container mt-5">
              <label :for="'subpar-' + index">Subpar</label>
              <input type="radio" :name="'qualitative-value-' + index" :id="'subpar-' + index" value="4">
            </div>
            <div class="radio-container mt-5">
              <label :for="'average-' + index">Average</label>
              <input type="radio" :name="'qualitative-value-' + index" :id="'average-' + index" value="5">
            </div>
            <div class="radio-container mt-5">
              <label :for="'fair-' + index">Fair</label>
              <input type="radio" :name="'qualitative-value-' + index" :id="'fair-' + index" value="6">
            </div>
            <div class="radio-container mt-5">
              <label :for="'good-' + index">Good</label>
              <input type="radio" :name="'qualitative-value-' + index" :id="'good-' + index" value="7">
            </div>
            <div class="radio-container mt-5">
              <label :for="'very-good-' + index">Very Good</label>
              <input type="radio" :name="'qualitative-value-' + index" :id="'very-good-' + index" value="8">
            </div>
            <div class="radio-container mt-5">
              <label :for="'excellent-' + index">Excellent</label>
              <input type="radio" :name="'qualitative-value-' + index" :id="'excellent-' + index" value="9">
            </div>
          </div>
        </div>
      </div>

      <div id="section-weighting" class="section disabled">
        <div v-for="i in alternatives.length">{{ alternatives[i - 1].name }}</div>
        <div class="slidercontainer">
          <input type="range" min="1" max="100" value="50" class="slider" id="myRange">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {useRoute} from "vue-router";
import axios from "axios";
import Swal from "sweetalert2";
import {alternatives, criteria as storedCriteria} from "@/store/store";
import Sortable from "sortablejs";

export default {
  name: "TaskEditNewCriterion",
  methods: {
    saveCriterion() {
      const name = document.getElementById("name").value;
      const beneficiality = document.getElementById("beneficiality").value;
      const description = document.getElementById("description").value;
      const taskID = this.route.params.taskID;
      const section = document.querySelector(".section:not(.disabled)").id;

      let values = [];
      if (section === "section-quantitative") {
        document.querySelectorAll(".alternative input").forEach(input => {
          values.push(parseFloat(input.value));
        });
      } else if (section === "section-ranking") {
        // FORMULA FOR CALCULATING THE RANKING SCORE FOR EACH INDIVIDUAL ALTERNATIVE
        // score = alternatives_length - current_order_number + 1

        document.querySelectorAll("#draggable li").forEach(li => {
          const name = li.getElementsByClassName("alt-name")[0].innerHTML;
          const order = parseInt(li.getElementsByClassName("order-number")[0].innerHTML);

          for (let i = 0; i < this.alternatives.length; i++) {
            if (name === this.alternatives[i].name) {
              values[i] = this.alternatives.length - order + 1;
            }
          }
        })
      } else if (section === "section-qualitative") {
        for (let i = 0; i < this.alternatives.length; i++) {
          let val = parseInt(document.querySelector("input[name='qualitative-value-" + i + "']:checked").value);
          values.push(val);
        }
      } else if (section === "section-weighting") {
        // how to set values here?
      }

      const path = "http://127.0.0.1:5000/save-criterion-to-db";
      const axiosPromise = axios.post(path, {
        name: name,
        beneficiality: beneficiality,
        description: description,
        taskID: taskID,
        values: values,
      }, {
        withCredentials: true,
        headers: {
          "X-CSRF-TOKEN": localStorage.getItem("csrfToken"),
        }
      });

      const router = this.$router;
      axiosPromise
          .then(() => {
            Swal.fire({
              position: "top-end",
              toast: true,
              icon: "success",
              title: "Criterion has been saved",
              showConfirmButton: false,
              timer: 3000,
            });

            // set stored crit to an empty arr to trigger a DB call
            storedCriteria.criteria = [];

            router.push({
              name: "taskEditCriteria",
            });
          })
          .catch(() => {
            console.log(
                "Error when creating a new criterion. Please try again..."
            );
          });
    },
    getAlternativesByTaskID() {
      const path = "http://127.0.0.1:5000/get-alternatives-by-task-id";
      const axiosPromise = axios.post(path, {
        taskID: this.route.params.taskID,
        projectID: this.route.params.projectID,
      }, {
        withCredentials: true,
        headers: {
          "X-CSRF-TOKEN": localStorage.getItem("csrfToken"),
        },
      });

      axiosPromise
          .then((response) => {
            this.alternatives = response.data;
            // this.fillWeightingAlternatives();
          })
          .catch(() => {
            console.log(
                "Error when querying for alternatives. Please try again..."
            );
          });
    },
    onCritTypeChange(event) {
      const selectedSection = document.getElementById(event.target.value);
      const allSections = document.getElementsByClassName("section");
      for (const section of allSections) {
        section.classList.add("disabled");
      }
      selectedSection.classList.remove("disabled");
    },
    fillWeightingAlternatives() {
      // console.log(this.alternatives.length)
      // for (let i = 0; i < this.alternatives.length; i++) {
      //   for (let j = 0; j < this.alternatives.length; j++) {
      //     //  fix weights
      //     this.weightingAlternatives[i][j] =
      //   }
      // }
    }
  },
  created() {
    this.route = useRoute();
    this.getAlternativesByTaskID()
  },
  mounted() {
    // clear the text fields
    document.getElementById("name").value = "";
    document.getElementById("description").value = "";

    const updateOrder = () => {
      const orderNumbers = document.getElementsByClassName("order-number");
      for (let i = 0; i < orderNumbers.length; i++) {
        const orderNumber = orderNumbers[i];
        orderNumber.innerHTML = i + 1;
      }
    };

    // create a draggable component
    const el = document.getElementById("draggable");
    let sortable = Sortable.create(el, {
      onEnd: (evt) => {
        updateOrder();
      }
    });

    updateOrder();
  },
  data() {
    return {
      route: null,
      alternatives: [],
      weightingAlternatives: []
    };
  },
};
</script>

<style scoped lang="scss">
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
}

.save-criterion-btn {
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

.criterion {
  &__name {
    display: flex;
    flex-direction: column;
    gap: 5px;

    input {
      border: 1px solid $light-gray;
      border-radius: 8px;
      padding: 8px;
      //transition: 0.2s ease-in-out;

      &:focus {
        outline: 2px solid $main-blue-20;
      }
    }
  }

  &__dropdown {
    display: flex;
    flex-direction: column;
    gap: 5px;

    select {
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
  }

  &__description {
    display: flex;
    flex-direction: column;
    gap: 5px;

    textarea {
      border: 1px solid $light-gray;
      border-radius: 8px;
      padding: 8px;
      height: 100px;
      vertical-align: top;
      resize: none;

      &:focus {
        outline: 2px solid $main-blue-20;
      }
    }
  }

  label {
    width: fit-content;
    font-size: 0.875rem;
    font-weight: 300;
    font-style: italic;
  }
}

.alternative {
  display: flex;
  flex-direction: column;
  gap: 5px;

  input {
    border: 1px solid #e7e7e9;
    border-radius: 8px;
    padding: 8px;
  }
}

#draggable {
  li {
    border: 1px solid $light-gray;
    padding: 12px 20px;
    margin: 5px 0;
    cursor: move;
    cursor: -webkit-grabbing;
    display: flex;
    justify-content: space-between;

    &:first-child {
      border-top-left-radius: 4px;
      border-top-right-radius: 4px;
    }

    &:last-child {
      border-bottom-left-radius: 4px;
      border-bottom-right-radius: 4px;
    }
  }

  .sortable-ghost {
    background-color: $main-blue;
    opacity: 0.1;
  }

  .order-number {
    border-radius: 50%;
    background-color: $light-gray;
    width: 20px;
    height: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.8rem;
    line-height: 0.8rem;
  }
}

.section {
  &.disabled {
    display: none;
  }
}

#radio-buttons {
  display: flex;
  flex-wrap: wrap;
  row-gap: 15px;
  column-gap: 25px;

  .radio-container {
    display: flex;
    justify-content: space-between;
    column-gap: 5px;

    input {
      appearance: auto;
    }
  }
}

</style>
