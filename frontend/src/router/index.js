import { createRouter, createWebHistory } from "vue-router";

import landingRoutes from "./landingRoutes.js";
import appRoutes from "./appRoutes.js";

// logic to determine the subdomain
const host = window.location.host;
const parts = host.split(".");
// const domainLength = 3; // app.synthetiq.com => domain length = 3

let routes = [];
if (parts[0] === "www" || parts[0] === "localhost:8080") {
  routes = landingRoutes;
} else if (parts[0] === "app") {
  routes = appRoutes;
}

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: routes,
});

export default router;
