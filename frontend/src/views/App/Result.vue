<script>
import TheHeader from "@/components/AppComponents/TheHeader.vue";
import axiosExtended from "@/router/axiosExtended";
import * as echarts from "echarts";
import { useRoute } from "vue-router";
import jsPDF from "jspdf";
import html2canvas from "html2canvas";
import Swal from "sweetalert2";

export default {
  name: "Result",
  components: { TheHeader },
  data() {
    return {
      ranking: [],
      decisionMatrix: {
        criteria: [],
        alternatives: [],
        values: [],
      },
      chartInstance: null,
    };
  },
  components: {TheHeader},
  created() {
    this.route = useRoute();
  },
  mounted() {
    this.calculateResult();
  },
  methods: {
    formatNumber(number, decimals) {
    if (typeof number !== "number" || isNaN(number)) {
      return "N/A"; // or return "0" if you prefer
    }
    return number.toFixed(decimals);
  },
    calculateResult() {
      let loader = this.$loading.show({
        container: document.getElementById("loader-container"),
      });

      axiosExtended
          .post("/calculate-result", {
            projectID: this.route.params.projectID,
            taskID: this.route.params.taskID,
          })
          .then((response) => {
            if (response.data.success) {
              this.ranking = response.data.ranking;
              this.decisionMatrix = response.data.decision_matrix;
              this.renderChart(); // Render chart after data is loaded
            }
            loader.hide();
          })
          .catch(() => {
            Swal.fire({
              icon: "error",
              text: "Error when calculating result. Check if all variables are set!",
              position: "top-end",
              toast: true,
              showConfirmButton: false,
              timer: 5000,
            });
          });
    },
    renderChart() {
      const chartDom = document.getElementById("resultChart");
      if (!chartDom) return;

      if (this.chartInstance) {
        this.chartInstance.dispose(); // Properly dispose before re-initializing
      }

      this.chartInstance = echarts.init(chartDom);
      const names = this.ranking.map((item) => item.name);
      const scores = this.ranking.map((item) => item.score);

      const option = {
        title: { text: "Ranking Scores", left: "center" },
        tooltip: { trigger: "axis", axisPointer: { type: "shadow" } },
        xAxis: { type: "category", data: names, axisLabel: { rotate: 45 } },
        yAxis: { type: "value", name: "Score" },
        series: [{ data: scores, type: "bar", color: "#2ecc71" }],
        grid: { left: "3%", right: "4%", bottom: "10%", containLabel: true },
      };

      this.chartInstance.setOption(option);
    },
    async downloadPDF() {
      try {
        const pdf = new jsPDF("p", "mm", "a4");

        // Capture Ranking Table
        const rankingTableElement = document.querySelector(".tables-container .table-wrapper:first-child table");
        const rankingTableCanvas = await html2canvas(rankingTableElement, { scale: 2 });
        const rankingTableImage = rankingTableCanvas.toDataURL("image/png");

        // Capture Decision Matrix Table
        const decisionMatrixTableElement = document.querySelector(".tables-container .table-wrapper:last-child table");
        const decisionMatrixTableCanvas = await html2canvas(decisionMatrixTableElement, { scale: 2 });
        const decisionMatrixTableImage = decisionMatrixTableCanvas.toDataURL("image/png");

        // Capture Chart
        const chartElement = document.getElementById("resultChart");
        const chartCanvas = await html2canvas(chartElement, { scale: 2 });
        const chartImage = chartCanvas.toDataURL("image/png");

        // Add Ranking Table to PDF
        pdf.text("Ranking Table", 10, 10);
        pdf.addImage(rankingTableImage, "PNG", 10, 20, 180, 50);

        // Add Decision Matrix Table to PDF
        pdf.text("Decision Matrix Table", 10, 80);
        pdf.addImage(decisionMatrixTableImage, "PNG", 10, 90, 180, 50);

        // Add Chart to PDF
        pdf.text("Ranking Chart", 10, 150);
        pdf.addImage(chartImage, "PNG", 10, 160, 180, 80);

        // Save PDF
        pdf.save("result.pdf");
      } catch (error) {
        console.error("Error generating PDF:", error);
        alert("Failed to generate PDF. Please try again.");
      }
    }
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
    <div class="full-width mt-45 pb-20" id="loader-container">
      <h2>Result</h2>

      <div class="tables-container">
        <div class="table-wrapper">
          <h3>Ranking</h3>
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
                <td>{{ formatNumber(Number(rank.score), 4) }}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="table-wrapper">
          <h3>Decision Matrix</h3>
          <table class="mt-30">
            <thead>
              <tr>
                <th>Alternative</th>
                <th v-for="criterion in decisionMatrix.criteria" :key="criterion">
                  {{ criterion }}
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(alternative, index) in decisionMatrix.alternatives" :key="index">
                <td>{{ alternative }}</td>
                <td v-for="(value, idx) in decisionMatrix.values[index]" :key="idx">
                  {{ formatNumber(Number(value), 2) }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div id="resultChart" class="chart-container"></div>

      <button @click="downloadPDF" class="download-button">
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
      background-color: #2ecc71;
      color: white;
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
        border-bottom: 2px solid #2ecc71;
      }

      td {
        padding: 12px 15px;
      }

      &:hover {
        color: #2ecc71;
      }
    }
  }
}

.chart-container {
  width: 100%;
  height: 400px;
  margin-top: 30px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.tables-container {
  display: flex;
  gap: 20px;
  margin-top: 30px;

  .table-wrapper {
    flex: 1;
  }
}

table {
  border-collapse: collapse;
  font-size: 0.9rem;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
  width: 100%;

  thead {
    tr {
      background-color: #2ecc71;
      color: white;
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
        border-bottom: 2px solid #2ecc71;
      }

      td {
        padding: 12px 15px;
      }

      &:hover {
        color: #2ecc71;
      }
    }
  }
}
.download-button {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #2ecc71;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;

  &:hover {
    background-color: #27ae60;
  }
}
</style>