import {createApp} from "vue";
import App from "./App.vue";
import router from "./router";
import FloatingVue from "floating-vue";
import "floating-vue/dist/style.css";
import {LoadingPlugin} from "vue-loading-overlay";
import 'vue-loading-overlay/dist/css/index.css';

const app = createApp(App);
app.use(router);
app.use(FloatingVue);

// default LoadingPlugin config
app.use(LoadingPlugin, {
    loader: "spinner",
    "lock-scroll": true,
    color: "#2c64ff",
    opacity: 1,
    "is-full-page": false
});

app.mount("#app");
