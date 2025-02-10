import axios from "axios";
import router from "@/router/index.js";

const accessToken = localStorage.getItem("accessToken");
const axiosExtended = axios.create({
    baseURL: process.env.VUE_APP_AXIOS_BASE_URL,
    headers: {
        "Authorization": accessToken ? `Bearer ${accessToken}` : "",
    },
});

// we need it just in case
axiosExtended.interceptors.request.use(
    (config) => {
        const accessToken = localStorage.getItem("accessToken");
        if (accessToken) {
            config.headers["Authorization"] = `Bearer ${accessToken}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

axiosExtended.interceptors.response.use(
    (response) => response,
    (error) => {
        if (error.response.status === 401) {
            router.push({
                name: "signIn",
            });
        }
    }
);

export default axiosExtended;
