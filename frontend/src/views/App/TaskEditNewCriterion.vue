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
        <select id="type">
          <option value="min">Quantitative</option>
          <option value="max">Ranking</option>
          <option value="min">Qualitative</option>
          <option value="min">Weighting</option>
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
      <div v-for="(alternative, index) in alternatives" :key="index" class="alternative mt-15">
        <label for="{{ alternative.name }}">{{ alternative.name }}</label>
        <input id="{{ alternative.name }}" name="{{ alternative.name }}" required type="number"
               placeholder="Enter a value"/>
      </div>
    </div>
  </div>
</template>

<script>
import {useRoute} from "vue-router";
import axios from "axios";
import Swal from "sweetalert2";
import {criteria as storedCriteria} from "@/store/store";

export default {
  name: "TaskEditNewCriterion",
  methods: {
    saveCriterion() {
      const name = document.getElementById("name").value;
      const beneficiality = document.getElementById("beneficiality").value;
      const description = document.getElementById("description").value;
      const taskID = this.route.params.taskID;

      const values = [];
      document.querySelectorAll(".alternative input").forEach(input => {
        values.push(parseFloat(input.value));
      });

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
          })
          .catch(() => {
            console.log(
                "Error when querying for alternatives. Please try again..."
            );
          });
    }
    ,
  },
  created() {
    this.route = useRoute();
    this.getAlternativesByTaskID()
  },
  mounted() {
    // clear the text fields
    document.getElementById("name").value = "";
    document.getElementById("description").value = "";
  },
  data() {
    return {
      route: null,
      alternatives: []
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
</style>
