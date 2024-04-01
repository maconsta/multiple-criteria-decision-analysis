/* Routes for the default landing page go here

   Domain: www.synthetiq.com
*/

import HomeView from "../views/Landing/HomeView.vue";
import SolutionsView from "../views/Landing/SolutionsView.vue";

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
];
