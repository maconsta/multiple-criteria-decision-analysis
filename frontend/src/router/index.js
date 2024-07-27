import { createRouter, createWebHistory } from "vue-router";

import landingRoutes from "./landingRoutes.js";
import appRoutes from "./appRoutes.js";

const routes = landingRoutes.concat(appRoutes);

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: routes,
});

export default router;
