/* Routes for the application go here

   Domain: app.synthetiq.com
*/

import HomeView from "../views/App/HomeView.vue";
import ProjectsView from "../views/App/ProjectsView.vue";
import LoginView from "../views/App/LoginView.vue";

export default [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/projects",
    name: "projects",
    component: ProjectsView,
  },
  {
    path: "/signIn",
    name: "signIn",
    component : LoginView,
  },
];
