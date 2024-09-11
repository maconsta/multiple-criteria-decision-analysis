<template>
  <div class="home">
    <TheHeader />
    <h1 @click="callTestApi">Home</h1>
  </div>
</template>

<script>
// @ is an alias to /src
import TheHeader from "@/components/AppComponents/TheHeader.vue";
import axios from "axios";

export default {
  name: "HomeApp",
  components: {
    TheHeader,
  },
  methods: {
    getCookie(name) {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(";").shift();
    },
    callTestApi() {
      console.log(this.getCookie("csrf_access_token"));
      const path = "http://127.0.0.1:5000/test-api";
      const axiosPromise = axios.post(
        path,
        {},
        {
          withCredentials: true,
          headers: {
            "X-CSRF-TOKEN": localStorage.getItem("csrfToken"),
          },
        }
      );

      axiosPromise.then((result) => {
        console.log(result)
      })
    },
  },
};
</script>
