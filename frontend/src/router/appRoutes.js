/* Routes for the application go here

   Domain: app.synthetiq.com
*/

import Home from "@/views/App/Home.vue";
import Projects from "@/views/App/Projects.vue";
import ProjectEdit from "@/views/App/ProjectEdit.vue";
import TaskEdit from "@/views/App/TaskEdit.vue";
import TaskEditMethod from "@/views/App/TaskEditMethod.vue";
import TaskEditCriteria from "@/views/App/TaskEditCriteria.vue";

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
        path: "method",
        name: "taskEditMethod",
        component: TaskEditMethod,
      },
      {
        path: "criteria",
        name: "taskEditCriteria",
        component: TaskEditCriteria,
      },
    ],
  },
];
