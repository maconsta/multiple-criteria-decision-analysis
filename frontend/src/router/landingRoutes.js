/* Routes for the default landing page go here */

import HomeView from "../views/Landing/HomeView.vue";
import SolutionsView from "../views/Landing/SolutionsView.vue";
import LoginView from "../views/App/LoginView.vue";

export default [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/solutions",
    name: "solutions",
    component: SolutionsView,
  },
  {
    path: "/signIn",
    name: "signIn",
    component: LoginView,
  },
];
