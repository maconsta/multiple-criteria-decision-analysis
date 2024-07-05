import { reactive } from "vue";

export const helpText = reactive({
  heading: "Desctiption",
  text: "Help related to the process will be shown here.",
});

/**
 * @param {String} heading The Heading in the help sidebar
 * @param {String} text The Text in the help sidebar
 */
export function changeHelpText(heading, text) {
  helpText.heading = heading;
  helpText.text = text;
}

export const selectedMethod = reactive({
  method: "",
});

export const criteria = reactive({ criteria: [] });

export const alternatives = reactive({ alternatives: [] });

export const weights = reactive({ matrix: [] });

// TODO: IMPORTANT make a function that fills the crits and alts FROM THE DB and implement it here