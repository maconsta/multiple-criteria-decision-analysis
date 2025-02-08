import axios from "axios";
import router from "@/router/index.js";

const accessToken = localStorage.getItem("accessToken");
console.log('JWT Token:', accessToken);  // Add this for debugging
const axiosExtended = axios.create({
    baseURL: process.env.VUE_APP_AXIOS_BASE_URL,
    headers: {
        "Authorization": accessToken ? `Bearer ${accessToken}` : "",
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
