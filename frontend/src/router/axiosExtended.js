import axios from "axios";
import router from "@/router/index.js";

const csrfToken = localStorage.getItem("csrfToken");
console.log('CSRF Token:', csrfToken);

const axiosExtended = axios.create({
    baseURL: process.env.VUE_APP_AXIOS_BASE_URL,
    withCredentials: true,
    headers: {
        "X-CSRF-TOKEN": csrfToken ? csrfToken : "",
    },
});

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
