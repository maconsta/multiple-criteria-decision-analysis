import axios from "axios";
import router from "@/router/index.js";

const axiosExtended = axios.create({
  baseURL: process.env.VUE_APP_AXIOS_BASE_URL,
  withCredentials: true,
  headers: {
    "X-CSRF-TOKEN": localStorage.getItem("csrfToken"),
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
