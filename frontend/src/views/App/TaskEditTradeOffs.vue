<script>
import axiosExtended from "@/router/axiosExtended";
import { useRoute } from "vue-router";
import Swal from "sweetalert2";

export default {
  name: "TaskEditTradeOffs",
  created() {
    this.route = useRoute();
    this.getTradeOffByTaskId();
  },
  data() {
    return {
      tradeOff: null,
      route: null,
    };
  },
  methods: {
    addNewTradeOff() {
      this.$router.push({
        name: "taskEditNewTradeOff",
      });
    },
    getTradeOffByTaskId() {
      const axiosPromise = axiosExtended.post("/get-trade-off-by-task-id", {
        taskID: this.route.params.taskID,
      });

      axiosPromise
        .then((response) => {
          if (response.data.success) {
            this.tradeOff = response.data;

            document
              .getElementsByClassName("delete-trade-off-btn")[0]
              .classList.add("delete-trade-off-btn--active");
          } else {
            document
              .getElementsByClassName("delete-trade-off-btn")[0]
              .classList.remove("delete-trade-off-btn--active");
          }
        })
        .catch(() => {
          console.log("Error when querying for criteria. Please try again...");
        });
    },
    deleteTradeOff() {
      if (
        !document
          .getElementsByClassName("delete-trade-off-btn")[0]
          .classList.contains("delete-trade-off-btn--active")
      ) {
        return;
      }

      const axiosPromise = axiosExtended.post("/delete-trade-off-by-task-id", {
        taskID: this.route.params.taskID,
      });

      axiosPromise
        .then((response) => {
          Swal.fire({
            position: "top-end",
            toast: true,
            icon: "success",
            title: "Trade-Off has been deleted",
            showConfirmButton: false,
            timer: 3000,
          });

          this.tradeOff = null;
          document
            .getElementsByClassName("delete-trade-off-btn")[0]
            .classList.remove("delete-trade-off-btn--active");
        })
        .catch((response) => {
          console.log("Error when deleting project.");
        });
    },
  },
};
</script>

<template>
  <div class="w-100 mt-30">
    <div class="topbar w-100">
      <h2>Trade-Offs</h2>
      <div class="btn-container">
        <div class="add-trade-off-btn" @click="addNewTradeOff" role="button">
          <div class="plus-icon plus-icon--white"></div>
          <div class="add-trade-off-btn__text">Add Trade-Off</div>
        </div>
        <div class="delete-trade-off-btn" @click="deleteTradeOff" role="button">
          <div class="trash-icon trash-icon--white"></div>
          <div class="delete-trade-off-btn__text">Delete</div>
        </div>
      </div>
    </div>
    <div v-if="tradeOff != null" class="trade-off mt-30">
      <span class="text">Trade-Off</span>
      <!--        suppress VueUnrecognizedDirective-->
      <span
        class="help"
        v-tooltip="{
          content: '<b>Decision Method</b>: ' + tradeOff.decisionMethod + '',
          html: true,
        }"
      ></span>
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
</style>
