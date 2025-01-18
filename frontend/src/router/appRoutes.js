/* Routes for the application go here */

import HomeApp from "@/views/App/HomeApp.vue";
import Projects from "@/views/App/Projects.vue";
import ProjectEdit from "@/views/App/ProjectEdit.vue";
import TaskEdit from "@/views/App/TaskEdit.vue";
import TaskEditTradeOffs from "@/views/App/TaskEditTradeOffs.vue";
import TaskEditCriteria from "@/views/App/TaskEditCriteria.vue";
import TaskEditAlternatives from "@/views/App/TaskEditAlternatives.vue";
import TaskEditNewCriterion from "@/views/App/TaskEditNewCriterion.vue";
import TaskEditNewAlternative from "@/views/App/TaskEditNewAlternative.vue";
import TaskEditNewTradeOff from "@/views/App/TaskEditNewTradeOff.vue";
import Result from "@/views/App/Result.vue"
import UserProfile from "@/views/App/UserProfile.vue";

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
        path: "trade-offs",
        name: "taskEditTradeOffs",
        component: TaskEditTradeOffs,
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
        path: "new-trade-off",
        name: "taskEditNewTradeOff",
        component: TaskEditNewTradeOff,
      }
    ],
  },
  {
    path: "/app/project/:projectID/task/:taskID/result",
    name: "result",
    component: Result,
  },
  {
    path: "/app/profile",
    name: "userProfile",
    component: UserProfile,
  },

];
