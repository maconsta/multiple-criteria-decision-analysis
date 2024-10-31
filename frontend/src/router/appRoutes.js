/* Routes for the application go here */

import HomeApp from "@/views/App/HomeApp.vue";
import Projects from "@/views/App/Projects.vue";
import ProjectEdit from "@/views/App/ProjectEdit.vue";
import TaskEdit from "@/views/App/TaskEdit.vue";
import TaskEditOverview from "@/views/App/TaskEditOverview.vue";
import TaskEditMethod from "@/views/App/TaskEditMethod.vue";
import TaskEditCriteria from "@/views/App/TaskEditCriteria.vue";
import TaskEditAlternatives from "@/views/App/TaskEditAlternatives.vue";
import TaskEditWeights from "@/views/App/TaskEditWeights.vue";
import TaskEditNewCriterion from "@/views/App/TaskEditNewCriterion.vue";
import TaskEditNewAlternative from "@/views/App/TaskEditNewAlternative.vue";
import TaskEditCalculate from "@/views/App/TaskEditCalculate.vue";

export default [
  {
    path: "/app",
    name: "homeApp",
    component: HomeApp,
  },
  {
    path: "/app/projects",
    name: "projects",
    component: Projects,
  },
  {
    path: "/app/project/:projectID/edit",
    name: "projectEdit",
    component: ProjectEdit,
  },
  {
    path: "/app/project/:projectID/task/:taskID",
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
        path: "weights",
        name: "taskEditWeights",
        component: TaskEditWeights,
      },
      {
        path: "new-criterion",
        name: "taskEditNewCriterion",
        component: TaskEditNewCriterion,
      },
      {
        path: "new-alternative",
        name: "taskEditNewAlternative",
        component: TaskEditNewAlternative,
      },
      {
        path: "calculate",
        name: "taskEditCalculate",
        component: TaskEditCalculate,
      },
    ],
  },
];
