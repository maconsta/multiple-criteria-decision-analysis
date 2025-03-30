/* Routes for the application go here */

import HomeApp from "@/views/App/HomeApp.vue";
import Projects from "@/views/App/Projects.vue";
import ProjectEdit from "@/views/App/ProjectEdit.vue";
import TaskEdit from "@/views/App/TaskEdit.vue";
import TaskEditTradeOff from "@/views/App/TaskEditTradeOff.vue";
import TaskEditCriteria from "@/views/App/TaskEditCriteria.vue";
import TaskEditAlternatives from "@/views/App/TaskEditAlternatives.vue";
import TaskEditNewCriterion from "@/views/App/TaskEditNewCriterion.vue";
import TaskEditNewAlternative from "@/views/App/TaskEditNewAlternative.vue";
import Result from "@/views/App/Result.vue";
import UserProfile from "@/views/App/UserProfile.vue";
import TaskEditMethod from "@/views/App/TaskEditMethod.vue";

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
                path: "trade-off",
                name: "taskEditTradeOff",
                component: TaskEditTradeOff,
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
                path: "new-criterion/:criterionID?", // ? after the variable makes the variable optional
                name: "taskEditNewCriterion",
                component: TaskEditNewCriterion,
                props: true,
            },
            {
                path: "new-alternative",
                name: "taskEditNewAlternative",
                component: TaskEditNewAlternative,
            },
            {
                path: "method",
                name: "taskEditMethod",
                component: TaskEditMethod,
            },
            {
                path: "result",
                name: "result",
                component: Result,
            },
        ],
    },
    {
        path: "/app/profile",
        name: "userProfile",
        component: UserProfile,
    },
];
