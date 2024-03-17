/* Routes for the default landing page go here

   Domain: www.synthetiq.com
*/

import HomeView from "../views/Landing/HomeView.vue";

export default [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
];
