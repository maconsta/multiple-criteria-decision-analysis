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
