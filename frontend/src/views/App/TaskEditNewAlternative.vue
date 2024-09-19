<!-- TODO add value selector dropdown (decimal, string, etc) then an input field for the actual value -->

<template>
  <div class="w-100 mt-30">
    <div class="topbar w-100">
      <router-link :to="{ name: 'taskEditAlternatives' }" class="back-btn">
        <div class="chevron chevron--left"></div>
        <div class="back-btn__text">Back to Alternatives</div>
      </router-link>
      <div class="save-alternative-btn" @click="saveAlternative">
        <div class="save-alternative-btn__text">Save Alternative</div>
      </div>
    </div>
    <div class="alternative mt-20">
      <div class="alternative__name">
        <label for="name">Name (Required)</label>
        <input
          type="text"
          name="name"
          id="name"
          required
          minlength="3"
          maxlength="70"
          placeholder="Alternative Name"
        />
      </div>
      <div class="alternative__values mt-15">
        <label for="values">Values (Required)</label>
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Value</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(crit, index) in criteria" :key="index">
              <td>{{ crit.name }}</td>
              <td>
                <input
                  type="number"
                  :name="crit.name"
                  :id="crit.name"
                  :data-crit-id="crit.criterionID"
                  class="alt-value"
                  step="1"
                  required
                />
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="alternative__description mt-15">
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
    </div>
  </div>
</template>

<script>
import { useRoute } from "vue-router";
import axios from "axios";
import Swal from "sweetalert2";
import {
  alternatives as storedAlternatives,
  criteria as storedCriteria,
} from "@/store/store";

export default {
  name: "TaskEditNewAlternative",
  methods: {
    saveAlternative() {
      const name = document.getElementById("name").value;
      const description = document.getElementById("description").value;
      const taskID = this.route.params.taskID;

      const values = [];
      const inputFields = document.getElementsByClassName("alt-value");
      for (let i = 0; i < inputFields.length; i++) {
        values.push({
          key: inputFields[i].getAttribute("data-crit-id"),
          value: inputFields[i].value,
        });
      }

      const path = "http://127.0.0.1:5000/save-alternative-to-db";
      const axiosPromise = axios.post(path, {
        name: name,
        description: description,
        taskID: taskID,
        values: values,
      });

      const router = this.$router;
      axiosPromise
        .then((result) => {
          Swal.fire({
            position: "top-end",
            toast: true,
            icon: "success",
            title: "Alternative has been saved",
            showConfirmButton: false,
            timer: 3000,
          });

          // set stored alts to blank so that a DB call is triggered
          storedAlternatives.alternatives = [];

          router.push({
            name: "taskEditAlternatives",
          });
        })
        .catch(() => {
          console.log(
            "Error when creating a new alternative. Please try again..."
          );
        });
    },
  },
  created() {
    this.route = useRoute();
  },
  mounted() {
    // clear the text fields
    document.getElementById("name").value = "";
    document.getElementById("description").value = "";
  },
  data() {
    return {
      route: null,
      criteria: storedCriteria.criteria,
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

.save-alternative-btn {
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

.alternative {
  label {
    width: fit-content;
    font-size: 0.875rem;
    font-weight: 300;
    font-style: italic;
  }

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

  &__values {
    display: flex;
    flex-direction: column;
    gap: 5px;

    table {
      width: 100%;

      th,
      td {
        padding: 8px 12px;
        font-size: 0.875rem;
      }

      thead {
        tr {
          background-color: $main-blue-10;

          th {
          }
        }
      }

      tbody {
        tr:not(:last-child) {
          border-bottom: 1px solid $main-blue-10;
        }

        td {
          vertical-align: middle;
        }
      }

      input {
        outline: none;
        border: 1px solid $main-blue-10;
        border-radius: 4px;
        width: 100%;
        padding: 4px 8px;

        &:focus {
          border-color: $main-blue-20;
          outline: 1px solid $main-blue-20;
        }

        // hide arrows
        //-webkit-appearance: none;
        //margin: 0;
        //-moz-appearance: textfield;
      }

      input::-webkit-outer-spin-button,
      input::-webkit-outer-spin-button {
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
        margin: 0;
      }
    }
  }
}
</style>
