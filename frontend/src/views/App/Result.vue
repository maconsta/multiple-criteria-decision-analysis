<script>
import TheHeader from "@/components/AppComponents/TheHeader.vue";
import axiosExtended from "@/router/axiosExtended";
import * as echarts from "echarts";
import {useRoute} from "vue-router";
import jsPDF from "jspdf";
import html2canvas from "html2canvas";

export default {
  name: "Result",
  data() {
    return {
      route: null,
      ranking: [],
      chartInstance: null,
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
      axiosExtended
          .post("/calculate-result", {
            projectID: this.route.params.projectID,
            taskID: this.route.params.taskID,
          })
          .then((response) => {
            if (response.data.success) {
              this.ranking = response.data.ranking;
              this.renderChart(); // Render chart after data is loaded
            }
          })
          .catch(() => {
            console.log("Error when creating a new project. Please try again...");
          });
    },
    renderChart() {
      const chartDom = document.getElementById("resultChart");
      if (!this.chartInstance) {
        this.chartInstance = echarts.init(chartDom);
      }

      const names = this.ranking.map((item) => item.name);
      const scores = this.ranking.map((item) => item.score);

      const option = {
        title: {text: "Ranking Scores", left: "center"},
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        tooltip: {
          trigger: "axis", axisPointer: {
            type: 'shadow'
          }
        },
        xAxis: {type: "category", data: names, axisLabel: {rotate: 90}},
        yAxis: {type: "value", name: "Score"},
        series: [{data: scores, type: "bar", color: "#2ecc71"}],
      };

      this.chartInstance.setOption(option);
    },
    async downloadPDF() {
      const pdf = new jsPDF();

      // Capture table as image
      const tableElement = document.querySelector("table");
      const tableCanvas = await html2canvas(tableElement);
      const tableImage = tableCanvas.toDataURL("image/png");

      // Capture chart as image
      const chartElement = document.getElementById("resultChart");
      const chartCanvas = await html2canvas(chartElement);
      const chartImage = chartCanvas.toDataURL("image/png");

      // Add table image to PDF
      pdf.text("Result Table", 10, 10);
      pdf.addImage(tableImage, "PNG", 10, 20, 190, 60);

      // Add chart image to PDF
      pdf.text("Ranking Chart", 10, 90);
      pdf.addImage(chartImage, "PNG", 10, 100, 190, 80);

      // Save PDF
      pdf.save("result.pdf");
    },
  },
  beforeUnmount() {
    if (this.chartInstance) {
      this.chartInstance.dispose();
    }
  },
};
</script>

<template>
  <div class="main">
    <div class="full-width mt-45 pb-20">
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
      <div
          id="resultChart"
          style="width: 100%; height: 400px; margin-top: 30px"
      ></div>
      <button
          @click="downloadPDF"
          style="
          margin-top: 20px;
          padding: 10px 20px;
          background-color: #2ecc71;
          color: white;
          border: none;
          border-radius: 5px;
          cursor: pointer;
        "
      >
        Download PDF
      </button>
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

      &:last-child {
        border-bottom: 2px solid $plant-green;
      }

      td {
        padding: 12px 15px;
      }

      &:hover {
        color: $plant-green;
      }
    }
  }

  @media screen and (max-width: 440px) {
    thead {
      tr {
        th {
          min-width: auto;
        }
      }
    }
  }
}

#resultChart {
  border: 1px solid #ddd;
  border-radius: 5px;
}
</style>
