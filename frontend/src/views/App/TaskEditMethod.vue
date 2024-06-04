<template>
  <div class="w-100 mt-30">
    <h2>Select Method</h2>
    <div class="methods mt-20">
      <div class="method" @click="selectMethod($event)">
        <span class="checkbox"></span>
        <span class="text">TOPSIS</span>
        <span class="help"></span>
      </div>
      <div class="method" @click="selectMethod($event)">
        <span class="checkbox"></span>
        <span class="text">AHP</span>
        <span class="help"></span>
      </div>
      <div class="method" @click="selectMethod($event)">
        <span class="checkbox"></span>
        <span class="text">Electre</span>
        <span class="help"></span>
      </div>
      <div class="method" @click="selectMethod($event)">
        <span class="checkbox"></span>
        <span class="text">Weighted Sum</span>
        <span class="help"></span>
      </div>
      <div class="method" @click="selectMethod($event)">
        <span class="checkbox"></span>
        <span class="text">PROMETHEE II</span>
        <span class="help"></span>
      </div>
    </div>
  </div>
</template>

<script>
import { helpText } from "@/store/store";

export default {
  name: "TaskEditMethod",
  methods: {
    selectMethod(event) {
      const allCheckboxes = document.getElementsByClassName("checkbox");
      for (let checkbox of allCheckboxes) {
        checkbox.classList.remove("checkbox--selected");
      }

      const checkbox = event.currentTarget.querySelector(".checkbox");
      checkbox.classList.add("checkbox--selected");

      helpText.text = "Test Methods";

      // Todo: add call to DB and make a decision matrix?
    },
  },
  data() {
    return {
      helpText,
    };
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
  gap: 10px;
}

.method {
  width: 100%;
  height: 60px;
  border: 1px solid $light-gray;
  border-radius: 8px;
  padding: 8px 16px 8px 8px;
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  transition: 0.2s ease-in-out;

  .checkbox {
    height: 10px;
    width: 10px;
    border: 1px solid $charcoal;
    border-radius: 50%;

    &--selected {
      background-color: $charcoal;
    }
  }

  .text {
    align-self: center;
    flex: 1;
    font-weight: 500;
    font-size: 15px;
  }

  &:hover {
    border-color: $main-blue-20;
    background-color: $main-blue-20;
  }
}
</style>
