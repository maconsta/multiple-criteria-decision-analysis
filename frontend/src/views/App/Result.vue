<script>
import TheHeader from "@/components/AppComponents/TheHeader.vue";
import axios from "axios";
import {useRoute} from "vue-router";

export default {
  name: "Result",
  data() {
    return {
      route: null,
      ranking: [],
    };
  },
  components: {TheHeader},
  created() {
    this.route = useRoute();
    this.calculateResult();
  },
  methods: {
    formatNumber(number, decimals) {
      return number.toFixed(decimals);
    },
    calculateResult() {
      const path = "http://127.0.0.1:5000/calculate-result";
      const axiosPromise = axios.post(
          path,
          {
            projectID: this.route.params.projectID,
            taskID: this.route.params.taskID,
          },
          {
            withCredentials: true,
            headers: {
              "X-CSRF-TOKEN": localStorage.getItem("csrfToken"),
            },
          }
      );

      axiosPromise
          .then((response) => {
            if (response.data.success) {
              console.log(response.data)
              this.ranking = response.data.ranking;
            }
          })
          .catch(() => {
            console.log("Error when creating a new project. Please try again...");
          });
    },
  }
}
</script>

<template>
  <div class="main">
    <TheHeader/>
    <div class="full-width mt-45">
      <h2>Result</h2>
      <table class="mt-30">
        <thead>
        <tr>
          <th>Rank</th>
          <th>Name</th>
          <th>Score</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(rank, index) in ranking" :key="index">
          <td>{{ index + 1 }}</td>
          <td>{{ rank.name }}</td>
          <td>{{ formatNumber(rank.score, 4) }}</td>
        </tr>
        </tbody>

      </table>
    </div>
  </div>

</template>

<style scoped lang="scss">
h2 {
  font-weight: 600;
  font-size: 1.25rem;
}

table {
  border-collapse: collapse;
  font-size: 0.9rem;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);

  thead {
    tr {
      background-color: $plant-green;
      color: #ffffff;
      text-align: left;

      th {
        padding: 12px 15px;
        min-width: 100px;
      }
    }
  }

  tbody {
    tr {
      border-bottom: 1px solid #dddddd;

      &:nth-child(even) {
        background-color: #f3f3f3;
      }
    ;

      &:last-child {
        border-bottom: 2px solid $plant-green;
      }

      td {
        padding: 12px 15px;
      }

      &:hover {
        font-weight: 600;
        color: $plant-green;
      }
    }
  }
}
</style>