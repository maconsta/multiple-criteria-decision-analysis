import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import FloatingVue from "floating-vue";
import "floating-vue/dist/style.css";
import VueCookies from "vue-cookies";

const app = createApp(App);
app.use(router);
app.use(FloatingVue);
app.use(VueCookies, { expires: "7d" });
app.mount("#app");
