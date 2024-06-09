/* Routes for the application go here

   Domain: app.synthetiq.com
*/

import Home from "@/views/App/Home.vue";
import Projects from "@/views/App/Projects.vue";
import ProjectEdit from "@/views/App/ProjectEdit.vue";
import TaskEdit from "@/views/App/TaskEdit.vue";
import TaskEditOverview from "@/views/App/TaskEditOverview.vue";
import TaskEditMethod from "@/views/App/TaskEditMethod.vue";
import TaskEditCriteria from "@/views/App/TaskEditCriteria.vue";
import TaskEditAlternatives from "@/views/App/TaskEditAlternatives.vue";
import TaskEditResult from "@/views/App/TaskEditResult.vue";
import TaskEditNewCriterion from "@/views/App/TaskEditNewCriterion.vue";

export default [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/projects",
    name: "projects",
    component: Projects,
  },
  {
    path: "/project/:projectID/edit",
    name: "projectEdit",
    component: ProjectEdit,
  },
  {
    path: "/task/:taskID",
    name: "taskEdit",
    component: TaskEdit,
    children: [
      {
        path: "overview",
        name: "taskEditOverview",
        component: TaskEditOverview,
      },
      {
        path: "method",
        name: "taskEditMethod",
        component: TaskEditMethod,
      },
      {
        path: "criteria",
        name: "taskEditCriteria",
        component: TaskEditCriteria,
      },
      {
        path: "alternatives",
        name: "taskEditAlternatives",
        component: TaskEditAlternatives,
      },
      {
        path: "result",
        name: "taskEditResult",
        component: TaskEditResult,
      },
      {
        path: "new-criterion",
        name: "taskEditNewCriterion",
        component: TaskEditNewCriterion,
      },
    ],
  },
  {
    path: "/signIn",
    name: "signIn",
    component : LoginView,
  },
];
